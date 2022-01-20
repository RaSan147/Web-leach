import requests
import json

x = requests.post("https://freeimage.host/api/1/upload",
                  data={"key": "6d207e02198a847aa98d0a2a901485a5"},
                  files={"source": open("8.jpg", "rb")})
print(x.text)
print(x.__dict__)
for key in x.__dict__.keys():
    print(key, ' : ', x.__dict__[key])

# convert json to dict
x = json.loads(x.text)
print(x)
for key in x.keys():
    print(key, ' : ', x[key])


"""{"status_code":200,"success":{"message":"image uploaded","code":200},"image":{"name":"8","extension":"jpg","width":"1280","height":"1814","size":821217,"time":"1642658830","expiration":"0","adult":"0","status":"0","cloud":"0","vision":"0","likes":"0","description":null,"original_exifdata":null,"original_filename":"8.jpg","views_html":"0","views_hotlink":"0","access_html":"0","access_hotlink":"0","file":{"resource":{"chain":{"image":"https:\/\/iili.io\/ld551n.jpg","thumb":"https:\/\/iili.io\/ld551n.th.jpg","medium":"https:\/\/iili.io\/ld551n.md.jpg"},"chain_code":{"image":"ld551n","thumb":"ld551n","medium":"ld551n"}}},"is_animated":0,"nsfw":0,"id_encoded":"ld551n","ratio":0.7056229327453142,"size_formatted":"821.2 KB","filename":"ld551n.jpg","url":"https:\/\/iili.io\/ld551n.jpg","url_short":"https:\/\/freeimage.host\/","url_seo":"https:\/\/freeimage.host\/i\/8.ld551n","url_viewer":"https:\/\/freeimage.host\/i\/ld551n","url_viewer_preview":"https:\/\/freeimage.host\/i\/ld551n","url_viewer_thumb":"https:\/\/freeimage.host\/i\/ld551n","image":{"filename":"ld551n.jpg","name":"ld551n","mime":"image\/jpeg","extension":"jpg","url":"https:\/\/iili.io\/ld551n.jpg","size":821217},"thumb":{"filename":"ld551n.th.jpg","name":"ld551n.th","mime":"image\/jpeg","extension":"jpg","url":"https:\/\/iili.io\/ld551n.th.jpg"},"medium":{"filename":"ld551n.md.jpg","name":"ld551n.md","mime":"image\/jpeg","extension":"jpg","url":"https:\/\/iili.io\/ld551n.md.jpg"},"display_url":"https:\/\/iili.io\/ld551n.md.jpg","display_width":"1280","display_height":"1814","views_label":"views","likes_label":"likes","how_long_ago":"moments ago","date_fixed_peer":"2022-01-20 06:07:10","title":"8","title_truncated":"8","title_truncated_html":"8","is_use_loader":false},"status_txt":"OK"}
{'_content': b'{"status_code":200,"success":{"message":"image uploaded","code":200},"image":{"name":"8","extension":"jpg","width":"1280","height":"1814","size":821217,"time":"1642658830","expiration":"0","adult":"0","status":"0","cloud":"0","vision":"0","likes":"0","description":null,"original_exifdata":null,"original_filename":"8.jpg","views_html":"0","views_hotlink":"0","access_html":"0","access_hotlink":"0","file":{"resource":{"chain":{"image":"https:\\/\\/iili.io\\/ld551n.jpg","thumb":"https:\\/\\/iili.io\\/ld551n.th.jpg","medium":"https:\\/\\/iili.io\\/ld551n.md.jpg"},"chain_code":{"image":"ld551n","thumb":"ld551n","medium":"ld551n"}}},"is_animated":0,"nsfw":0,"id_encoded":"ld551n","ratio":0.7056229327453142,"size_formatted":"821.2 KB","filename":"ld551n.jpg","url":"https:\\/\\/iili.io\\/ld551n.jpg","url_short":"https:\\/\\/freeimage.host\\/","url_seo":"https:\\/\\/freeimage.host\\/i\\/8.ld551n","url_viewer":"https:\\/\\/freeimage.host\\/i\\/ld551n","url_viewer_preview":"https:\\/\\/freeimage.host\\/i\\/ld551n","url_viewer_thumb":"https:\\/\\/freeimage.host\\/i\\/ld551n","image":{"filename":"ld551n.jpg","name":"ld551n","mime":"image\\/jpeg","extension":"jpg","url":"https:\\/\\/iili.io\\/ld551n.jpg","size":821217},"thumb":{"filename":"ld551n.th.jpg","name":"ld551n.th","mime":"image\\/jpeg","extension":"jpg","url":"https:\\/\\/iili.io\\/ld551n.th.jpg"},"medium":{"filename":"ld551n.md.jpg","name":"ld551n.md","mime":"image\\/jpeg","extension":"jpg","url":"https:\\/\\/iili.io\\/ld551n.md.jpg"},"display_url":"https:\\/\\/iili.io\\/ld551n.md.jpg","display_width":"1280","display_height":"1814","views_label":"views","likes_label":"likes","how_long_ago":"moments ago","date_fixed_peer":"2022-01-20 06:07:10","title":"8","title_truncated":"8","title_truncated_html":"8","is_use_loader":false},"status_txt":"OK"}', '_content_consumed': True, '_next': None, 'status_code': 200, 'headers': {'Server': 'nginx', 'Date': 'Thu, 20 Jan 2022 06:07:10 GMT', 'Content-Type': 'application/json; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Set-Cookie': 'PHPSESSID=r4r0daj27patfa3i7me0eubnff; path=/', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Last-Modified': 'Thu, 20 Jan 2022 06:07:10GMT', 'Cache-Control': 'no-cache, must-revalidate', 'Pragma': 'no-cache', 'X-Frame-Options': 'DENY', 'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload', 'Content-Encoding': 'gzip'}, 'raw': <urllib3.response.HTTPResponse object at 0x0000018DA4D907F0>, 'url': 'https://freeimage.host/api/1/upload', 'encoding': 'UTF-8', 'history': [], 'reason': 'OK', 'cookies': <RequestsCookieJar[Cookie(version=0, name='PHPSESSID', value='r4r0daj27patfa3i7me0eubnff', port=None, port_specified=False, domain='freeimage.host', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False)]>, 'elapsed': datetime.timedelta(seconds=2, microseconds=876197), 'request': <PreparedRequest [POST]>, 'connection': <requests.adapters.HTTPAdapter object at 0x0000018DA4D78130>}  
_content  :  b'{"status_code":200,"success":{"message":"image uploaded","code":200},"image":{"name":"8","extension":"jpg","width":"1280","height":"1814","size":821217,"time":"1642658830","expiration":"0","adult":"0","status":"0","cloud":"0","vision":"0","likes":"0","description":null,"original_exifdata":null,"original_filename":"8.jpg","views_html":"0","views_hotlink":"0","access_html":"0","access_hotlink":"0","file":{"resource":{"chain":{"image":"https:\\/\\/iili.io\\/ld551n.jpg","thumb":"https:\\/\\/iili.io\\/ld551n.th.jpg","medium":"https:\\/\\/iili.io\\/ld551n.md.jpg"},"chain_code":{"image":"ld551n","thumb":"ld551n","medium":"ld551n"}}},"is_animated":0,"nsfw":0,"id_encoded":"ld551n","ratio":0.7056229327453142,"size_formatted":"821.2 KB","filename":"ld551n.jpg","url":"https:\\/\\/iili.io\\/ld551n.jpg","url_short":"https:\\/\\/freeimage.host\\/","url_seo":"https:\\/\\/freeimage.host\\/i\\/8.ld551n","url_viewer":"https:\\/\\/freeimage.host\\/i\\/ld551n","url_viewer_preview":"https:\\/\\/freeimage.host\\/i\\/ld551n","url_viewer_thumb":"https:\\/\\/freeimage.host\\/i\\/ld551n","image":{"filename":"ld551n.jpg","name":"ld551n","mime":"image\\/jpeg","extension":"jpg","url":"https:\\/\\/iili.io\\/ld551n.jpg","size":821217},"thumb":{"filename":"ld551n.th.jpg","name":"ld551n.th","mime":"image\\/jpeg","extension":"jpg","url":"https:\\/\\/iili.io\\/ld551n.th.jpg"},"medium":{"filename":"ld551n.md.jpg","name":"ld551n.md","mime":"image\\/jpeg","extension":"jpg","url":"https:\\/\\/iili.io\\/ld551n.md.jpg"},"display_url":"https:\\/\\/iili.io\\/ld551n.md.jpg","display_width":"1280","display_height":"1814","views_label":"views","likes_label":"likes","how_long_ago":"moments ago","date_fixed_peer":"2022-01-20 06:07:10","title":"8","title_truncated":"8","title_truncated_html":"8","is_use_loader":false},"status_txt":"OK"}'
_content_consumed  :  True
_next  :  None
status_code  :  200
headers  :  {'Server': 'nginx', 'Date': 'Thu, 20 Jan 2022 06:07:10 GMT', 'Content-Type': 'application/json; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Set-Cookie': 
'PHPSESSID=r4r0daj27patfa3i7me0eubnff; path=/', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Last-Modified': 'Thu, 20 Jan 2022 06:07:10GMT', 'Cache-Control': 'no-cache, must-revalidate', 'Pragma': 'no-cache', 'X-Frame-Options': 'DENY', 'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload', 'Content-Encoding': 'gzip'}
raw  :  <urllib3.response.HTTPResponse object at 0x0000018DA4D907F0>
url  :  https://freeimage.host/api/1/upload
encoding  :  UTF-8
history  :  []
reason  :  OK
cookies  :  <RequestsCookieJar[<Cookie PHPSESSID=r4r0daj27patfa3i7me0eubnff for freeimage.host/>]>
elapsed  :  0:00:02.876197
request  :  <PreparedRequest [POST]>
connection  :  <requests.adapters.HTTPAdapter object at 0x0000018DA4D78130>
{'status_code': 200, 'success': {'message': 'image uploaded', 'code': 200}, 'image': {'name': '8', 'extension': 'jpg', 'width': '1280', 'height': '1814', 'size': 821217, 'time': '1642658830', 'expiration': '0', 'adult': '0', 
'status': '0', 'cloud': '0', 'vision': '0', 'likes': '0', 'description': None, 'original_exifdata': None, 'original_filename': '8.jpg', 'views_html': '0', 'views_hotlink': '0', 'access_html': '0', 'access_hotlink': '0', 'file': {'resource': {'chain': {'image': 'https://iili.io/ld551n.jpg', 'thumb': 'https://iili.io/ld551n.th.jpg', 'medium': 'https://iili.io/ld551n.md.jpg'}, 'chain_code': {'image': 'ld551n', 'thumb': 'ld551n', 'medium': 'ld551n'}}}, 'is_animated': 0, 'nsfw': 0, 'id_encoded': 'ld551n', 'ratio': 0.7056229327453142, 'size_formatted': '821.2 KB', 'filename': 'ld551n.jpg', 'url': 'https://iili.io/ld551n.jpg', 'url_short': 'https://freeimage.host/', 'url_seo': 'https://freeimage.host/i/8.ld551n', 'url_viewer': 'https://freeimage.host/i/ld551n', 'url_viewer_preview': 'https://freeimage.host/i/ld551n', 'url_viewer_thumb': 'https://freeimage.host/i/ld551n', 'image': {'filename': 'ld551n.jpg', 'name': 'ld551n', 'mime': 'image/jpeg', 'extension': 'jpg', 'url': 'https://iili.io/ld551n.jpg', 'size': 821217}, 'thumb': {'filename': 'ld551n.th.jpg', 'name': 'ld551n.th', 'mime': 'image/jpeg', 'extension': 'jpg', 'url': 'https://iili.io/ld551n.th.jpg'}, 'medium': {'filename': 'ld551n.md.jpg', 'name': 'ld551n.md', 'mime': 'image/jpeg', 'extension': 'jpg', 'url': 'https://iili.io/ld551n.md.jpg'}, 'display_url': 'https://iili.io/ld551n.md.jpg', 'display_width': '1280', 'display_height': '1814', 'views_label': 'views', 'likes_label': 'likes', 'how_long_ago': 'moments ago', 'date_fixed_peer': '2022-01-20 06:07:10', 'title': '8', 'title_truncated': '8', 'title_truncated_html': '8', 'is_use_loader': False}, 'status_txt': 'OK'}
status_code  :  200
success  :  {'message': 'image uploaded', 'code': 200}
image  :  {'name': '8', 'extension': 'jpg', 'width': '1280', 'height': '1814', 'size': 821217, 'time': '1642658830', 'expiration': '0', 'adult': '0', 'status': '0', 'cloud': '0', 'vision': '0', 'likes': '0', 'description': None, 'original_exifdata': None, 'original_filename': '8.jpg', 'views_html': '0', 'views_hotlink': '0', 'access_html': '0', 'access_hotlink': '0', 'file': {'resource': {'chain': {'image': 'https://iili.io/ld551n.jpg', 'thumb': 
'https://iili.io/ld551n.th.jpg', 'medium': 'https://iili.io/ld551n.md.jpg'}, 'chain_code': {'image': 'ld551n', 'thumb': 'ld551n', 'medium': 'ld551n'}}}, 'is_animated': 0, 'nsfw': 0, 'id_encoded': 'ld551n', 'ratio': 0.7056229327453142, 'size_formatted': '821.2 KB', 'filename': 'ld551n.jpg', 'url': 'https://iili.io/ld551n.jpg', 'url_short': 'https://freeimage.host/', 'url_seo': 'https://freeimage.host/i/8.ld551n', 'url_viewer': 'https://freeimage.host/i/ld551n', 'url_viewer_preview': 'https://freeimage.host/i/ld551n', 'url_viewer_thumb': 'https://freeimage.host/i/ld551n', 'image': {'filename': 'ld551n.jpg', 'name': 'ld551n', 'mime': 'image/jpeg', 'extension': 'jpg', 'url': 'https://iili.io/ld551n.jpg', 'size': 821217}, 'thumb': {'filename': 'ld551n.th.jpg', 'name': 'ld551n.th', 'mime': 'image/jpeg', 'extension': 'jpg', 'url': 'https://iili.io/ld551n.th.jpg'}, 'medium': {'filename': 'ld551n.md.jpg', 'name': 'ld551n.md', 'mime': 'image/jpeg', 'extension': 'jpg', 'url': 'https://iili.io/ld551n.md.jpg'}, 'display_url': 'https://iili.io/ld551n.md.jpg', 'display_width': '1280', 'display_height': '1814', 'views_label': 'views', 'likes_label': 'likes', 'how_long_ago': 'moments ago', 'date_fixed_peer': '2022-01-20 06:07:10', 'title': '8', 'title_truncated': '8', 'title_truncated_html': '8', 'is_use_loader': False}
status_txt  :  OK"""

