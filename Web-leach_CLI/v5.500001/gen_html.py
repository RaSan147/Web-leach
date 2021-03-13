from leach5_500001_class import *

run_server(port)
def main():
	while True:
		try:
			Project=safe_input('\nEnter Batch download directory (Project name): ')
		except LeachICancelError:
			print("\n\u001b[33;1mCancellation command entered.\nExiting peacefully\u001b[0m")
			try:
				server_code.kill()
				print('Server closed...')
			except: pass
			leach_logger("0x1||5000||User Exit-0")
			exit(0)
		if Project=='':
			print('You must enter a Project name here.')
		else:
			corruptions=[]
			break

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
						sub_dirs = natsort.realsorted([get_file_name(i[0], 'url').split('.')[0] for i in all_list])
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


					


while True:
	main()
