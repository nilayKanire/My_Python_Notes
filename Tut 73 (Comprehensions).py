'''
Python Comprehensions
'''
# ----------------- LIST COMPREHENSION ----------------------
'''
# ls = []
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)
#
# print(ls)

ls = [i for i in range(100) if i%3==0]       #This is the list comprehension of the above many lines code in few line.
print(ls)
# LIST COMPREHENSION - 1 line me list ko banane ka tarika
'''
# ------------------ DICTIONARY COMPREHENSION -----------------------
'''
# dict1 = {0:"item0", 1:"item1",2:"item3 " ' and so on ......' }
# print(dict1)

dict1 = {i:f"item{i} " for i in range(1 , 10001) if i%100 == 0}               # range function jo hai vo   ' 0  to n-1 '  tak value leta hai
print(dict1)
# This dictionary comprehension not only helps in making dict of large no. of items but it also used to reverse the key value pair of dict.

dict1 = {i:f"Item{i} " for i in range(5)}

dict2 = {value:key for key, value in dict1.items()}               # with this line we can reverse ki key value pair means dictionary ko ulti kar dena.
print(dict1,"\n", dict2)
'''
# ------------------- SET  COMPREHENSION -----------------------------
'''
# in set comp. the values are taken only 1 time only not repeatedly.

dresses = {dress for dress in ["dress1 ","dress2 ","dress1 ",
                              "dress2 ","dress1 ","dress2 "]}           # this curly bracket end shows that it is set. If we used square bracket then it will become list.
print(dresses)
print(type(dresses))
'''
# ----------------- GENERATOR COMPREHENSION -----------------------------
#  generator hamare pass aise function hote hai jo ki yeild karte hai. yaniki generate karne k layak hote hai but actually generate  nahi karte. Hum chahey toh unse on the fly value generate karwa sakte hai.
'''
evens = (i for i in range(100) if i%2==0)
print(type(evens))
print(evens)
# print(evens.__next__())

for item in evens:
    print(item)

# Generator comprehension  -     1 line me generator produce karte hai
'''

# ----------------------- QUIZ --------------------

inp1 = int(input("How many items do u want to add  in list \n"))

if inp1==0:
    dict = {i: f"Item{i} " for i in range(5)}
    print(dict)
elif inp1>0:
    dict = {i: f"Item{i} " for i in range(5 + inp1)}
    print(dict)

inp2 =int(input("which type of comprehension do you want to  make"
      "1. list comp  , 2. dict comp,  3. set comp \n"))
if inp2 == 1:
    print(list(dict))
elif inp2 ==2:
    print(dict)
elif inp2 == 3:
    print(set(dict))



