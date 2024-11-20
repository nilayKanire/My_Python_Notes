"""
For Loops in Python
"""
list1 = ["Harry", "Nilay","Larry","Carry"]
for item in list1:
    print(item)
list1 = [["Harry",1], ["Nilay",2], ["Larry",6], ["Carry",250]]         # <-- here we created list of list and unpacked it.
for item in list1:
    print(item)

for item, lollypop in list1:
    print(item,lollypop)
    print(item, "and lolly is", lollypop)               # This gives Itration
    # after running we get||
    #                     VV
'''    
Harry and lolly is 1                <--  here we get  "Itration" in each of  this is written.
Nilay and lolly is 2
Larry and lolly is 6
Carry and lolly is 250
'''
dict1 = dict(list1)       # typcasting list1 into an dictionary
print(dict1)
for item, lollypop in dict1.items():
    print(item, "and lolly is", lollypop)

# for only getting key |||
     #                 VVV
for item in dict1:
    print(item)

"""
 ||| QUIZ
 VVV
"""
# Create a list and only find out from list that there will only be number, and number greater than and equal to 6. and print those.
items = [int,float,"Harry",5,3, 3,22,21,64,23,233, 23,6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)


n = 7
for i in range(1,11):
    print(n,"x", i,"=", n*i)
