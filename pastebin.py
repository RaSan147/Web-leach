# from builtins import print
import requests # see https://2.python-requests.org/en/master/
 
key = "f7e117d452fed3df6e5cc1ea2eee658a"
text = "a text"
t_title = "a_paste_title"
 
login_data = {
    'api_dev_key': key,
    'api_user_name': "DarKnighTitan",
    'api_user_password': "147852369aA.."
    }
data = {
    'api_option': 'paste',
    'api_dev_key':key,
    'api_paste_code':text,
    'api_paste_name':t_title,
    'api_paste_expire_date': 'N',
    'api_user_key': None,
    'api_paste_format': ''
    }
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
login = requests.post("https://pastebin.com/api/api_login.php", data=login_data, headers=headers)
status= login.status_code
#print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")
#print("User token: ", login.text)
data['api_user_key'] = login.text
 
 
def send_paste(data, title):
	data['api_paste_code']=data
	data['api_paste_name']=title
	r = requests.post("https://pastebin.com/api/api_post.php", data=data, headers=headers)
	#print("Paste send: ", r.status_code if r.status_code != 200 else "OK/200")
	#print("Paste URL: ", r.text)
	return r.text