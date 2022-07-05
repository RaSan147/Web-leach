import os
path = "."
count = 0
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename.endswith('.py'): 
            for i in open(os.path.join(dirpath, filename)).readlines():
            	if i.strip()!="":
            		count +=1
            		
            		
            		
print(count)
            
