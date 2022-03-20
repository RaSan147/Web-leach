from os import system as os_system
from platform import system as os_name
os_name = os_name()
from sys import stdout as sys_stdout
sys_write = sys_stdout.write
del sys_stdout
import rcrypto
from constants import Constants, AboutApp

from print_text import xprint

from html import escape as html_escape


from exceptions import LeachICancelError, LeachKnownError

import Number_sys_conv as Nsys

from hashlib import sha1 as hashlib_sha1


class IOsys_:  # fc=0500
	""" Contains Input and Output functions """
	def __init__(self, config):
		self.config = config
		self.process_id = config.process_id

	def clear_screen(self):  # fc=0501 v
		"""clears terminal output screen"""

		if os_name == "Windows":
			os_system('cls')
		else:
			os_system('clear')

	def delete_last_line(self, lines=1):  # fc=0502 v
		"""Use this function to delete the last line in the STDOUT

		args:
		-----
			lines: total number of lines *1
				0 to delete current line"""

		# return 0
		if lines == 0:
			sys_write('\n')
			self.delete_last_line()
			return 0

		for _ in range(lines):
			# cursor up one line
			sys_write('\x1b[1A')

			# delete last line
			sys_write('\x1b[2K')

	def leach_logger(self, io, key='lock'):  # fc=0503 v
		"""saves encrypted logger data to file\n
		(new in 5.3_class: auto adds dt_() at the beginning)

		args:
		-----
			io: the log message\n
			key: salt text"""

		if self.config.sp_arg_flag['no log']:
			return None
		try:
			while True:
				try:
					try:
						_key = "Asuna"
						salt = hashlib_sha1(key.encode()).hexdigest()[:-6] + AboutApp._Vcode

						Fsys.writer('userlog.leach', 'ab', rcrypto.encrypt(salt + ('%s||'%Nsys.compressed_dt()) + str(self.process_id) + '||' + html_escape(io) + '||', _key).encode('utf-8') + b'\n', 'data', '00008')
						break
					except EOFError:
						pass
					except KeyboardInterrupt:
						pass
				except EOFError:
					pass
				except KeyboardInterrupt:
					pass

		except EOFError:
			self.leach_logger(io, key='lock')
		except KeyboardInterrupt:
			self.leach_logger(io, key='lock')

	def safe_input(self, msg='', i_func=input, o_func=xprint,
	               on_error=LeachICancelError):  # fc=0504 v
		"""gets user input and returns str

		args:
		-----
			msg: the message to show for asking input *`empty string`
			i_func: the function used for input *`input()`
			o_func: the function used for msg print *`xprint()`
			on_error: What to do when `^C` pressed *`raise LeachICancelError` or `return None`"""

		o_func(msg, end='')
		try:
			try:
				try:
					box = i_func()
					return box
				except EOFError:
					if on_error == LeachICancelError:
						raise LeachICancelError
					else:
						return on_error
				except KeyboardInterrupt:
					raise LeachICancelError
				except LeachICancelError:
					# leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
					exit(0)
			except EOFError:
				if on_error == LeachICancelError:
					raise LeachICancelError
				else:
					return on_error
			except KeyboardInterrupt:
				if on_error == LeachICancelError:
					raise LeachICancelError
				else:
					return on_error
		except EOFError:
			if on_error == LeachICancelError:
				raise LeachICancelError
			else:
				return on_error
		except KeyboardInterrupt:
			if on_error == LeachICancelError:
				raise LeachICancelError
			else:
				return on_error

	def asker(self, out='', default=None, True_False=(True, False),
	          extra_opt=tuple(), extra_return=tuple(),
	          i_func=input, o_func=xprint, on_error=LeachICancelError,
	          condERR=Constants.condERR, no_bool=False):  # fc=0505 v
		"""asks for yes no or equivalent inputs

		args:
		-----
			out: `xprint` text to ask tha question *`empty string`
			default: default output for empty response *`None`
			True_False: returning data instead of True and False *`(True, False)`
			extra_opt: Add additional options with Yeses and Nos *must be array of single options*
			extra_return: Returns output according to `extra_ops`
			i_func: the function used for input *`input()`
			o_func: the function used for msg print *`xprint()`
			on_error: What to do when `^C` pressed *`raise LeachICancelError` or `return None`
			no_bool: won't take yes no as input [extras required] *`False`"""

		if len(extra_opt) != len(extra_return):
			xprint('/r/Additional options and Additional return data don\'t have equal length/=/')
			raise LeachKnownError

		if no_bool:
			if len(extra_opt) < 1:
				xprint('/r/With no_bool arg, you must give at least 1 extra option [extra_arg & extra_return]/=/')
				raise LeachKnownError

		Ques2 = self.safe_input(out, i_func, o_func, on_error).lower()
		if default is not None and Ques2 == '':
			return default
		# Ques2 = Ques2
		while Ques2 not in (tuple() if no_bool else Constants.cond) + Nsys.flatten_array(extra_opt, tuple):
			Ques2 = self.safe_input(condERR, i_func, o_func, on_error).lower()
		# Ques2 = Ques2

		if not no_bool and Ques2 in Constants.cond:
			if Ques2 in Constants.yes:
				return True_False[0]
			else:
				return True_False[1]
		else:
			return extra_return[extra_opt.index(Ques2)]


