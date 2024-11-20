'''
Generators in Python             - we use generator object because they create value on the fly and therefore we use them to save our ram
'''
"""
Iterable -  __iter__()  or  __getitem__()  ,iterable me ye do method define hote hai.agar hum run kare is program ko toh ye iterator pradan karega.
   |
   V
Iterator -  __next__()
   |
   V
Iteration -
"""
# Iterable  - Iterator ko generate karta hai agar vo function iterable ho toh.

# for i in range(78):         # on the fly generate karra hai values ko . iterate karra hai ,generate karra hai.....same process going again and again. Ek bar humne isse iterate kar dia toh fir apan usse agli baar iterate nahi kar payenge agar vo ek generator hai.
#     print(i)                # range  is an generator . Toh isliye hum use sirf ek baar iterate kar sakte hai.

def gen(n):
    for i in range(n):   # 'yield' on the fly generate karega values ko , yield hamara generator hai . generator kabhi   function nahi hota.
        yield i         # if we write ' return ' in place  of yield then it will be funtion k return value hai aur return statement ko dekhke func. laut jayega wapas. yaniki uske aage usse kuch nahi karna hai, ' return ' k baad kuch bhi likhdo wo run nahi hone wala.
                        # if we write ' print ' in place  of yield then print jo hai vo console pe print karta hai. matlab hume wo run wali tab me dikhega aur function apna chalta rahega.
# g = gen(4522626245624642)
# print(g )

#jab bhi hume values chahiye rahenge generator se toh hum le lenge . apan ko itne bade no. ki ' list ' banana nahi purata, values stores karne k liye . therfore we use generator.

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
for i in g:            # for loop me hume stop iteration error nahi maila kyuki, ' for loop ' automatically usko handle kar leta hai, for loop ka design hii aisa kuch hota hai ki we ' stop iteration ' ko handle kar lete hai aur jaise hii khatam hota hai generator wo ruk jata hai wahi par.
    print(i)

h = "harry"           # string ye iterable hoti hai ,matlab hum usse iterate kar sakte hai aur usme __iter__ method use hota hai.
print(h[0])
print(iter(h))

for c in h:
    print(c)

ier = iter(h)                   # integer items are not iterable q ki isme __iter__ ya __getitem__ define nahi hota hai our hum isse iterator pradan nahi kar sakte.isliye hum ise iterate nhi kar sakte.
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())