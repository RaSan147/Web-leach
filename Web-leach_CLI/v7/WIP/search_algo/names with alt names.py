import bs4, requests, json

x = requests.get("https://en.m.wikipedia.org/wiki/List_of_manga_licensed_in_English").text


s = bs4.BeautifulSoup(x, features="lxml")

m = []
for i in s.findAll("td"):
	if not i.find("span"): continue
	mm = []
	for j in i.findAll("a"):
		mm.append(j.text.lower())
		
	for j in i.findAll("span"):
		if j.has_attr("lang"):
			mm.append(j.text.lower())
			
	for j in i.findAll("i"):
		if j.has_attr("lang"):
			mm.append(j.text.lower())
	m.append(mm)
			
names = json.dumps(m, indent=2)

with open("names with alt names.json", "w") as f:
	f.write(names)