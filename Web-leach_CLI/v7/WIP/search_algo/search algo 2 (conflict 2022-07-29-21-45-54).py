import json, re
from unidecode import  unidecode as uni
from collections import Counter

times = 1 # to make the array larger for future addutions
data = json.load(open("names with alt names.json"))*times

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
		pos_list = [9999 for _ in range(l)]
		for i in range(l):
			got = 0
			for r in kwr:
				for x in data[i]:
					result = r.search(x)
					if result:
						pos = result.span()[0]
						pos_list[i] = min(pos_list[i], pos)
						found[i] += 1


		return found, pos_list

	def _search_small(self, found, small):
		for key in found.keys():
			dd = data[key]
			for j in small:
				if any(j in d for d in dd):
					found[key] += 1

		return found

	def sort_by_position(self, found, pos_list):
		def get_pos(item):
			print(pos_list[item])
			return pos_list[item]
		item_bkp = []
		print(json.dumps(found, indent=2))
		for times, items in found.items():
			item_bkp = items[:]
			item_bkp.sort(key=get_pos, reverse=True)

			found[times] = item_bkp[:]

		print(json.dumps(found, indent=2))
		return found



	def search(self, kw):


		kwr, small = self.make_regex(kw)


		found, pos_list = self._search_regex(kwr)
		found = self._search_small(found, small)


		to_sort = {}
		for value in found.values():
			to_sort[value] = []
		box = []
		# for key, value in found.items():
		# 	print(data[key], value)
		for i, times in found.most_common():
			to_sort[times].append(i)

		final = self.sort_by_position(to_sort, pos_list)
			
		keys = sorted(list(final.keys()), reverse=True)
		for key in keys:
			items = final[key]
			print(items)
			for item in items:
				# print(data[item])
				box.append(item)

		return box




		#print(re.search(kw, "fuck her"))

if __name__ == "__main__":
	s = Search_Algo()
	import time, timeit

	query = "(akame ga k-ill"
	query = ".hack xxx"
	# query = "sword art kill"
	def out(txt):
		return s.search(txt)


	print("start, Query: ", query)

	def one():
		x = out(query)
		#print(x)
		for i in x:
			print(data[i], pos_list[i], )



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

	#import cProfile
	#cProfile.run('out(query)')

	# multi()
	start = time.time()
	one()
	print("\n TIME TAKEN: ", time.time() - start)

