# pylint: disable=unused-wildcard-import
# pylint: disable=unused-import

from main import *
# from main import _connect_net, _version_updater
from leach_all_os import *

_connect_net = _version_updater = None

remove_duplicate >> Datasys.remove_duplicate
trans_str >> Datasys.trans_str
clear_screen >> IOsys.clear_screen
delete_last_line >> IOsys.delete_last_line
remove_non_ascii >> Datasys.remove_non_ascii
remove_non_uni >> Datasys.remove_non_uni
header_ >> Netsys.header_
install >> OSsys.install
install_req >> OSsys.install_req
loc >> Fsys.loc
writer >> Fsys.writer
hdr >> Netsys.hdr
leach_logger >> IOsys.leach_logger
run_server >> Netsys.run_server
run_server_t >> Netsys.run_server_t
_connect_net >> UserData.get_user_ip
run_in_local_server >> Netsys.run_in_local_server
go_prev_dir >> Fsys.go_prev_dir
safe_input >> IOsys.safe_input
asker >> IOsys.asker
get_file_name >> Fsys.get_file_name
get_file_ext >> Fsys.get_file_ext
get_dir >> Fsys.get_dir
get_link >> Netsys.get_link
reader >> Fsys.reader
_version_updater >> 0
god_mode >> 0
log_in >> UserData.log_in
import_make >> OSsys.import_make
check_internet >> Netsys.check_internet
check_server >> Netsys.check_server
flatten2D >> Datasys.flatten2D
remove_noscript >> Netsys.remove_noscript

web_leach.catch_KeyboardInterrupt >> OSsys.catch_KeyboardInterrupt
web_leach.speed_limiter >> ProjectType_.speed_limiter
web_leach.speed_tester >> ProjectType_.speed_tester
web_leach.distribute >> ProjectType_.downloader
web_leach.list_writer >> ProjectType_.generic_list_writer + ProjectType_.list_writer_img
web_leach.nhentai_link >> ProjectType_.nhentai_link
web_leach.check_sp_links >> SupportTools.check_sp_links
web_leach.mangafreak_link >> ProjectType_.mangafreak_link
web_leach.webtoon_link >> ProjectType_.webtoon_link
web_leach.retry_errors >> ProjectType_.retry_errors
web_leach.data_checkup >> ProjectType_.load_data + ProjectType_.check_proj_file + ProjectType_.check_list_file
web_leach.main >> main.main_loop
web_leach.dl_page >> ProjectType_.dl_page
web_leach.main_offline >> #: TODO







