from main import *


class ProjectType_(ProjectType_):
	def downloader(self, part, is_error=False, partitions=None):
		if partition is None:
			partition = self.dl_threads

		global err_hdr_list
		task_id = str(part+1)
		res = 0

		if self.existing_found:
			if os_exists(AboutApp.thread_data_dir + self.Project + '/t' + task_id + '.txt'):
				res = Fsys.reader(AboutApp.thread_data_dir + self.Project + '/t' + task_id + '.txt').strip()
				res = eval(res) if res!='' else 0# resume point of the list (index # int)
		self.done += res

		session = requests.session()

		if is_error:
			lists = range(self.errors)
		else:
			lists = range(0, self.total)[part::partitions]

		time.sleep(1.2) # to make sure other threads started safely and the restore points are calculated correctly

		for j in lists:

			error_name = False

			if self.break_all == True: return 0

			if lists.index(j)<res:
				continue
			download = True # switch for downloading the file
			streaming = not is_error # will not stream the file if it already caused an error

			if 'ignore_on_null_content' in self.sp_flags or 'stop_on_null_content' in self.sp_flags:
				streaming = False


			if is_error:
				i = self.error_links[j]
				timeout = 30

			else:
				i = self.all_list[j]
				timeout = 6

			fname = i[2]
			fdir = self.sub_dirs[i[1]]
			flink = i[0]

			self.is_error = is_error

			if self.sub_links!=[]: # if sub_links are available, then use them as header referer
				current_header = Netsys.header_(self.sub_links[i[1]])
			else:
				current_header = Netsys.header_()	# randomizes header from list on every download to at least try to fool server


			if self.overwrite_bool == False:
				if os_isfile(AboutApp.download_dir + self.Project + '/' + fdir + '/' + fname + self.sp_extension): download = False
			if download:

				if config.sp_arg_flag['disable dl get'] == True:
					try:
						file = session.head(flink, , headers= current_header, timeout = timeout)
					except NetErrors as e:
						__net_stat = Netsys.check_network_available()
						if __net_stat==False:
							self.break_all = True
							AboutApp.

					else:

						

