import requests, json

# from main import *


def post_online(url, data,file):
	try:
		r = requests.post(url, data=data, files=file)
		return r.text
	except Exception as e:
		pass

# leach_logger('fuck')