dir_path = os_dirname(os_realpath(__file__))

def make_cbz(all_li, dir_list, project, seq, ext=''):
	first_page=None
	dir_len = len(dir_list)

	dir_list= natsort.natsorted(dir_list)
	first_page = dir_path+'/Download_projects/'+ project+'/'+project+'.html'
	has_non_cbz = False
	missing_files = False
	cbz_ext = []
	xprint('/y/Creating CBZ files\nPlease wait.../=/\n  [ 0 / %i ] done...'%dir_len)
	for i in range(dir_len):
		temp=[]

		for j in range(len(all_li)):
			if all_li[j][1] == i:
				file_name = get_file_name(all_li[j][0]
										).replace('/','-').replace('\\','-'
										).replace('|','-').replace(':','-'
										).replace('*','-').replace('"',"'"
										).replace('>','-').replace('<','-'
										).replace('?','-')+ext
				if get_file_ext(file_name) not in cbz_ext:
					if has_non_cbz is False:
						has_non_cbz = True
						print('Ignoring CBZ unsupported files')
				else:
					temp.append(html_unescape(get_file_name(all_li[j][0])).replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-'))

		temp=remove_duplicate(temp)

		if seq:
			temp= natsort.natsorted(temp)

		outpath= 'Download_projects/[CBZ]'+ project+'/'+dir_list[i]+'.cbz'
		
		with zipfile.ZipFile(outpath, 'w') as zip:
			for index, image in enumerate(temp):
				file = reader('Download_projects/'+ project+'/'+dir_list[i]+'/'+image, 'rb', on_error= None)
				if file==None:
					if missing_files==False:
						xprint('\r\Some files are missing\n/y/Ignoring. Please try Updating the project to get the missing files.')
				zip.writestr("%i.%s" % (index, get_file_ext(temp)), file)
		delete_last_line()
		print('  [ %i / %i ] done'%(i, dir_len))
	return first_page


