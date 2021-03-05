from itertools import permutations  
  
# Get all permutations of [1, 2, 3]

txt = input("Enter text: ")
perm = permutations(list(txt))  
print('\n\n\n')
# Print the obtained permutations
perm = list(dict.fromkeys(perm))
for i in list(perm):  
    print (''.join(i))
