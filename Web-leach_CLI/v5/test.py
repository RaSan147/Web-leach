import requests, time
int('ff')
x= time.time()
r= requests.head('http://images.mangafreak.net:8080/downloads/Nisekoi_228')

print(r.headers['content-length'], time.time()-x)