import pkg_resources
import sys
import subprocess
from platform import system as os_name
from os import system


installed_pkgs = sorted([m.key for m in pkg_resources.working_set])
#print(installed_pkgs)


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def clean():
        if os_name() == 'Windows':
                _ = system('cls')
        else:
                _ = system('clear')


def download(url,fn,n):
        print('GETTING CHAPTER: ',str(n))
#       print(url)
        resp = requests.get(url)

        with open(fn+'_'+str(n)+'.zip','wb') as f:
                print('FILE CREATED')
                f.write(resp.content)




def analyze(c):
        a = c.split('conn ')
        a1 = a[len(a)-1]
        print(a1)
        a2 = a1.split(' ')
        print(a1)

        for s in a2:
                s.capitalize()

        manga_name = '_'.join(a2)

        return manga_name

def ex_cm_dw(c,mn):
        try:
                if ' ' in c:
                        b = c.split(' ')
                        b1 = b[1]
                        if '-' in b1:
                                b2 = b1.split('-')
                                start = int(b2[0])
                                end = int(b2[1])+1
                                fn = input('enter a name for using on zip file: ')
                                for n in range(start,end):
                                        url = "http://images.mangafreak.net:8080/downloads/{0}_{1}".format(mn,str(n))
                                        download(url,fn,n)

        except:
                raise

def run(i):
        if 'conn' in i:
                m_n = analyze(i)
                while True:
                        comand = input(m_n+'$ ')
                        if comand == 'xit':
                                break
                        elif 'download'in comand:
                                ex_cm_dw(comand,m_n)








print('[mangaScrapy _v1.0 running]')
if 'requests' in installed_pkgs:
        print('REQUIREMENTS ALREADY SATISFIED')
else:
        print('SOME MODULES ARE MISSING')
        choice = input('Do you want to install the missing modules?(Y/N): ')
        if choice == 'Y':
                install('requests')
                clean()
                print('REQUIREMENTS ARE SATISFIED')
        else:
                print('This software can not be operated with the current console')

import requests


s = requests.Session()
while True:
        i = input('» ')
        if i == 'x':
                break
        #run(i)
        

        s.get(i)
        r = s.get(i)

        print(r.content)

        # print(requests.get(i, allow_redirects=True).content)
        # response = requests.get(i)
        # if response.history:
        #         print("Request was redirected")
        #         for resp in response.history:
        #                 print(resp.status_code, resp.url)
        #         print("Final destination:")
        #         print(response.status_code, response.url)
        # else:
        #         print("Request was not redirected")

