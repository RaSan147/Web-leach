# from main import *
dir_path = os_dirname(os_realpath(__file__))
import zipfile

def make_cbz(all_li, dir_list, project, seq, ext='', dir_sorted = False):   #func_code= 50001
	first_page=None
	dir_len = len(dir_list)

	if not dir_sorted: dir_list= natsort.natsorted(dir_list)
	first_page = dir_path+'/Download_projects/'+ project+'/'+project+'.html'
	has_non_cbz = False
	missing_files = False
	cbz_ext = ('jpg', 'jpeg', 'png', 'gif')
	xprint('/y/Creating CBZ files\nPlease wait.../=/\n  [ 0 / %i ] done...'%dir_len)
	for i in range(dir_len):
		temp= all_li.all_names[i].copy()
		for j in range(len(temp)):
			if not temp[j].endswith(cbz_ext):
				temp[j] = None
				if has_non_cbz is False:
					has_non_cbz = True
					IOsys.delete_last_line()
					print('Ignoring CBZ unsupported files\n')
					leach_logger('50001xU||'+project)


		if seq:
			temp= natsort.natsorted(temp)

		
		outpath= 'Download_projects/[CBZ]'+ project+'/'+dir_list[i]+'.cbz'
		Fsys.writer(dir_list[i]+'.cbz', 'wb', b'', 'Download_projects/[CBZ]'+ project, '50001')
		
		with zipfile.ZipFile(outpath, 'w') as zip:
			for index, image in enumerate(temp):
				if image is None: continue
				file = Fsys.reader('Download_projects/'+ project+'/'+dir_list[i]+'/'+image, 'rb', on_missing= False, ignore_missing_log = True, f_code= '50001')
				if file==False:
					if missing_files==False:
						IOsys.delete_last_line()
						xprint('/r/Some files are missing\n/y/Ignoring. Please try Updating the project to get the missing files./=/\n')
						leach_logger('50001xM||'+project)
						missing_files= True
					continue
				zip.writestr("%i.%s" % (index, Fsys.get_file_ext(image)), file)
		IOsys.delete_last_line()
		print('  [ %i / %i ] done'%(i+1, dir_len))
	return first_page
