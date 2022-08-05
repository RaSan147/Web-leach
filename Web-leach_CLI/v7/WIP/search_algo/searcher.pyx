import json, re
from unidecode import  unidecode as uni
from collections import Counter


cdef list data = json.load(open("names with alt names.json"))*1


cdef int data_l = len(data)
print(data_l)
print("total titles", sum(len(i) for i in data))


cdef list fix_data(list data=data):
	cdef int i
	cdef list li, li_bkp
	cdef str x, dec
	
	for i in range(data_l):
		li = data[i]
		li_bkp = li[:]
		for x in li_bkp:
			dec = uni(x)
			if dec not in li:
				#li.append(dec)
				data[i].append(dec)
				#print(data[i], li)
				
	return data

print("Fixing data")
data=fix_data()
print("done!")

cdef class Search_Algo:
	cdef str yy, yyy
	cdef object yyr

	def __init__(self):
				
		cdef str yy = r"""\\\(|\\\{|\\\[|\\\)|\\\}|\\\]|\'|!|/|\\\"|\\-|\\\+|\\\?|\\\*"""
			#yyyy = "(" + re.escape(yy) +")+"
		cdef str yyy
		yyy =  r"""(\(|\{|\[|\]|\}|\)|'|!|/|\"|\-|\+|\?|\*|\s)+"""
		
		yyy = r"""[\(\)\{\}\[\]\.\s'\"\+\-_\?\*/!]*"""
			#print(yy)
			
		self.yyy = yyy
		self.yyr = re.compile(yy)

		
		
	cdef list make_regex(self, str kw):
		
		
		cdef list kwr, small, kws, kw_
		cdef str i
		kws = kws.replace(".", ",")
		kws = kws.replace("_", ",")
		kws = kw.strip().split()
		kwr = []
		small = []
		for kw in kws:
			#print(kw)
			kw = kw
			kw = re.escape(kw)
			
			kw = kw.replace(",", "(?:,|\\.)*")
			kw_ = [i for i in self.yyr.split(kw) if i!=""]
			
			kw = self.yyy.join(kw_)
						
			if len(kw)<3: 
				small.append(kw)
				continue
			#print(kw)
	
			if kw:
				kwr.append(re.compile(kw, flags=re.I))
				
		return [kwr, small]
		
	cdef _search_regex(self, list kwr):
		cdef int i
		cdef str x
		
		found = Counter()
		
		for i in range(data_l):
			#got = 0
			for r in kwr:
				if any(r.search(x) for x in data[i]):
					
					#got = 1
					found[i] += 1
					#break
			#if got: continue
			
		return found
		
	cdef _search_small(self, found, list small):
		cdef str d, j
		cdef list dd
		for s in small:
			for i in found.keys():
				#print(i)
				dd = data[i]
				if any(s in d for d in dd):
					found[i] += 1
					#print(data[i])
		#print(found)
		return found
		
	cpdef list search(self, str kw):
		cdef list kwr, small
		

		kwr, small = self.make_regex(kw)
		
		
		found = self._search_regex(kwr)
		found = self._search_small(found, small)
		
			
		
		cdef list box = []
		
		for i in found.most_common():
			#print(i)
			box.append(i)
			
		return box
		

s = Search_Algo()
import time, timeit
	
query = "(akame ga k-ill"
query = ".hack xxx"
#query="トハックヨ"
query = "sword of the"

cpdef out(txt):
	return s.search(txt)
	


	
def one(query=query):
	x= out(query)
	#print(x)
	for i,j in x:
		print(data[i], j)
	
	
	
def multi(query=query):
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
	
def profile():
	import cProfile
	with cProfile.Profile() as pr:
		print(out(query))

	pr.print_stats()

def test(query = query):
	#profile()	
	multi(query)
	start = time.time()
	one(query)
	print(time.time() - start)
if __name__ == "__main__":	
	print("start, Query: ", query)
	

