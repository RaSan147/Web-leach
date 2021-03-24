proj_name= input("Project name: ")

with open('data/leach_projects/%s.proj'%proj_name) as f:
    exec(f.read())
r=[]

with open('data/leach_projects/%s/errors.txt'%proj_name) as f:
    for i in f.readlines():
        i=i.strip()
        if i!='':
            r.append(eval(i))
# print(r)
r.sort(key=lambda m: sub_dirs[m[1]])
with open('data/leach_projects/%s/%s_error_report.txt'%(proj_name,proj_name), 'w') as a: a.write('')
with open('data/leach_projects/%s/%s_error_report.txt'%(proj_name,proj_name), 'a') as a:
    for m in r:
        a.write('%s -- %s\n'%(sub_dirs[m[1]], m[0]))
print('Report card done at "data/leach_projects/%s/%s_left_error_report.txt"'%(proj_name,proj_name))
r=[]
try:
    with open('data/leach_projects/%s/left_errors.txt'%proj_name) as f:
        for i in f.readlines():
            r.append(eval(i))
    # print(r)
    r.sort(key=lambda m: sub_dirs[m[1]])
    with open('data/leach_projects/%s/%s_left_error_report.txt'%(proj_name,proj_name), 'w') as a: a.write('')
    with open('data/leach_projects/%s/%s_left_error_report.txt'%(proj_name,proj_name), 'a') as a:
        for m in r:
            a.write('%s -- %s\n'%(sub_dirs[m[1]], m[0]))
    print('\nand\n"data/leach_projects/%s/%s_left_error_report.txt"'%(proj_name,proj_name))
except: pass

