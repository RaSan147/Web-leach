# find non unicode characters in files

with open("./main_ez.py", 'rb') as f:
    data = f.read()

    for i in range(len(data)):
        if data[i] >= 0x80:
            print(i, data[i])
            print(data[i:i+50])
            break
        if i == len(data) - 1:
            print("No non-unicode characters found.")
            break
