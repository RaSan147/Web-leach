requirements_all= ('requests',  'beautifulsoup4', 'natsort', 'google')
requirements_win= ('pypiwin32', 'comtypes', 'psutil', 'lxml', 'pywin32-ctypes')
_VERSION="5.50004"



true= True
false= False



img=('jpeg','jpg','png','gif', 'webp', 'bmp', 'tif')


who_r_u='https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
yamatte= ('https://www.myinstants.com/media/sounds/yamatte.mp3','https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3')
yes= ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yep', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yep', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yep')
no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
cond=yes+no
condERR = "/y/Sorry,  I can't understand what you are saying./=/\n Just type yes or no.   "
hard_cancel = '/y/Hand Cancel Command entered.\nExiting.../=/'


__update__G = 'pass'
__update__L = 'pass'
user_list=['bec6113e5eca1d00da8af7027a2b1b070d85b5ea','eb23efbb267893b699389ae74854547979d265bd']

has_all_libs = True
g_mode=False
ara_ara= True #to control parody noise
no_log = False #to stop logging
death = False
dying= False

proxy_port = 0

death_talk = 0

sp_arg_flag={'disable dl cancel' : False,
			'disable dl get' : False,
			'ara ara': False if ara_ara==None else ara_ara,
			'no log': False if no_log==None else no_log,
			'no browser': False,
			'max dlim': 0, # in kbps
			'chunk_size': 8192, # in Bytes
		}

ara_ara= False #to control parody noise

server_status = 'undefined'