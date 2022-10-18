import os, zipfile
from print_text3 import oneLine
import glob

import warnings
warnings.filterwarnings("ignore")

total = 0
oneline = oneLine()
#oneline.new()

if os.path.isfile("new.zip"):
	os.remove("new.zip")
with zipfile.ZipFile("new.zip",mode="w") as z:
	for filepath in glob.iglob('**/*.jpg', recursive=True):
		#print(filepath)
		"""with open(filepath, "rb") as f:
			data = f.read(1024*8)
			while data:
				total+=len(data)
				oneline._update(total, end="")
				z.writestr(filepath, data)
				data = f.read(1024*8)"""
		try:
			z.write(filepath)
		except:
			print(filepath)
			print("\n\n")
		total += os.stat(filepath).st_size
		oneline._update(total)
				
	


