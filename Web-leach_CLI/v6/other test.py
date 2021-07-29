from requests_html import HTMLSession
 
# create an HTML Session object
session = HTMLSession()
 
# Use the object above to connect to needed webpage
resp = session.get("https://www.webtoons.com/en/fantasy/the-princesss-jewels/list?title_no=2966&page=1")
 
# Run JavaScript code on webpage
# resp.html.render()

with open("test.html", "w") as f:
	f.write(resp.html.html)