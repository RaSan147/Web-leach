# pylint: disable=anomalous-backslash-in-string

# for testing
Project = main_link = link_startswith = file_types = file_starts = sub_dirs = sp_flags= sp_extension = overwrite_bool = dimention = dl_done = sequence = sub_links = has_missing = dir_sorted = 0

class Constants:
	"""Stores most commonly used constants
	"""

	# file types
	img = ('jpeg', 'jpg', 'png', 'gif', 'webp', 'bmp', 'tif')

	# DLC links
	who_r_u = 'https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
	yamatte = ('https://www.myinstants.com/media/sounds/yamatte.mp3', 'https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3')

	# conversation words
	yes = ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yep', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yep', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yep')
	no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
	cond = yes + no
	condERR = "/y/Sorry,  I can't understand what you are saying./=/\n Just type yes or no.   "
	hard_cancel = '/y/Hand Cancel Command entered.\nExiting.../=/'

	special_starts = {'nh':'https://nhentai\.((net)|(to)|(xxx))/g/',
		'mangafreak':'https://w[^\/]+\.mangafreak.net/(?:M|m)anga/([^\?\#]+)',
		'nh_sc':'^nh (\d+)$',
		'mf_sc':'^mf (.+)$',
		'pinterest':'https://www.pinterest.com/',
		'mf_read':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(?:_\d+)[\?\#]?.*',
		'mf_read_chap':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(_\d+)[\?\#]?.*',
		'webtoon_ep':'https\:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/.*?\/viewer\?title_no\=(\d+)\&episode_no\=\d+',
		'webtoon': 'https:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/list\?title_no=(\d+)'}



true = True
false = False
none = None


def leach_logger(*args):
	pass
