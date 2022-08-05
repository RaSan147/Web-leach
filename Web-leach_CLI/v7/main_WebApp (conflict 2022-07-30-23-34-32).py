log_output = 0

directory_explorer_header = '''
<html>

<head>

<meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1, maximum-scale=1">

<meta charset="UTF-8">

<style type="text/css">
body{
  
  position: relative;
  min-height: 100vh;
}
html, body, input, textarea, select, button {
	border-color: #736b5e;
	color: #e8e6e3;
	background-color: #181a1b !important;
}
* {
	scrollbar-color: #0f0f0f #454a4d;
}


a{
  font-size: 20px;
  font-weight: 600;
  font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
  text-decoration: none;
  color: rgb(64, 164, 247);
}

.link{
  color: #F00;
  background-color: rgba(146, 146, 146, 0.282);
}

.file{
  font-weight: 300;
  color: rgb(240, 41, 117);
}

#footer {
  position: absolute;
  bottom: 0;
  width: 100%%;
  height: 2.5rem;            /* Footer height */
}
</style>


'''



__version__ = "0.6"

__all__ = [
	"HTTPServer", "ThreadingHTTPServer", "BaseHTTPRequestHandler",
	"SimpleHTTPRequestHandler", "CGIHTTPRequestHandler",
]

import copy
import datetime
import email.utils
import html
import http.client
import io
import mimetypes
import os
import posixpath
import select
import shutil
import socket # For gethostbyaddr()
import socketserver
import sys
import time
import urllib.parse

import contextlib
import natsort
from functools import partial

from http import HTTPStatus


import re,json
# Default error message template
DEFAULT_ERROR_MESSAGE = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
		"http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
		<title>Error response</title>
	</head>
	<body>
		<h1>Error response</h1>
		<p>Error code: %(code)d</p>
		<p>Message: %(message)s.</p>
		<p>Error code explanation: %(code)s - %(explain)s.</p>
	</body>
