def zero(s):
    if s[0] == "0":
        return s[1:]
 
def one(s):
    if s[0] == "1":
        return s[1:]
 
"""
def rule_sequence(s, rules):
    for rule in rules:
        s = rule(s)
        if s == None:
            break
 
    return s
"""


def rule_sequence(val, func_list):
    if not func_list or val == None:
        return val

    return rule_sequence(func_list[0](val), func_list[1:])
 

print rule_sequence('0101', [zero, one, zero])
# => 1
 
print rule_sequence('0101', [zero, zero])
# => None
 
# Reimplement rule_sequence as a recursive function.
# Make sure that when it is run, it returns the results shown above.



