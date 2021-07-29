from timeit import timeit
from requests_html import HTMLSession as HTMLSession_
from requests import Session

# test with cprofile
print(timeit("""
	
# create an HTML Session object
session = Session()
 
# Use the object above to connect to needed webpage
resp = session.get("https://www.google.com/")
 
# Run JavaScript code on webpage
# resp.html.render()""", number= 100, globals= globals()))