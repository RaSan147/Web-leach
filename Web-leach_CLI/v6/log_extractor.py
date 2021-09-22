import Number_sys_conv as Nsys
import html

def extractor006000(_decrypto_dat, column, _decrypto_dat_, line_index):
	if _decrypto_dat[2]=='0x_':
		column[3]= "<b>Failed to start up</b>"
		column[4]= "No internet connection and old update file not found"

	elif _decrypto_dat[2]=='0x*':
		column[3]= "<b>Session terminated</b>"
		column[4]= "Program and server closed"

	elif _decrypto_dat[2]=='0x0':
		column[3]= "<b>User exit</b>"
		column[4]= "Waiting to be terminated"

	elif _decrypto_dat[2]=='0x1':
		column[3]= '%s (called from %s)' %(_decrypto_dat[4],_decrypto_dat[3])
		column[4]= "Waiting to be terminated"

	elif _decrypto_dat[2]=='000':
		temp= " (Called from %s)"%_decrypto_dat[3]
		if _decrypto_dat[5]=='f-Stop':
			temp1= "Input cancelled from \"%s\""%_decrypto_dat[4]
			temp2= ' (<b>Situation: </b> %s)'%_decrypto_dat[6]
			column[3]= '<br>'.join([temp1, temp, temp2])

			column[4]= _decrypto_dat[7]

		elif _decrypto_dat[5]=='D-Break':
			column[3] = "Thread download task cancelled"+temp
			column[4]= "Waiting to break all threads"

		elif _decrypto_dat[5]=='D-Stop':
			column[3] = "Downloading Stopped"
			try:
				temp= '<b>Downloaded: </b> %s<br><b>Error: </b> %s'%tuple(_decrypto_dat[4].split('|'))
			except:
				print([_decrypto_dat_], line_index)
				return None
			column[4] = temp

		
		else: 
			column[3]= "<b>Unknown Error occured</b><br><b>Project:<b> "+_decrypto_dat[4]
			column[4]= "<b><u>Messages</u>:</b><br>%s"%("<br>".join(_decrypto_dat[5:]))





	elif _decrypto_dat[2]=='001':
		temp= "<u><b>App V </u></b>"+_decrypto_dat[3]+"<br><u><b>Launched at</u>:</b> "+("%s/%s/%s  %s: %s: %s" %Nsys.dec_dt(_decrypto_dat[6]))+"<br><u><b>User Ip</u>: </b> "+_decrypto_dat[5]+(
				"<br><u><b>Timezone</u>:</b> %s<br><u><b>Start up latency</u>: </b> %s"%(_decrypto_dat[7],_decrypto_dat[8]))

		_temp = eval(html.unescape(_decrypto_dat[4]))
		_temp2=''
		for key in _temp:
			_temp2+='<tr><td><b>%s</b></td><td>%s</td></tr>\n'%(key, _temp[key])

		_temp2 = '<table class= "device_info">%s</table>'%_temp2
		column[3]=temp
		column[4]= _temp2
		del temp, _temp, _temp2
		#_decrypto_dat=_decrypto_dat[: 5]


	elif _decrypto_dat[2]== '002':
		column[4]= "<u><b>Server version</u>: </b> "+_decrypto_dat[4]+"<br><b><u>Load latency: </b></u> "+_decrypto_dat[3]
		column[3]= "Server connected successfully!"

	elif _decrypto_dat[2]== '003':
		# print(_decrypto_dat[4])
		column[4] = "<u><b>User Hash</u>: </b> "+_decrypto_dat[3]+"<br><u><b>Log in at</u></b> "+"%s/%s/%s %s: %s: %s" %Nsys.dec_dt(_decrypto_dat[4])
		column[3] = 'User logged in'



	#####################################################
	#####################################################
	#
	#          NEED TO UPDATE THIS PART
	#
	#####################################################
	#####################################################
	elif _decrypto_dat[2] == "201":
		_decrypto_dat[3] = '<i>(Updating app)</i><br>Updating to <b><u>latest version</u>: </b> %sb <br><u><b>From: </b></u> %s'%(_decrypto_dat[3],_decrypto_dat[4])
		if len(_decrypto_dat) == 6:
			_decrypto_dat[4] = '<b><u>Server version</u>: </b> %s'%( _decrypto_dat[5])
		elif len(_decrypto_dat) == 7:
			_decrypto_dat[4] = '<b><u>Current version</u>: </b> %s <br><b><u>Server version</u>: </b> %s'%(_decrypto_dat[5], _decrypto_dat[6])


		else: return False


	elif _decrypto_dat[2] == '202':
		_decrypto_dat[4]= '<b><u>Update file link</u>: </b> %s <br><b><u>Header index</u>: </b> %s'%(_decrypto_dat[3], _decrypto_dat[4])
		_decrypto_dat[3]= '<i>(Updating app)</i><br><b><u>Network issue</u>: </b> %s'%(_decrypto_dat[5])

	elif _decrypto_dat[2] == '203':
		_decrypto_dat.append('<i>Downloaded in: </i><br> '+_decrypto_dat[3])
		_decrypto_dat[3]= '<i>(Updating app)</i><br><b><u>Download Complete</u></b>'

	elif _decrypto_dat[2] == '204':
		_decrypto_dat[4]= '<b><u>Update file link</u>: </b> %s <br><b><u>Latest Version</u>: </b> %s<br><b><u>Server link</u>: </b> %s<br><b><u>File list</u>: </b> %s'%(_decrypto_dat[3], _decrypto_dat[4], _decrypto_dat[5], _decrypto_dat[6])
		_decrypto_dat[3]= '<i>(Updating app)</i><br><b><u>Corrupted zip</u>: </b> The zip contains files other than the main .EXE file<br><i>Will be depricated in v0.5.500002</i>'

	elif _decrypto_dat[2] == '205':
		_decrypto_dat.append('-')
		_decrypto_dat[3]= '<i>(Updating app)</i><br><b><u>Zip extracted</u></b>'

	elif _decrypto_dat[2] == '206':
		_decrypto_dat.append('<i>(Updating app)</i><br><b><u>Update complete</u></b>')
		_decrypto_dat.append('-')

	elif _decrypto_dat[2] == '207':
		_decrypto_dat.append('<i>(Updating app)</i><br><b><u>Zip removed</u></b>')
		_decrypto_dat.append('-')

	elif _decrypto_dat[2] == '208':
		_decrypto_dat[4]= '<b><u>Fake EXE MD5</u>: </b> %s <br><b><u>File Link</u>: </b> %s<br><b><u>Latest Version</u>: </b> %s<br><b><u>Server link</u>: </b> %s'%(_decrypto_dat[3], _decrypto_dat[4], _decrypto_dat[5], _decrypto_dat[6])
		_decrypto_dat[3]= '<i>(Updating app)</i><br><b><u>Corrupted EXE</u>: </b> MD5 of Downloaded EXE don\'t match with server MD5'

	elif _decrypto_dat[2] == '209':
		_decrypto_dat[4]= '<b><u>Fake ZIP MD5</u>: </b> %s <br><b><u>File Link</u>: </b> %s<br><b><u>Latest Version</u>: </b> %s<br><b><u>Server link</u>: </b> %s'%(_decrypto_dat[3], _decrypto_dat[4], _decrypto_dat[5], _decrypto_dat[6])
		_decrypto_dat[3]= '<i>(Updating app)</i><br><b><u>Corrupted ZIP</u>: </b> MD5 of Downloaded ZIP don\'t match with server MD5'


	elif _decrypto_dat[2] == '2FF':
		if len(_decrypto_dat)==8:
			_decrypto_dat = '||'.join(_decrypto_dat).replace('Hashing', '||Hashing').split('||')

		_decrypto_dat[4]= '<b><u>Error Code</u>: </b> %s<br><b><u>Error String</u>: </b> %s<br><b><u>File Link</u>: </b> %s<br><b><u>Latest Version</u>: </b> %s<br><b><u>Server link</u>: </b> %s'%(_decrypto_dat[7], _decrypto_dat[8], _decrypto_dat[3], _decrypto_dat[4], _decrypto_dat[5])
		_decrypto_dat[3]= '<i>(Updating app)</i><br><b><u>Unknown error occured</u></b><br>When <i>%s</i>'%_decrypto_dat[6]

	####################################################
	####################################################

	elif len(_decrypto_dat[2].split('x'))>1:
		fcode = _decrypto_dat[2].split('x')[0]
		ecode = _decrypto_dat[2].split('x')[1]

		column[2] = f'<a href="fcode={fcode}">{fcode}</a>' ' x '+ ecode

		if fcode == '0306':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while running Appconfig~god_mode'

				column[4] = '<b>Error Code: </b>' + _decrypto_dat[5] + '<br>' + '<b>Error String: </b>' + _decrypto_dat[6] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[3] + '<br>' + '<b>Message: </b>' + _decrypto_dat[7]

			elif ecode == '1':
				column[3] = '<b><u>Site Error</u>: </b>  <br>while running <b>Appconfig</b>~<b>god_mode</b>'

				column[4] = 'Failed to download "who_r_u.mp3"<hr><b>Status Code: </b>' + _decrypto_dat[5] + '<br>' +  '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[3]

			elif ecode == '2':
				column[3] = '<b><u>Site Error</u>: </b>  <br>while running <b>Appconfig</b>~<b>god_mode</b>'

				column[4] = 'Failed to download "who_r_u.mp3"<hr><b>Error Code: </b>' + _decrypto_dat[5] + '<br>' + '<b>Error String: </b>' + _decrypto_dat[6] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[3]

			elif ecode == '3':
				column[3] = '<b><u>Site Error</u>: </b>  <br>while running <b>Appconfig</b>~<b>god_mode</b>'

				column[4] = 'Failed to download "updateL.ext"<hr><b>Status Code: </b>' + _decrypto_dat[5] + '<br>' +  '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[3]

			elif ecode == '4':
				column[3] = '<b><u>Site Error</u>: </b>  <br>while running <b>Appconfig</b>~<b>god_mode</b>'

				column[4] = 'Failed to download "updateL.ext"<hr><b>Error Code: </b>' + _decrypto_dat[5] + '<br>' + '<b>Error String: </b>' + _decrypto_dat[6] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[3]

			elif ecode == '5':
				column[3] = '<b><u>Site Error</u>: </b>  <br>while running <b>Appconfig</b>~<b>god_mode</b>'

				column[4] = 'Failed to download "updateG.ext"<hr><b>Status Code: </b>' + _decrypto_dat[5] + '<br>' +  '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[3]

			elif ecode == '6':
				column[3] = '<b><u>Site Error</u>: </b>  <br>while running <b>Appconfig</b>~<b>god_mode</b>'

				column[4] = 'Failed to download "updateG.ext"<hr><b>Error Code: </b>' + _decrypto_dat[5] + '<br>' + '<b>Error String: </b>' + _decrypto_dat[6] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[3]


			else: return False

		elif fcode == '0402':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while running <b>UserData</b>~<b>get_user_ip</b>'

				column[4] = 'Failed to connect to "api.myip.com"<hr><b>Header dex: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Error Code: </b>' + _decrypto_dat[4] + '<br>' + '<b>Error String: </b>' + _decrypto_dat[5]

			elif ecode == '1':
				column[3] = '<b><u>Site Error</u></b>  <br>while running <b>UserData</b>~<b>get_user_ip</b>'

				column[4] = 'Failed to connect to "api.myip.com"<hr><b>Header dex: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Status Code: </b>' + _decrypto_dat[4]

			elif ecode == '2':
				column[3] = '<b><u>Network Error</u>: </b>  <br>while running <b>UserData</b>~<b>get_user_ip</b>'

				column[4] = 'Failed to connect to "api.myip.com"<hr><b>Header dex: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Error Code: </b>' + _decrypto_dat[4] + '<br>' + '<b>Error String: </b>' + _decrypto_dat[5]


			else: return False
		elif fcode == '0607':
			if ecode == '1':
				column[3] = '<b><u>Failed to read file</u></b>'

				column[4] = 'File not found<hr><b>File: </b>' + _decrypto_dat[4] + '<br>' + '<b>Output format: </b>' + _decrypto_dat[5] + '<br>' + '<b>Encoding: </b>' + _decrypto_dat[6] + '<br>' + '<b>Igones Encoding error: </b>' + _decrypto_dat[7] + '<br>' + '<b>If the file is missing: </b>' + _decrypto_dat[8]+ '<hr>' + '<b>Caller ID: </b>' + _decrypto_dat[3]

			elif ecode == '2':
				column[3] = '<b><u>Failed to read file</u></b>'

				column[4] = 'Permission Denied<hr><b>File: </b>' + _decrypto_dat[4] + '<br>' + '<b>Output format: </b>' + _decrypto_dat[5] + '<br>' + '<b>Encoding: </b>' + _decrypto_dat[6] + '<br>' + '<b>Igones Encoding error: </b>' + _decrypto_dat[7] + '<br>' + '<b>If the file is missing: </b>' + _decrypto_dat[8]+ '<hr>' + '<b>Caller ID: </b>' + _decrypto_dat[3]

			elif ecode == '3':
				column[3] = '<b><u>Failed to read file</u></b>'
				column[4] = 'Failed to <b>decode</b> the data<hr><b>File: </b>' + _decrypto_dat[4] + '<br>' + '<b>Output format: </b>' + _decrypto_dat[5] + '<br>' + '<b>Encoding: </b>' + _decrypto_dat[6] + '<br>' + '<b>Igones Encoding error: </b>' + _decrypto_dat[7] + '<br>' + '<b>If the file is missing: </b>' + _decrypto_dat[8]+ '<hr>' + '<b>Caller ID: </b>' + _decrypto_dat[3]

			elif ecode == '4':
				column[3] = '<b><u>Failed to read file</u></b>'
				column[4] = 'Failed to <b>encode</b> the data<hr><b>File: </b>' + _decrypto_dat[4] + '<br>' + '<b>Output format: </b>' + _decrypto_dat[5] + '<br>' + '<b>Encoding: </b>' + _decrypto_dat[6] + '<br>' + '<b>Igones Encoding error: </b>' + _decrypto_dat[7] + '<br>' + '<b>If the file is missing: </b>' + _decrypto_dat[8]+ '<hr>' + '<b>Caller ID: </b>' + _decrypto_dat[3]


			else: return False


		elif fcode == '0608':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while running <b>Fsys_</b>~<b>writer</b>'

				column[4] = 'Unknown Error<hr><b>Caller ID: </b>' + _decrypto_dat[3] + '<br>' + '<b>File name: </b>' + _decrypto_dat[4] + '<br>' + '<b>File path: </b>' + _decrypto_dat[5] + '<br>' + '<b>Data type: </b>' + _decrypto_dat[7] + '<br>' + '<b>Write mode: </b>'+ _decrypto_dat[6] + '<br>' + '<b>Encoding: </b>' + _decrypto_dat[8] + '<hr>' + '<b>Error Code: </b>' + _decrypto_dat[9] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[10]

			elif ecode == '1':
				column[3] = '<b><u>Failed to write file</u></b>' + '<br>' + '<b>File/Folder name</b> contains Invalid charecters'

				column[4] = '<b>Caller ID: </b>' + _decrypto_dat[3] + '<br>' + '<b>File name: </b>' + _decrypto_dat[4] + '<br>' + '<b>File path: </b>' + _decrypto_dat[5] + '<br>' + '<b>Data type: </b>' + _decrypto_dat[7] + '<br>' + '<b>Write mode: </b>'+ _decrypto_dat[6] + '<br>' + '<b>Encoding: </b>' + _decrypto_dat[8]

			elif ecode == '2':
				column[3] = '<b><u>Failed to write file</u></b>' + '<br>' + '<b>Failed to create <b>Folder</b> deu to <b>Permission error</b>'

				column[4] = '<b>Caller ID: </b>' + _decrypto_dat[3] + '<br>' + '<b>File name: </b>' + _decrypto_dat[4] + '<br>' + '<b>File path: </b>' + _decrypto_dat[5] + '<br>' + '<b>Data type: </b>' + _decrypto_dat[7] + '<br>' + '<b>Write mode: </b>'+ _decrypto_dat[6] + '<br>' + '<b>Encoding: </b>' + _decrypto_dat[8] + '<br>' + '<b>Has permission upto: </b>' + _decrypto_dat[9]

			elif ecode == '3':
				column[3] = '<b><u>Failed to write file</u></b>'
				column[4] = 'Invalid write Data type<hr><b>File: </b>' + _decrypto_dat[4] + '<br>' + '<b>Output format: </b>' + _decrypto_dat[5] + '<br>' + '<b>Encoding: </b>' + _decrypto_dat[6] + '<br>' + '<b>Igones Encoding error: </b>' + _decrypto_dat[7] + '<br>' + '<b>If the file is missing: </b>' + _decrypto_dat[8]+ '<hr>' + '<b>Caller ID: </b>' + _decrypto_dat[3]

			elif ecode == 'P':
				column[3] = '<b><u>Failed to write file</u></b>'

				column[4] = 'Permission Denied<hr><b>Caller ID: </b>'+ _decrypto_dat[3] + '<br><b>File name: </b>' + _decrypto_dat[4] + '<br>' + '<b>Output format: </b>' + _decrypto_dat[5] + '<br>' + '<b>Encoding: </b>' + _decrypto_dat[6] + '<br>' + '<b>Igones Encoding error: </b>' + _decrypto_dat[7] + '<br>' + '<b>If the file is missing: </b>' + _decrypto_dat[8]+ '<hr>' + '<b>Caller ID: </b>' + _decrypto_dat[3]


			else: return False

			
		elif fcode == '0704':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while importing make files'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Failed File: </b>' + _decrypto_dat[4] + '<br>' + '<b>Error Code: </b>' + _decrypto_dat[5] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[6]


			else: return False

			
		elif fcode == '0705':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while catching Keyboard Interrupt'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Function name: </b>' + _decrypto_dat[4] + '<br>' + '<b>Message: </b>' + _decrypto_dat[5] 
				

			else: return False

			
		elif fcode == '0803':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while catching Keyboard Interrupt'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Header: </b>' + _decrypto_dat[4] + '<br>' + '<b>Error Code: </b>' + _decrypto_dat[5] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[6]

			elif ecode == '1':
				column[3] = '<b>Header not found</b>'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Header: </b>' + _decrypto_dat[4] + '<br>' + '<b>Possible cause: </b> Data corruption'
				

			else: return False

			
		elif fcode == '0806':
			if ecode == '1':
				column[3] = '<b><u>Internet issue</u></b>  <br>Failed to fetch a link'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>'+ _decrypto_dat[5]+ '<br>' + '<b>Timout: </b>' + _decrypto_dat[6] + '<br>' + '<b>Error Code: </b>' + _decrypto_dat[7] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[8]
				
			elif ecode == '2':
				column[3] = '<b><u>Server issue</u></b>  <br>Failed to fetch a link'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>'+ _decrypto_dat[5]+ '<br>' + '<b>Timout: </b>' + _decrypto_dat[6] + '<br>' + '<b>Status Code: </b>' + _decrypto_dat[7]


			else: return False

			
		elif fcode == '0807':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while running server [Netsys.runserver()]'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Port: </b>' + _decrypto_dat[4] + '<br>' + '<b>cd: </b>' + _decrypto_dat[5] + '<br><b>Error Code: </b>' + _decrypto_dat[6] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[7]

			elif ecode == '1':
				column[3] = '<b><u><i>cd</i> containes invalid charecters</u></b><br>Failed to run server'

				column[4] = '<b>Caller ID: </b>' + _decrypto_dat[3] + '<br>' + '<b>Port: </b>' + _decrypto_dat[4] + '<br>' + '<b>cd: </b>' + _decrypto_dat[5]

			elif ecode == '2':
				column[3] = '<b><u><i>cd</i> is not a directory</u></b><br>Failed to run server'

				column[4] = '<b>Caller ID: </b>' + _decrypto_dat[3] + '<br>' + '<b>Port: </b>' + _decrypto_dat[4] + '<br>' + '<b>cd: </b>' + _decrypto_dat[5]


			else: return False

			
		elif fcode == '080A':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while running server [Netsys.check_server()]'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Timeout: </b>' + _decrypto_dat[5] + '<br><b>Error Code: </b>' + _decrypto_dat[6] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[7]

			elif ecode == '1':
				column[3] = '<b><u>Failed to open server link</u></b><br>Due to App or Network issue'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Timeout: </b>' + _decrypto_dat[5] + '<br><b>Error Code: </b>' + _decrypto_dat[6] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[7]

			
			elif ecode == '2':
				column[3] = '<b><u>Failed to open server link</u></b><br>Due to server file issue <br><b>Possible cause: </b> older server running'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Timeout: </b>' + _decrypto_dat[5] + '<br><b>Status Code: </b>' + _decrypto_dat[6] + '<br>' + '<b>1st 20 chars: </b>' + _decrypto_dat[7]

			elif ecode == '3':
				column[3] = '<b><u>Failed to open server link</u></b><br>Due to server file issue<br><b>Possible cause: </b> port is used by other app'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Timeout: </b>' + _decrypto_dat[5] + '<br><b>Status Code: </b>' + _decrypto_dat[6]


			else: return False

			
		elif fcode == '0902':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while running [Datasys.remove_non_ascii()]'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Text: </b>' + _decrypto_dat[4]+  '<br><b>Error Code: </b>' + _decrypto_dat[5] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[6]


			else: return False

			
		elif fcode == '0903':
			if ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u></b>  <br>while running [Datasys.remove_non_uni()<hr>returning <i>remove_non_ascii()<i>]'

				column[4] = '<b>Caller ID: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Text: </b>' + _decrypto_dat[4]+ '<br><b>Output Type: </b>' + _decrypto_dat[5] +  '<br><b>Encoding: </b>' + _decrypto_dat[6] + '<br>' + '<b>Error Code: </b>'+ _decrypto_dat[7] + '<b>Error Message: </b>' + _decrypto_dat[8]


			else: return False

			

		elif fcode == '0A02':
			if ecode == '1':
				column[3] = '<b>Failed to download <u>yamatte file</u> due to server error'

				column[4] = '<b>Link: </b>' + _decrypto_dat[3] + '<br>' + '<b>Status code</b>:' + _decrypto_dat[4]

			elif ecode == '2':
				column[3] = '<b>Failed to download <u>yamatte file</u> due to Network error'

				column[4] = '<b>Link: </b>' + _decrypto_dat[3] + '<br>' + '<b>Rerror code</b>:' + _decrypto_dat[4]


			else: return False

			




		elif fcode == '0P0B':
			if ecode == '1':
				column[3] = '<b><u>Failed to <i>re-Download</i></u></b><br>Due to server file issue'
				
				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[5] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[4] + '<br><b>File name: </b>' + _decrypto_dat[6] + '<br><b>File dir: </b>' + _decrypto_dat[7] + '<br><b>Status Code: </b>' + _decrypto_dat[8]

			
			elif ecode == '2':
				column[3] = '<b><u>Failed to <i>re-Download</i></u></b><br>Due to Network issue'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[5] + '<br>' + '<b>Header dex:</b>' + _decrypto_dat[4] + '<br><b>File name: </b>' + _decrypto_dat[6] + '<br><b>File dir: </b>' + _decrypto_dat[7]  + '<br><b>Error Code: </b>' + _decrypto_dat[8] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[9]

			elif ecode == '3':
				column[3] = '<b><u>Failed to <i>extract ZIp</i></u></b>'
				
				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[5] + '<br>' + '<b>Header dex:</b>' + _decrypto_dat[4] + '<br><b>File name: </b>' + _decrypto_dat[6] + '<br><b>File dir: </b>' + _decrypto_dat[7]  + '<br><b>Error Code: </b>' + _decrypto_dat[8] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[9]


			else: return False

			

		elif fcode == '0P0C':
			if ecode == 'I':
				column[3] = '<b><u>Began to <i>re-Download</i></u></b>'
				
				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Total files: </b>' + _decrypto_dat[4] + '<br>' + '<b>Downloaded files: </b>' + _decrypto_dat[5] + '<br><b>Failed: </b>' + _decrypto_dat[6]
				
			
			elif ecode == '1':
				column[3] = '<b>Failed to load <u>"errors.wlerr"</u> while <i>re-Downloading</i></b>'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Total files: </b>' + _decrypto_dat[4] + '<br>' + '<b>Downloaded files: </b>' + _decrypto_dat[5] + '<br><b>Failed: </b>' + _decrypto_dat[6]
				
			elif ecode == '2':
				column[3] = '<b><i>retry_errors</i> Function exited successfully</b>'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Total files: </b>' + _decrypto_dat[4] + '<br>' + '<b>Downloaded files: </b>' + _decrypto_dat[5] + '<br><b>Failed: </b>' + _decrypto_dat[6]
				

			else: return False

			

		elif fcode == '0P0D':
			if ecode == '1':
				column[3] = '<b><u>Failed to index link</u></b>'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br>' + '<b>Link: </b>' + _decrypto_dat[5] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[4] + '<br><b>Status/Error Code: </b>' + _decrypto_dat[6] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[7]


			else: return False

			

		elif fcode == '0P0F':
			if ecode == '0':
				column[3] = '<b><u>Unknow Error occured while <i>Indexing</i></u></b>'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br><b>Error Code: </b>' + _decrypto_dat[4] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[5]


			else: return False

			
		elif fcode == '0P0N':
			if ecode == '1':
				column[3] = '<b><u>Failed to connect <a href="https://nhentai.net">nhentai.net</a></u></b><br><b>Possible cause</b>: possible cause wrong link or location blocked or internet issue'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br><b>NH Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[5]

			elif ecode == '2':
				column[3] = '<b><u>Failed to connect <a href="https://nhentai.to">nhentai.to</a></u></b>[DEPRICATED]<br><b>Possible cause</b>: possible cause wrong link or internet issue'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br><b>NH Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[5]

			elif ecode == '3':
				column[3] = '<b><u>Failed to connect <a href="https://nhentai.xxx">nhentai.xxx</a></u></b><br><b>Possible cause</b>: possible cause wrong link or location blocked or internet issue'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br><b>NH Link: </b>' + _decrypto_dat[4] + '<br>' + '<b>Header dex: </b>' + _decrypto_dat[5]


			else: return False

			

		elif fcode == '0P0W':
			if ecode == '0':
				column[3] = '<b><u>Unknown error occured</u><br>Failed to index links from Webtoon</u></b>'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br><b>Webtoon link: </b>' + _decrypto_dat[4] + '<br><b>Status/Error Code: </b>' + _decrypto_dat[6] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[7]

			elif ecode == 'X':
				column[3] = '<b><u>Invalid link</u><br>Failed to pass link REGEX for Webtoon</u></b>'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br><b>Webtoon link: </b>' + _decrypto_dat[4] 
			else: return False

			
		elif fcode == '7001':
			if ecode == 'I':
				column[3] = '<b><u>HTML creation Began</u></b>'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br><b>Sort files: </b>' + _decrypto_dat[4] + '<br><b>File extension: </b>' + _decrypto_dat[5] + '<br><b>Sort directories: </b>' + _decrypto_dat[6]

			elif ecode == '0':
				column[3] = '<b><u>Unknown Error occured</u> while generating web pages using make_html</b>'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3] + '<br><b>Error Code: </b>' + _decrypto_dat[4] + '<br>' + '<b>Error Message: </b>' + _decrypto_dat[5]

			elif ecode == '1':
				column[3] = '<b><u>User cancelled HTML generation</u></b>'

				column[4] = '<b>Project: </b>'+ _decrypto_dat[3]


			else: return False

		

		else: return False

	# print("extracted data: ", column)
	return column

def extractor(_Vcode, _decrypto_dat, column, _decrypto_dat_, line_index):
	if _Vcode in ['006000', '006015']:
		return extractor006000(_decrypto_dat, column, _decrypto_dat_, line_index)

	else:
		return extractor006000(_decrypto_dat, column, _decrypto_dat_, line_index)
