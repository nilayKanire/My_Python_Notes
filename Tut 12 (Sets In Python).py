"""
Sets in Python
"""
s = set()
print(type(s))
l = [1,2,3,4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(2)
s1 = s.union({1,2,3})
s2 = s.intersection({1,2,3})

print(s1)
print(s2)
print(len(s1))
print(min(s1))
print(max(s1))
s1 = {4,6}
print(s,s1)
print(s.isdisjoint(s1))