</html>
"""

DEFAULT_ERROR_CONTENT_TYPE = "text/html;charset=utf-8"




class Tools:
	def __init__(self):
		self.styles = {
			"equal" : "=",
			"star"    : "*",
			"hash"  : "#",
			"dash"  : "-",
			"udash": "_"
		}

	def text_box(self, *text, style = "equal"):
		text = " ".join(map(str, text))
		term_col = shutil.get_terminal_size()[0]

		s = self.styles[style] if style in self.styles else style
		tt = ""
		for i in text.split("\n"):
			tt += i.center(term_col) + "\n"
		return (f"\n\n{s*term_col}\n{tt}{s*term_col}\n\n")

tools = Tools()

class HTTPServer(socketserver.TCPServer):

	allow_reuse_address = 1    # Seems to make sense in testing environment

	def server_bind(self):
		"""Override server_bind to store the server name."""
		socketserver.TCPServer.server_bind(self)
		host, port = self.server_address[:2]
		self.server_name = socket.getfqdn(host)
		self.server_port = port


class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
	daemon_threads = True


class BaseHTTPRequestHandler(socketserver.StreamRequestHandler):

	"""
	The various request details are stored in instance variables:

	- client_address is the client IP address in the form (host,
	port);

	- command, path and version are the broken-down request line;

	- headers is an instance of email.message.Message (or a derived
	class) containing the header information;

	- rfile is a file object open for reading positioned at the
	start of the optional input data part;

	- wfile is a file object open for writing.

	"""

	# The Python system version, truncated to its first component.
	sys_version = "Python/" + sys.version.split()[0]

	# The server software version.  You may want to override this.
	# The format is multiple whitespace-separated strings,
	# where each string is of the form name[/version].
	server_version = "BaseHTTP/" + __version__

	error_message_format = DEFAULT_ERROR_MESSAGE
	error_content_type = DEFAULT_ERROR_CONTENT_TYPE

	# The default request version.  This only affects responses up until
	# the point where the request line is parsed, so it mainly decides what
	# the client gets back when sending a malformed request line.
	# Most web servers default to HTTP 0.9, i.e. don't send a status line.
	default_request_version = "HTTP/0.9"

	def parse_request(self):
		"""Parse a request (internal).

		The request should be stored in self.raw_requestline; the results
		are in self.command, self.path, self.request_version and
		self.headers.

		Return True for success, False for failure; on failure, any relevant
		error response has already been sent back.

		"""
		self.command = None  # set in case of error on the first line
		self.request_version = version = self.default_request_version
		self.close_connection = True
		requestline = str(self.raw_requestline, 'iso-8859-1')
		requestline = requestline.rstrip('\r\n')
		self.requestline = requestline
		words = requestline.split()
		if len(words) == 0:
			return False

		if len(words) >= 3:  # Enough to determine protocol version
			version = words[-1]
			try:
				if not version.startswith('HTTP/'):
					raise ValueError
				base_version_number = version.split('/', 1)[1]
				version_number = base_version_number.split(".")
				# RFC 2145 section 3.1 says there can be only one "." and
				#   - major and minor numbers MUST be treated as
				#      separate integers;
				#   - HTTP/2.4 is a lower version than HTTP/2.13, which in
				#      turn is lower than HTTP/12.3;
				#   - Leading zeros MUST be ignored by recipients.
				if len(version_number) != 2:
					raise ValueError
				version_number = int(version_number[0]), int(version_number[1])
			except (ValueError, IndexError):
				self.send_error(
					HTTPStatus.BAD_REQUEST,
					"Bad request version (%r)" % version)
				return False
			if version_number >= (1, 1) and self.protocol_version >= "HTTP/1.1":
				self.close_connection = False
			if version_number >= (2, 0):
				self.send_error(
					HTTPStatus.HTTP_VERSION_NOT_SUPPORTED,
					"Invalid HTTP version (%s)" % base_version_number)
				return False
			self.request_version = version

		if not 2 <= len(words) <= 3:
			self.send_error(
				HTTPStatus.BAD_REQUEST,
				"Bad request syntax (%r)" % requestline)
			return False
		command, path = words[:2]
		if len(words) == 2:
			self.close_connection = True
			if command != 'GET':
				self.send_error(
					HTTPStatus.BAD_REQUEST,
					"Bad HTTP/0.9 request type (%r)" % command)
				return False
		self.command, self.path = command, path

		# Examine the headers and look for a Connection directive.
		try:
			self.headers = http.client.parse_headers(self.rfile,
													 _class=self.MessageClass)
		except http.client.LineTooLong as err:
			self.send_error(
				HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE,
				"Line too long",
				str(err))
			return False
		except http.client.HTTPException as err:
			self.send_error(
				HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE,
				"Too many headers",
				str(err)
			)
			return False

		conntype = self.headers.get('Connection', "")
		if conntype.lower() == 'close':
			self.close_connection = True
		elif (conntype.lower() == 'keep-alive' and
			  self.protocol_version >= "HTTP/1.1"):
			self.close_connection = False
		# Examine the headers and look for an Expect directive
		expect = self.headers.get('Expect', "")
		if (expect.lower() == "100-continue" and
				self.protocol_version >= "HTTP/1.1" and
				self.request_version >= "HTTP/1.1"):
			if not self.handle_expect_100():
				return False
		return True

	def handle_expect_100(self):
		"""Decide what to do with an "Expect: 100-continue" header.

		If the client is expecting a 100 Continue response, we must
		respond with either a 100 Continue or a final response before
		waiting for the request body. The default is to always respond
		with a 100 Continue. You can behave differently (for example,
		reject unauthorized requests) by overriding this method.

		This method should either return True (possibly after sending
		a 100 Continue response) or send an error response and return
		False.

		"""
		self.send_response_only(HTTPStatus.CONTINUE)
		self.end_headers()
		return True

	def handle_one_request(self):
		"""Handle a single HTTP request.

		You normally don't need to override this method; see the class
		__doc__ string for information on how to handle specific HTTP
		commands such as GET and POST.

		"""
		try:
			self.raw_requestline = self.rfile.readline(65537)
			if len(self.raw_requestline) > 65536:
				self.requestline = ''
				self.request_version = ''
				self.command = ''
				self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
				return
			if not self.raw_requestline:
				self.close_connection = True
				return
			if not self.parse_request():
				# An error code has been sent, just exit
				return
			mname = 'do_' + self.command
			if not hasattr(self, mname):
				self.send_error(
					HTTPStatus.NOT_IMPLEMENTED,
					"Unsupported method (%r)" % self.command)
				return
			method = getattr(self, mname)
			method()
			self.wfile.flush() #actually send the response if not already done.
		except TimeoutError as e:
			#a read or a write timed out.  Discard this connection
			self.log_error("Request timed out: %r", e)
			self.close_connection = True
			return

	def handle(self):
		"""Handle multiple requests if necessary."""
		self.close_connection = True

		self.handle_one_request()
		while not self.close_connection:
			self.handle_one_request()

	def send_error(self, code, message=None, explain=None):
		"""Send and log an error reply.

		Arguments are
		* code:    an HTTP error code
				   3 digits
		* message: a simple optional 1 line reason phrase.
				   *( HTAB / SP / VCHAR / %x80-FF )
				   defaults to short entry matching the response code
		* explain: a detailed message defaults to the long entry
				   matching the response code.

		This sends an error response (so it must be called before any
		output has been generated), logs the error, and finally sends
		a piece of HTML explaining the error to the user.

		"""

		try:
			shortmsg, longmsg = self.responses[code]
		except KeyError:
			shortmsg, longmsg = '???', '???'
		if message is None:
			message = shortmsg
		if explain is None:
			explain = longmsg
		self.log_error("code %d, message %s", code, message)
		self.send_response(code, message)
		self.send_header('Connection', 'close')

		# Message body is omitted for cases described in:
		#  - RFC7230: 3.3. 1xx, 204(No Content), 304(Not Modified)
		#  - RFC7231: 6.3.6. 205(Reset Content)
		body = None
		if (code >= 200 and
			code not in (HTTPStatus.NO_CONTENT,
						 HTTPStatus.RESET_CONTENT,
						 HTTPStatus.NOT_MODIFIED)):
			# HTML encode to prevent Cross Site Scripting attacks
			# (see bug #1100201)
			content = (self.error_message_format % {
				'code': code,
				'message': html.escape(message, quote=False),
				'explain': html.escape(explain, quote=False)
			})
			body = content.encode('UTF-8', 'replace')
			self.send_header("Content-Type", self.error_content_type)
			self.send_header('Content-Length', str(len(body)))
		self.end_headers()

		if self.command != 'HEAD' and body:
			self.wfile.write(body)

	def send_response(self, code, message=None):
		"""Add the response header to the headers buffer and log the
		response code.

		Also send two standard headers with the server software
		version and the current date.

		"""
		self.log_request(code)
		self.send_response_only(code, message)
		self.send_header('Server', self.version_string())
		self.send_header('Date', self.date_time_string())

	def send_response_only(self, code, message=None):
		"""Send the response header only."""
		if self.request_version != 'HTTP/0.9':
			if message is None:
				if code in self.responses:
					message = self.responses[code][0]
				else:
					message = ''
			if not hasattr(self, '_headers_buffer'):
				self._headers_buffer = []
			self._headers_buffer.append(("%s %d %s\r\n" %
					(self.protocol_version, code, message)).encode(
						'latin-1', 'strict'))

	def send_header(self, keyword, value):
		"""Send a MIME header to the headers buffer."""
		if self.request_version != 'HTTP/0.9':
			if not hasattr(self, '_headers_buffer'):
				self._headers_buffer = []
			self._headers_buffer.append(
				("%s: %s\r\n" % (keyword, value)).encode('latin-1', 'strict'))

		if keyword.lower() == 'connection':
			if value.lower() == 'close':
				self.close_connection = True
			elif value.lower() == 'keep-alive':
				self.close_connection = False

	def end_headers(self):
		"""Send the blank line ending the MIME headers."""
		if self.request_version != 'HTTP/0.9':
			self._headers_buffer.append(b"\r\n")
			self.flush_headers()

	def flush_headers(self):
		if hasattr(self, '_headers_buffer'):
			self.wfile.write(b"".join(self._headers_buffer))
			self._headers_buffer = []

	def log_request(self, code='-', size='-'):
		"""Log an accepted request.

		This is called by send_response().

		"""
		if isinstance(code, HTTPStatus):
			code = code.value
		self.log_message('"%s" %s %s',
						 self.requestline, str(code), str(size))

	def log_error(self, format, *args):
		"""Log an error.

		This is called when a request cannot be fulfilled.  By
		default it passes the message on to log_message().

		Arguments are the same as for log_message().

		XXX This should go to the separate error log.

		"""

		self.log_message(format, *args)

	def log_message(self, format, *args):
		"""Log an arbitrary message.

		This is used by all other logging functions.  Override
		it if you have specific logging wishes.

		The first argument, FORMAT, is a format string for the
		message to be logged.  If the format string contains
		any % escapes requiring parameters, they should be
		specified as subsequent arguments (it's just like
		printf!).

		The client ip and current date/time are prefixed to
		every message."""
		
		
		#print(log_output)
		
		if log_output:
			sys.stderr.write("%s - - [%s] %s\n" %
						 (self.address_string(),
						  self.log_date_time_string(),
						  format%args))

	def version_string(self):
		"""Return the server software version string."""
		return self.server_version + ' ' + self.sys_version

	def date_time_string(self, timestamp=None):
		"""Return the current date and time formatted for a message header."""
		if timestamp is None:
			timestamp = time.time()
		return email.utils.formatdate(timestamp, usegmt=True)

	def log_date_time_string(self):
		"""Return the current time formatted for logging."""
		now = time.time()
		year, month, day, hh, mm, ss, x, y, z = time.localtime(now)
		s = "%02d/%3s/%04d %02d:%02d:%02d" % (
				day, self.monthname[month], year, hh, mm, ss)
		return s

	weekdayname = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

	monthname = [None,
				 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
				 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

	def address_string(self):
		"""Return the client address."""

		return self.client_address[0]

	# Essentially static class variables

	# The version of the HTTP protocol we support.
	# Set this to HTTP/1.1 to enable automatic keepalive
	protocol_version = "HTTP/1.0"

	# MessageClass used to parse headers
	MessageClass = http.client.HTTPMessage

	# hack to maintain backwards compatibility
	responses = {
		v: (v.phrase, v.description)
		for v in HTTPStatus.__members__.values()
	}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	"""Simple HTTP request handler with GET and HEAD commands.

	This serves files from the current directory and any of its
	subdirectories.  The MIME type for files is determined by
	calling the .guess_type() method.

	The GET and HEAD requests are identical except that the HEAD
	request omits the actual contents of the file.

	"""

	server_version = "SimpleHTTP/" + __version__
	extensions_map = _encodings_map_default = {
		'.gz': 'application/gzip',
		'.Z': 'application/octet-stream',
		'.bz2': 'application/x-bzip2',
		'.xz': 'application/x-xz'
	}
	extensions_map.update({
		'': 'application/octet-stream', # Default
		'.py': 'text/plain',
		'.c': 'text/plain',
		'.h': 'text/plain',
		'.css': 'text/css'
		})

	def __init__(self, *args, directory=None, data_dir="", **kwargs):
		if directory is None:
			directory = os.getcwd()
		self.directory = os.fspath(directory)
		self.data_dir = data_dir
		super().__init__(*args, **kwargs)
		

	def do_GET(self):
		"""Serve a GET request."""
		f = self.send_head()
		if f:
			try:
				self.copyfile(f, self.wfile)
			finally:
				f.close()

	def do_HEAD(self):
		"""Serve a HEAD request."""
		f = self.send_head()
		if f:
			f.close()
			
	
	def do_POST(self):
		"""Serve a POST request."""
		self.range = None # bug patch
		DO_NOT_JSON = False # wont convert r, info to json
		
		

		try:
			post_type, r, info = self.deal_post_data()
		except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError) as e:
			print(tools.text_box(e.__class__.__name__, e,"\nby ", self.client_address))
			return
		if post_type=='get-json':
			return self.list_directory_json()
				
		if post_type== "upload":
			DO_NOT_JSON = True
			
			
		print((r, type, info, "by: ", self.client_address))

		if r==True:
			head = "Success"
		elif r==False:
			head = "Failed"
		
		else:
			head = r

		body = info


		f = io.BytesIO()

		if DO_NOT_JSON:
			data = (head + body)
			content_type = 'text/html'
		else:
			data = json.dumps([head, body])
			content_type = 'application/json'
		
		
		f.write(data.encode('utf-8'))

		length = f.tell()
		f.seek(0)
		self.send_response(200)
		self.send_header("Content-type", content_type)
		self.send_header("Content-Length", str(length))
		self.end_headers()

		if f:
			self.copyfile(f, self.wfile)
			f.close()

	def deal_post_data(self):
		boundary = None
		uid = None
		num = 0
		post_type = None
		blank = 0 # blank is used to check if the post is empty or Connection Aborted

		refresh = "<br><br><div class='pagination center' onclick='window.location.reload()'>Refresh &#128259;</div>"


		def get_rel_path(filename):
			return urllib.parse.unquote(posixpath.join(self.path, filename), errors='surrogatepass')


		def get(show=True, strip=False, self=self):
			"""
			show: print line
			strip: strip \r\n at end
			"""
			nonlocal num, remainbytes, blank

			line = self.rfile.readline()

			if line == b'':
				blank += 1
			else:
				blank = 0
			if blank>=10:
				self.send_error(408, "Request Timeout")
				time.sleep(1) # wait for the client to close the connection
				
				raise ConnectionAbortedError
			if show:
				print(num, line)
				num+=1
			remainbytes -= len(line)

			if strip and line.endswith(b"\r\n"):
				line = line.rpartition(b"\r\n")[0]

			return line

		def pass_bound(self=self):
			nonlocal remainbytes
			line = get(0)
			if not boundary in line:
				return (False, "Content NOT begin with boundary")

		def get_type(line=None, self=self):
			nonlocal remainbytes
			if not line:
				line = get()
			try:
				return re.findall(r'Content-Disposition.*name="(.*?)"', line.decode())[0]
			except: return None

		def skip(self=self):
			get(0)

		def handle_files(self=self):
			nonlocal remainbytes
			uploaded_files = [] # Uploaded folder list

			# pass boundary
			pass_bound()
			
			uploading_path = self.path


			# PASSWORD SYSTEM
			if get_type()!="password":
				return (False, "Invalid request")


			skip()
			password= get(0)
			print('post password: ',  password)
			# if password != config.PASSWORD + b'\r\n': # readline returns password with \r\n at end
			# 	return (False, "Incorrect password") # won't even read what the random guy has to say and slap 'em

			pass_bound()


			while remainbytes > 0:
				line =get()

				fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line.decode())
				if not fn:
					return (False, "Can't find out file name...")
				path = self.translate_path(self.path)
				rltv_path = posixpath.join(self.path, fn[0])

				fn = os.path.join(path, fn[0])
				line = get(0) # content type
				line = get(0) # line gap

				# ORIGINAL FILE STARTS FROM HERE
				try:
					with open(fn, 'wb') as out:
						preline = get(0)
						while remainbytes > 0:
							line = get(0)
							if boundary in line:
								preline = preline[0:-1]
								if preline.endswith(b'\r'):
									preline = preline[0:-1]
								out.write(preline)
								uploaded_files.append(rltv_path,)
								break
							else:
								out.write(preline)
								preline = line
								
				except IOError:
					return (False, "Can't create file to write, do you have permission to write?")
				


			return (True, ("<!DOCTYPE html><html>\n<title>Upload Result Page</title>\n<body>\n<h2>Upload Result Page</h2>\n<hr>\nFile '%s' upload success!" % ",".join(uploaded_files)) +"<br><br><h2><a href=\"%s\">back</a></h2>" % uploading_path)


		while 0:
			line = get()


		content_type = self.headers['content-type']
		print(self.headers)

		if not content_type:
			return (False, "Content-Type header doesn't contain boundary")
		boundary = content_type.split("=")[1].encode()

		remainbytes = int(self.headers['content-length'])


		pass_bound()# LINE 1

		# get post type
		if get_type()=="post-type":
			skip() # newline
		else:
			return (False, "Invalid post request")

		line = get()
		handle_type = line.decode().strip() # post type LINE 3

		pass_bound() #boundary for password or guid of user

		if get_type()=="post-uid":
			skip() # newline
		else:
			return (False, "Unknown User request")

		uid = get() # uid LINE 5

		##################################

		# HANDLE USER PERMISSION BY CHECKING UID

		##################################
		
		r, info = (True, "Something")

		# if handle_type == "upload":
		# 	r, info = handle_files()


		# elif handle_type == "test":
		# 	while remainbytes > 0:
		# 		line =get()

		# elif handle_type == "del-f":
		# 	r, info = del_data()

		# elif handle_type == "del-p":
		# 	r, info = del_permanently()

		# elif handle_type=="rename":
		# 	r, info = rename()

		# elif handle_type=="info":
		# 	r, info = get_info()

		# elif handle_type == "new folder":
		# 	r, info = new_folder()

		# elif handle_type == "get-json":
		# 	r, info = (None, "get-json")

		
		return handle_type, r, info


	def send_head(self):
		"""Common code for GET and HEAD commands.

		This sends the response code and MIME headers.

		Return value is either a file object (which has to be copied
		to the outputfile by the caller unless the command was HEAD,
		and must be closed by the caller under all circumstances), or
		None, in which case the caller has nothing further to do.

		"""
		path = self.translate_path(self.path)
		f = None
		#print(self.data_dir)
		
		
		
		

		if self.path.startswith(("/?scripts", "/?assets")):
			path= self.data_dir+self.path[2:]
		
		if self.path == "/favicon.ico":
			path= self.data_dir+ "assets/icon.ico"
		
		
		
		if self.path == '/root?response':
			outp='Web-leach v6 is up and running'
			encoded = outp.encode('utf-8', 'surrogateescape')

			f = io.BytesIO()
			f.write(encoded)
			
			f.seek(0)
			self.send_response(HTTPStatus.OK)
			self.send_header("Content-type", "text/html; charset=%s" % 'utf-8')
			self.send_header("Content-Length", str(len(encoded)))
			self.end_headers()
			return f

		elif os.path.isdir(path):
			parts = urllib.parse.urlsplit(self.path)
			if not parts.path.endswith('/'):
				# redirect browser - doing basically what apache does
				self.send_response(HTTPStatus.MOVED_PERMANENTLY)
				new_parts = (parts[0], parts[1], parts[2] + '/',
							 parts[3], parts[4])
				new_url = urllib.parse.urlunsplit(new_parts)
				self.send_header("Location", new_url)
				self.send_header("Content-Length", "0")
				self.end_headers()
				return None
			for index in "index.html", "index.htm":
				index = os.path.join(path, index)
				if os.path.exists(index):
					path = index
					break
			else:
				return self.list_directory(path)
		ctype = self.guess_type(path)
		# check for trailing "/" which should return 404. See Issue17324
		# parseing and rejection of filenames with a trailing slash
		if path.endswith("/"):
			self.send_error(HTTPStatus.NOT_FOUND, "File not found")
			return None
		try:
			f = open(path, 'rb')
		except OSError:

			self.send_error(HTTPStatus.NOT_FOUND, "File not found")
			return None

		try:
			fs = os.fstat(f.fileno())
			# Use browser cache if possible
			if ("If-Modified-Since" in self.headers
					and "If-None-Match" not in self.headers):
				# compare If-Modified-Since and time of last file modification
				try:
					ims = email.utils.parsedate_to_datetime(
						self.headers["If-Modified-Since"])
				except (TypeError, IndexError, OverflowError, ValueError):
					# ignore ill-formed values
					pass
				else:
					if ims.tzinfo is None:
						# obsolete format with no timezone, cf.
						# https://tools.ietf.org/html/rfc7231#section-7.1.1.1
						ims = ims.replace(tzinfo=datetime.timezone.utc)
					if ims.tzinfo is datetime.timezone.utc:
						# compare to UTC datetime of last modification
						last_modif = datetime.datetime.fromtimestamp(
							fs.st_mtime, datetime.timezone.utc)
						# remove microseconds, like in If-Modified-Since
						last_modif = last_modif.replace(microsecond=0)

						if last_modif <= ims:
							self.send_response(HTTPStatus.NOT_MODIFIED)
							self.end_headers()
							f.close()
							return None

			self.send_response(HTTPStatus.OK)
			self.send_header("Content-type", ctype)
			self.send_header("Content-Length", str(fs[6]))
			self.send_header("Last-Modified",
				self.date_time_string(fs.st_mtime))
			self.end_headers()
			return f
		except:
			f.close()
			raise


	def list_directory(self, path):
		"""Helper to produce a directory listing (absent index.html).

		Return value is either a file object, or None (indicating an
		error).  In either case, the headers are sent, making the
		interface the same as for send_head().

		"""
		try:
			_list = os.listdir(path)
		except OSError:
			self.send_error(
				HTTPStatus.NOT_FOUND,
				"No permission to list directory")
			return None
		_list= natsort.natsorted(_list,  key= lambda x: x.lower())
		r = []
		try:
			displaypath = urllib.parse.unquote(self.path,
											   errors='surrogatepass')
		except UnicodeDecodeError:
			displaypath = urllib.parse.unquote(path)
		displaypath = html.escape(displaypath, quote=False)
		enc = sys.getfilesystemencoding()
		title = 'Inside %s' % displaypath
		r.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
				 '"http://www.w3.org/TR/html4/strict.dtd">')
		r.append(directory_explorer_header)
		r.append('<meta http-equiv="Content-Type" '
				 'content="text/html; charset=%s">' % enc)
		r.append('<title>%s</title>\n</head>' % title)
		r.append('<body>\n<h1>All files and folders in %s</h1>' % displaypath)
		r.append('<hr>\n<ul>')
		for name in _list:
			fullname = os.path.join(path, name)
			displayname = linkname = name
			_is_dir_= True
			# Append / for directories or @ for symbolic links
			if os.path.isdir(fullname):
				displayname = name + "/"
				linkname = name + "/"
			elif os.path.islink(fullname):
				displayname = name + "@"
				# Note: a link to a directory displays with @ and links with /
			else:
				_is_dir_ =False
				__, ext = posixpath.splitext(fullname)
				if ext=='.html':
					r.append('<li><a class= "%s" href="%s">%s</a></li>'
					% ("link", urllib.parse.quote(linkname,
										  errors='surrogatepass'),
					   html.escape(displayname, quote=False)))
				else:
					r.append('<li><a class= "%s" href="%s">%s</a></li>'
					% ("file", urllib.parse.quote(linkname,
										  errors='surrogatepass'),
					   html.escape(displayname, quote=False)))
			if _is_dir_:
				r.append('<li><a href="%s">%s</a></li>'
					% (urllib.parse.quote(linkname,
										  errors='surrogatepass'),
					   html.escape(displayname, quote=False)))
				
		r.append('</ul><br><br>\n<hr>\n</body>\n<footer id="footer"><br><br><br><br><hr><hr>\n<p style="color: darkgray;">Made by Rasan147 with Web leach</p>\n<br><br>\n</footer></html> \n')
		encoded = '\n'.join(r).encode(enc, 'surrogateescape')
		f = io.BytesIO()
		f.write(encoded)
		f.seek(0)
		self.send_response(HTTPStatus.OK)
		self.send_header("Content-type", "text/html; charset=%s" % enc)
		self.send_header("Content-Length", str(len(encoded)))
		self.end_headers()
		return f

	def translate_path(self, path):
		"""Translate a /-separated PATH to the local filename syntax.

		Components that mean special things to the local file system
		(e.g. drive or directory names) are ignored.  (XXX They should
		probably be diagnosed.)

		"""
		# abandon query parameters
		path = path.split('?',1)[0]
		path = path.split('#',1)[0]
		# Don't forget explicit trailing slash when normalizing. Issue17324
		trailing_slash = path.rstrip().endswith('/')
		try:
			path = urllib.parse.unquote(path, errors='surrogatepass')
		except UnicodeDecodeError:
			path = urllib.parse.unquote(path)
		path = posixpath.normpath(path)
		words = path.split('/')
		words = filter(None, words)
		path = self.directory
		for word in words:
			if os.path.dirname(word) or word in (os.curdir, os.pardir):
				# Ignore components that are not a simple file/directory name
				continue
			path = os.path.join(path, word)
		if trailing_slash:
			path += '/'
		return path

	def copyfile(self, source, outputfile):
		"""Copy all data between two file objects.

		The SOURCE argument is a file object open for reading
		(or anything with a read() method) and the DESTINATION
		argument is a file object open for writing (or
		anything with a write() method).

		The only reason for overriding this would be to change
		the block size or perhaps to replace newlines by CRLF
		-- note however that this the default server uses this
		to copy binary data as well.

		"""
		shutil.copyfileobj(source, outputfile)

	def guess_type(self, path):
		"""Guess the type of a file.

		Argument is a PATH (a filename).

		Return value is a string of the form type/subtype,
		usable for a MIME Content-type header.

		The default implementation looks the file's extension
		up in the table self.extensions_map, using application/octet-stream
		as a default; however it would be permissible (if
		slow) to look inside the data to make a better guess.

		"""

		base, ext = posixpath.splitext(path)
		if ext in self.extensions_map:
			return self.extensions_map[ext]
		ext = ext.lower()
		if ext in self.extensions_map:
			return self.extensions_map[ext]
		guess, _ = mimetypes.guess_type(path)
		if guess:
			return guess
		return 'application/octet-stream'


def _get_best_family(*address):
	infos = socket.getaddrinfo(
		*address,
		type=socket.SOCK_STREAM,
		flags=socket.AI_PASSIVE,
	)
	family, type, proto, canonname, sockaddr = next(iter(infos))
	return family, sockaddr


def test(HandlerClass=BaseHTTPRequestHandler,
		 ServerClass=ThreadingHTTPServer,
		 protocol="HTTP/1.0", port=8000, bind=None):
	"""Test the HTTP request handler class.

	This runs an HTTP server on port 8000 (or the port argument).

	"""
	if sys.version_info>(3,7,2):
		ServerClass.address_family, server_address = _get_best_family(bind, port)
		
	else:
		if bind==None: bind=''
		server_address = (bind, port)

	HandlerClass.protocol_version = protocol
	return ServerClass(server_address, HandlerClass)



# ensure dual-stack is not disabled; ref #38907
class DualStackServer(ThreadingHTTPServer):
	def handle_error(self, request, client_address):
		pass
	def server_bind(self):
		# suppress exception when protocol is IPv4
		with contextlib.suppress(Exception):
			self.socket.setsockopt(
				socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
		return super().server_bind()


def run_server(port = 8000, cd = os.getcwd(), data_dir=""):
	handler_class = partial(SimpleHTTPRequestHandler,
				directory=cd, data_dir=data_dir)
	
	return test(HandlerClass=handler_class,
		ServerClass=DualStackServer, port=port, bind=None)

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	
	parser.add_argument('--bind', '-b', default=None,
						metavar='ADDRESS',
						help='Specify alternate bind address '
							 '[default: all interfaces]')
	parser.add_argument('--directory', '-d', default=os.getcwd(),
						help='Specify alternative directory '
						'[default:current directory]')
	parser.add_argument('port', action='store',
						default=8000, type=int,
						nargs='?',
						help='Specify alternate port [default: 8000]')
	args = parser.parse_args()
	
	handler_class = partial(SimpleHTTPRequestHandler,
								directory=args.directory)
	try:
		test(HandlerClass=handler_class,
			ServerClass=DualStackServer, port=args.port, bind=args.bind).serve_forever()
	except KeyboardInterrupt:
				print("\nKeyboard interrupt received, exiting.")
				sys.exit(0)
