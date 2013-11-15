bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]
 
def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d
 
def set_canada_as_country(band):
    return assoc(band, 'country', "Canada")
 
def strip_punctuation_from_name(band):
    return assoc(band, 'name', band['name'].replace('.', ''))
 
def capitalize_names(band):
    return assoc(band, 'name', band['name'].title())



def pipeline_each(bands, func_list):
    if not func_list or bands == None:
        return bands

    return pipeline_each(
        map(lambda x: func_list[0](x), bands),
        func_list[1:])


def rule_sequence(val, func_list):
    if not func_list or val == None:
        return val
    return rule_sequence(func_list[0](val), func_list[1:])


def pipeline_each_2(bands, func_list):
    return map(lambda x: rule_sequence(x, func_list), bands)


print pipeline_each(bands, [set_canada_as_country,
                            strip_punctuation_from_name,
                            capitalize_names])



                            
# Implement pipeline_each so that the pipeline_each call
# above returns:
 
# => [{'name': 'Sunset Rubdown', 'active': False, 'country':
# 'Canada'},
#     {'name': 'Women', 'active': False, 'country': 'Canada' },
#     {'name': 'A Silver Mt Zion', 'active': True, 'country':
# 'Canada'}]