"""https://iili.io/RXLqMX.jpg

[url=https://freeimage.host/i/RX6VEb][img]https://iili.io/RX6VEb.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6MCu][img]https://iili.io/RX6MCu.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX61j9][img]https://iili.io/RX61j9.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6EQe][img]https://iili.io/RX6EQe.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6h3x][img]https://iili.io/RX6h3x.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6jYQ][img]https://iili.io/RX6jYQ.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6wvV][img]https://iili.io/RX6wvV.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6NyB][img]https://iili.io/RX6NyB.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6eTP][img]https://iili.io/RX6eTP.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6kj1][img]https://iili.io/RX6kj1.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6vZF][img]https://iili.io/RX6vZF.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6SCg][img]https://iili.io/RX6SCg.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6UGa][img]https://iili.io/RX6UGa.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6g6J][img]https://iili.io/RX6g6J.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX66aR][img]https://iili.io/RX66aR.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6Pvp][img]https://iili.io/RX6Pvp.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6iyN][img]https://iili.io/RX6iyN.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6Dnn][img]https://iili.io/RX6Dnn.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6bGs][img]https://iili.io/RX6bGs.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6ZZX][img]https://iili.io/RX6ZZX.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6m6G][img]https://iili.io/RX6m6G.md.jpg[/img][/url]
[url=https://freeimage.host/i/RX6yFf][img]https://iili.io/RX6yFf.md.jpg[/img][/url]
[url=https://freeimage.host/i/RXP9a4][img]https://iili.io/RXP9a4.md.jpg[/img][/url]
[url=https://freeimage.host/i/RXPH8l][img]https://iili.io/RXPH8l.md.jpg[/img][/url]
[url=https://freeimage.host/i/RXP2uS][img]https://iili.io/RXP2uS.md.jpg[/img][/url]
[url=https://freeimage.host/i/RXP3w7][img]https://iili.io/RXP3w7.md.jpg[/img][/url]
[url=https://freeimage.host/i/RXPFt9][img]https://iili.io/RXPFt9.md.jpg[/img][/url]
[url=https://freeimage.host/i/RXPqMu][img]https://iili.io/RXPqMu.md.jpg[/img][/url]
[url=https://freeimage.host/i/RXPnFj][img]https://iili.io/RXPnFj.md.jpg[/img][/url]
[url=https://freeimage.host/i/RXPfne][img]https://iili.io/RXPfne.png[/img][/url]"""
