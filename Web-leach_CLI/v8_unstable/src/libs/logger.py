from hashlib import sha1 as hashlib_sha1
from html import escape as html_escape
import os



from . import rcrypto
# from .FNDsys import Fsys

from .config import AboutApp
from . import Number_sys_conv as Nsys


def leach_logger(io, process_id, key='lock'):  # fc=0503 v
	"""saves encrypted logger data to file\n
	(new in 5.3_class: auto adds dt_() at the beginning)

	args:
	-----
		io: the log message\n
		key: salt text"""

	try:
		while True:
			try:
				try:
					_key = "SECret"
					salt = hashlib_sha1(key.encode()).hexdigest()[:-6] + AboutApp._Vcode

					with open(os.path.join(AboutApp.data_dir, 'userlog.leach'), 'ab') as f:
						f.write(rcrypto.encrypt(salt + ('%s||'%Nsys.compressed_dt() + str(process_id) + '||' + html_escape(io) + '||', _key)).encode('utf-8') + b'\n')
						f.close()

					# Fsys.writer('userlog.leach', 'ab', , 'data', '00008')
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
		leach_logger(io, key='lock')
	except KeyboardInterrupt:
		leach_logger(io, key='lock')
