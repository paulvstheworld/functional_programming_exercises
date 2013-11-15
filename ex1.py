# Unfunctional version:
 
names = ['Mary', 'Isla', 'Sam']

names = map(lambda x: hash(x), names)
print names

'''
for i in range(len(names)):
    names[i] = hash(names[i])
 
print names # => [6306819796133686941, 8135353348168144921, -1228887169324443034]
'''
 
# Rewrite the code above as a map
 
# Expected answer: [6306819796133686941, 8135353348168144921, -1228887169324443034]


def my_map(func, l):
    return [func(item) for item in l]

print my_map(lambda x: hash(x), names)


