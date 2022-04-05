import json

x = json.load(open("cloud data type.json"))

print(x)

def del_global_var(x):
    a=globals()
    if x in a:
        del a[x]

def get_var(x):
    xx = x.split(".")
    to_return = None

    a=globals()
    if x in a:
        if len(xx) == 1:
            return a[x]

        else:
            to_return = a[x]
            for i in range(len(xx)-1):
                

    

del_global_var('x["append"]')

print(x)