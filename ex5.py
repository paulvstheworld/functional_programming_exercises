bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]


def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d


def call(fn, key):
    def apply_fn(record):            
        return assoc(record, key, fn(record.get(key)))
    return apply_fn


def pluck_reduce(keys):
    def apply_fn(record):
        return reduce(lambda a, x: assoc(a, x, record[x]),
               keys,
               {})
    return apply_fn


def pluck_recursive(keys):
    def get_dict_with_keys(new_dict, _d, keys):
        if not keys:
            return new_dict
    
        if keys[0] in _d:
            new_dict[keys[0]] = _d[keys[0]]
    
        return get_dict_with_keys(new_dict, _d, keys[1:])


    def apply_fn(record):
        return get_dict_with_keys({}, record, keys)
    return apply_fn


def pluck_dict_comprehension(keys):
    def apply_fn(record):
        return { x:y for x,y in record.iteritems() if x in keys}
    return apply_fn
 
 
def pipeline_each(data, fns):
    return reduce(lambda a, fn: map(fn, a),
                  fns,
                  data)


print pipeline_each(bands, [call(lambda x: 'Canada', 'country'),
                            call(lambda x: x.replace('.', ''), 'name'),
                            call(str.title, 'name'),
                            pluck_reduce(['name', 'country'])])



                            
# Implement pluck so that the pipeline_each call
# above returns the bands below.
 
# => [{'name': 'Sunset Rubdown', 'country': 'Canada'},
#     {'name': 'Women', 'country': 'Canada' },
#     {'name': 'A Silver Mt Zion', 'country': 'Canada'}]
    
