people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
 
"""
height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1
 
if height_count > 0:
    average_height = height_total / height_count # => 120
"""
 


def my_len(my_list):
    return reduce(lambda a, x: a+1, my_list, 0)

def get_all_heights(people):
    return map(lambda x: x['height'], filter(lambda x: 'height' in x, people))


def get_average_height(people):
    heights = get_all_heights(people)
    return reduce(lambda a, x: x + a, heights) / my_len(heights)

print get_average_height(people)


# Rewrite the code above using map, reduce and filter
 
# Expected answer: 120





        
