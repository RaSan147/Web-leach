import json, re
from unidecode import  unidecode as uni
from collections import Counter
data = json.load(open("names with alt names.json"))*10

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
				
		yy = r"""\\\(|\\\{|\\\[|\\\)|\\\}|\\\]|\'|!|/|\\\"|\\-|\\\+|\\\?|\\\*"""
			#yyyy = "(" + re.escape(yy) +")+"
			
		yyy =  r"""(\(|\{|\[|\]|\}|\)|'|!|/|\"|\-|\+|\?|\*|\s)+"""
		
		yyy = r"""[\(\)\{\}\[\]\.\s'\"\+\-_\?\*/!]*"""
			#print(yy)
			
		self.yyy = yyy
		self.yyr = re.compile(yy)

		
		
	def make_regex(self, kw):
		
		kws = kw.strip().split()
		kwr = []
		small = []
		for kw in kws:
			#print(kw)
			kw = kw.replace(".", ",")
			kw = re.escape(kw)
			
			kw = kw.replace(",", "(?:,|\\.)*")
			kw = [i for i in self.yyr.split(kw) if i!=""]
			
			kw = self.yyy.join(kw)
						
			if len(kw)<3: 
				small.append(kw)
				continue
			#print(kw)
	
			if kw:
				kwr.append(re.compile(kw, flags=re.I))
				
		return kwr, small
		
	def _search_regex(self, kwr):
		found = Counter()
		l = len(data)
		for i in range(l):
			got = 0
			for r in kwr:
				if any(r.search(x) for x in data[i]):
					#print(data[i])
					got = 1
					found[i] += 1
					break
			if got: continue
			
		return found
		
	def _search_small(self, found, small):
		for i in found.keys():
			 dd = data[i]
			 for j in small:
			 	if any(j in d for d in dd):
			 		found[i] += 1
			 		
		return found
		
	def search(self, kw):
		

		kwr, small = self.make_regex(kw)
		
		
		found = self._search_regex(kwr)
		found = self._search_small(found, small)
		
			
		
		box = []
		for i, _ in found.most_common():
			box.append(i)
			
		return box
					
			
		
		
		#print(re.search(kw, "fuck her"))
		
if __name__ == "__main__":	
	s = Search_Algo()
	import time, timeit
	
	query = "(akame ga k-ill"
	query = ".hack xxx"
	def out(txt):
		return s.search(txt)
	
	
	print("start, Query: ", query)
	
	def one():
		x = out(query)
		#print(x)
		for i in x:
			print(data[i])
	
	
	
	def multi():
		timer = timeit.Timer(lambda: out(query))
		
		#query = "(akame )ga kill"
		loop = 10
		res = timer.repeat(loop, 1)
		
		print("max", max(res))
		print("min", min(res))
		print("avg", sum(res)/10)
		print(res)
	
	
	#for tt in range(10):
	#	for i in s.search("gel dust"):
	#		pass#print(data[i])
	
	import cProfile
	cProfile.run('out(query)')
	
	multi()
	start = time.time()
	one()
	print(time.time() - start)

