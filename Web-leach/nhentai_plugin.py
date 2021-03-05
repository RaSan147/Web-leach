#from __future__ import print_function
import requests
from bs4 import BeautifulSoup as bs
from re import compile as compiler
parser='html.parser'


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
re_link='https://nhentai.((to)|(net))/g/\d*/'
link='https://nhentai.to/g/121212/'
# page = requests.get(link,headers=headers)
# soup=bs(page.content, parser)
# title=soup.find("h1").getText()
all_list=set([])
def list_writer(link, web_starts, types, file_link_starts,n):
	global all_list

					
	page = requests.get(link,headers=headers)
	soup=bs(page.content, parser)
	# print(page.content)
	# time.sleep(10000)
	# li=[]
	searcher=compiler('^'+file_starts)
	for imgs in soup.find_all('img'):
		http=imgs.get('src')
		if http== None:
			http=imgs.get('data-src')
		if searcher.search(str(http))!=None and http.endswith(types):
			if http.startswith('//i') and '.imggur.net' in http:
				http="https:"+http
			all_list.add((http,n))


def nhantai_link(link):
	page = requests.get(link,headers=headers)
	if page:
		soup=bs(page.content, parser)
		title=soup.find("h1").getText()
		print("Indexing from",title)

#nhantai_link('https://nhentai.to/g/121212/')
# print(title)
#g/26346/15/

# print(eval('[fg,5,"gg'))

# for i in range(1000):
# 	print("sorry ",end='')


from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume, IAudioEndpointVolumeCallback


def main():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        #if session.Process and session.Process.name() == "Discord.exe":
        print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())


if __name__ == "__main__":
    main()
