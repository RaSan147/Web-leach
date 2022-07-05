from config import  config

config = config

def push(config_):
	global config
	config = config_
	print(config.x)
	config.x = 2
def get():
	print(config.x)