import json, re
from unidecode import  unidecode as uni

data = json.load(open("names with alt names.json"))*1

print(len(data))

for i in range(len(data)):
	li = data[i]
	li_bkp = li[:]
	for x in li_bkp:
		dec = uni(x)
		if dec not in li:
			#li.append(dec)
			data[i].append(dec)
			#print(data[i], li)

#print(data)


class Search_Algo:
	def __init__(self):
		pass
		
	def search(self, kw):

		kws = kw.strip().split()
		kwr = []
		
		yy = r"""'|!|/|\\\"|\\-|\\\+|\\\?|\\\*"""
			#yyyy = "(" + re.escape(yy) +")+"
			
		yyy =  r"""('|!|/|\"|\-|\+|\?|\*)+"""
			#print(yy)
		yyr = re.compile(yy)

		del kw
		for kw in kws:
			
			if len(kw)<3: continue
			kw = kw.replace(".", ",")
			kw = re.escape(kw)
			
			kw = kw.replace(",", "(,|\\.)*")
			kw = [i for i in yyr.split(kw) if i!=""]
			
			kw = yyy.join(kw)
			#print(kw)
			if kw:
				kwr.append(re.compile(kw, flags=re.I))

		found = []
		for i in range(len(data)):
			got = 0
			for r in kwr:
				if any(r.search(x) for x in data[i]):
					got = 1
					found.append(i)
					break
			if got: continue
			
			
		return found
					
			
		
		
		#print(re.search(kw, "fuck her"))
		
		
s = Search_Algo()
import time, timeit

query = "akame ga kill"

def out(txt):
	x = s.search(txt)
	for i in x:
		print(data[i])


print("start, Query: ", query)

def one():
	out(query)
	exit()


def multi():
	timer = timeit.Timer(lambda: out(query))
	
	query = "akame ga kill"
	loop = 10
	res = timer.repeat(loop, 1)
	
	print("max", max(res))
	print("min", min(res))
	print("avg", sum(res)/10)
	print(res)


#for tt in range(10):
#	for i in s.search("gel dust"):
#		pass#print(data[i])

start = time.time()

one()
#multi()
print(time.time() - start)

print("" in "kddk")