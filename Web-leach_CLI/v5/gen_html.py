
if __name__ == '__main__':
	exec('from leach_all_os import *')

run_server(port)

class offline_leach:
	def __init__(self):      #func_code= 10001
		"""initialize variables on every start of a project"""
		#global overwrite_bool, partial_do_all, homepage, existing_found, dimention,sp_flags, done,indx_count, sp_extension, errors
		print('Using offline mode, downlaod feature is Disabled.\nYou can only view the Downloaded projects from here...')
		self.total=0	  # number of total files
		self.break_all= False	  # trigger to stop the download
		self.done=0	  # total downloaded files
		self.errors=0	# number or errors
		self.sp_extension=''	# if custom file extension needed to be added with the downloaded file names
		self.sp_flags=[]	# list of flags for special downloads like mangafreaks
		self.overwrite_bool= True	# bool for wheather replace the duplicate file or not
		self.partial_do_all= False	# will use the same detected homepage for every other pages with no home
		"""if partial link found while indexing, then the program will find the
		homepage and ask if it will be used for all other partial links or not"""

		self.dimention = 0
		""" number indication how should the program scrap data from the link
		0: default, if 0 will ask for dimention input
		1: scrap from only the main link and won't ask for sublinks
		2: scrap from only the sublinks of the main link
		3: scrap from both main link and and the sublinks"""

		self.homepage= ''	# just assigning the homepage variable
		self.indx_count= 0	# counts the number of indexed links
		self.all_list = []	# assigning a list, but duplicates will be cancelled in process
		self.existing_found=False	# indicates if valid existing project is found
		self.dl_done=False	# indicates if the project scrapping was done or not
		self.sequence=True	# indicates if the files will be sorted or not
		self.update= False	# indicates if the project is getting an update or not
		self.corruptions=[]	# list of corruptions in project data if there's any or empty
		self.sub_dirs=[]	# list of sub directories on the project folder
		self.homepage_searcher=re_compile('(https?://[^/]*)')	# compiled regex tool for getting homepage
		self.Project=''	# project name (case insensitive *need to work on it)
		self.main_link=''	# the main link
		self.file_types= set()	# set of file extensions to be downloaded
		self.file_starts=''	# (str) each files must start with (used regex)
		self.link_startswith=''	# (str) each sublink must start with
		self.error_triggers=[]	# 0 to 9 the number of tasks
		self.open_file = False
		self.dl_chunks=0
		self.from_file= False
		self.page_error = 0
		self.re_error = 0   # number of errors after retrying errors

		self.special_starts ={'nh':'https://nhentai\.((net)|(to)|(xxx))/g/',
		'mangafreak':'https://w[\d]+\.mangafreak.net/(M|m)anga/',
		'nh_sc':'^nh (\d+)$',
		'mf_sc':'^mf (.+)$',
		'pinterest':'https://www.pinterest.com/',
		'mf_read':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(?:_\d+)[\?\#]?.*',
		'mf_read_chap':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(_\d+)[\?\#]?.*'}


	def main_offline(self):
		global death, sp_arg_flag
		"""runs the mainloop of the projects runtime code"""
		self.__init__()


		while True:
			try:
				self.Project=safe_input('\nEnter Batch download directory (Project name): ')

			except LeachICancelError:
				death = True
				print("\n\u001b[33;1mCancellation command entered.\nExiting peacefully\u001b[0m")
				leach_logger("0x1||10009||User Exit-0")
				try:
					server_code.kill()
				except: pass

				

				exit(0)
				# sys_exit(0)
			if self.Project=='':
				print('You must enter a Project name here.')
			elif self.Project in ['?enable-dl-thread', '?E-dl-T']:
				sp_arg_flag['disable dl cancel'] = True
				print('Disabled download cancellation by adding join thread option')
				return 0

			elif self.Project in ['?disable-dl-thread', '?D-dl-T']:
				sp_arg_flag['disable dl cancel'] = False
				print('Enabled download cancellation by adding removing thread option [DEFAULT]')
				return 0
			elif self.Project in ['?disable-dl-get', '?D-dl']:
				sp_arg_flag['disable dl get'] = True
				print('Disabled download save by using requests.head')
				return 0

			elif self.Project in ['?enable-dl-get', '?E-dl'] :
				sp_arg_flag['disable dl get'] = False
				print('Enabled download save by using requests.get [DEFAULT]')
				return 0

			elif self.Project in ['?enable-ara-ara', '?E-noise'] :
				sp_arg_flag['ara_ara'] = True
				print('Enabled fun sounds [DEFAULT]')
				return 0

			elif self.Project in ['?disable-ara-ara', '?D-noise'] :
				sp_arg_flag['ara_ara'] = False
				print('Enabled fun sounds [DEFAULT]')

			else:
				self.Project= self.Project
				break

		temp = self.Project
		temp1= temp.replace('"','')
		if temp1[0]=="'" and temp1[1]=="'": temp[1:-1]
		try:
			from_file= True
			if temp1.endswith('.proj') and os_isfile(temp1):
				if asker("Project file detected.\n\u29bf Do you want re-open project from that file?\n >> "):
					leach_logger("10009x0||%s||fileOpen"%(self.Project),user_name)
					if self.data_checkup(path = temp1, proj_name= temp)==0:
						return 0
				else: from_file = False
			else: from_file= False

			if from_file == False:
				if any([i in self.Project for i in '/\<>?"*|:']):
					print('Project name can\'t have these charecters : /\<>?"*|:\n\n')
					return 0
					
				# self.project_dir=self.Project[:].replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')
				leach_logger("10009x0||%s||Checking Project Database"%(self.Project),user_name)
				if self.Project in open('data/projects.db').read().split('\n'):
					print('Existing Project name found!')
					proj_good=False
					list_good=False
					if self.data_checkup()==0:
						return 0
			del from_file
		except LeachICancelError:
			print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
			leach_logger("000||10009||%s||f-Stop||is_proj_file||user probably freaked out for too much Ques"%self.Project)
			return 0

		

		del temp, temp1

		if any(i in self.Project for i in '\\/|:*"><?'):
			print("\n>> Project name can't have ")
			print("\\ / | : * \" > < ?\n".center(20))
			return 0

		leach_logger("50001x1||%s"%(Project),user_name)
		if Project in open('data/projects.db').read().split('\n'):
			global main_link, link_startswith, file_types, sub_dirs, sp_flags, sp_extension, overwrite_bool, dimention, dl_done, sequence
			print('Existing Project name found!')
			proj_good=False
			list_good=False

			if os_exists('Data/leach_projects/'+Project+'.proj') and os_exists('Data/leach_projects/'+Project+'.list'):
				proj_good= True
				sequence= None
				dl_done=False
				sp_flags=[]
				try:
					with open('Data/leach_projects/'+Project+'.proj', 'rb') as f:
						print('db found')
						_proj= f.read()
					existing_data=_proj.decode().strip().split('\n')
					try:
						dl_done=False
						exec(_proj, globals())

						proj_good= True
					except Exception as e:
						raise LeachKnownError
				except LeachKnownError:
					#print(existing_data)
					try:
						main_link=existing_data[0]
					except:
						corruptions+=[1]
						print('\033[1;31;40mCorrupted Data! Error code: 601x1\033[0m')
						proj_good=False

					if proj_good:
						try:
							link_startswith=existing_data[1]
						except:
							proj_good= False
							print('\033[1;31;40mCorrupted Data! Error code: 601x2\033[0m')
							corruptions+=[4]

					if proj_good:
						try:
							file_types=eval(existing_data[2])
						except Exception as e:
							proj_good= False
							print('\033[1;31;40mCorrupted Data! Error code: 601x3\033[0m')
							corruptions+=[4]
							raise e

					if proj_good:
						try:
							file_starts=existing_data[3]
						except:
							proj_good= False
							print('\033[1;31;40mCorrupted Data! Error code: 601x4\033[0m')
							corruptions+=[4]

					if proj_good:
						try:
							sub_dirs=eval(existing_data[4]) #sub directory list
						except:
							proj_good= False
							print('\033[1;31;40mCorrupted Data! Error code: 601x5\033[0m')
							corruptions+=[2]
						try:  #added in v5.0 may not be in older files
							sp_flags=eval(existing_data[5])
							sp_extension=eval(existing_data[6])
							overwrite_bool=eval(existing_data[7])
						except IndexError: pass
					if proj_good:
						try:  #added in v5.1 may not be in older files
							dl_done=eval(existing_data[8])
						except IndexError:
							pass


				if proj_good:
					with open('Data/leach_projects/'+Project+'.list') as f:
						try:
							file=f.read()

							if file.strip()=='': raise ValueError
							all_list= eval(str(file))
							print('list found')
							list_good= True
						except:
							list_good= False
							print('\033[1;31;40mCorrupted Data! Error code: 601x6\033[0m')
							corruptions+=[3]

					#print(x)
				if proj_good and list_good:
					if 'mangafreak' in sp_flags:
						if dl_done:
							if not os_exists('Download_projects/'+Project+'/'): 
								print("\n  \u001b[1m\u001b[4m\u001b[7mProject folder not found.\033[0m\nPlease recheck or update the donwload project\n*its required for Manga Freak Projects")
								return 0
							sub_dirs = natsort.natsorted([get_file_name(i[0], 'url').split('.')[0] for i in all_list])
							all_list =[]
							for i in range(len(sub_dirs)):
								try:
									for j in os_listdir('Download_projects/'+Project+'/'+sub_dirs[i]):
										#print(j)
										if os_isfile('Download_projects/'+Project+'/'+sub_dirs[i]+'/'+j) and not j.endswith('.html'):
											all_list.append([j,i])
								except OSError: continue
							first_page=make_pages(all_list,sub_dirs, Project, True)
						
							print("Local webpage created")
							if asker("Wanna check the page??\n leave a enter to pass", default=False):
								run_in_local_server(port, host_dir='Download_projects/%s/%s.html'%(Project, Project))


						else:
							print("can't generate web pages offline from incomplete manga freak download")
					else:
						exec(open('make_html.py').read(), globals())
						first_page=make_pages(all_list,sub_dirs, Project, True)

					
						print("Local webpage created")
					
						if asker("Wanna check the page??\n leave a enter to pass\n>> ", default=False):
							run_in_local_server(port, host_dir='Download_projects/%s/%s.html'%(Project, Project))

				else:
					print('Sorry, it seems the project data was Corrupted!\nRetry when online...')


					
if __name__=='__main__':
	x=offline_leach()
	while True:
		
		x.main()
