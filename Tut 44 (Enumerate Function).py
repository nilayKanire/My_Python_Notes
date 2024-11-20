'''
Enumerate Function
'''

l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

# By Normal method
# i = 1
# for item in l1:
#     if i%2 != 0:
#         print(f"Jarvis please buy {item}")
#     i += 1

#By Enumerate Function Method                               When calling a simple enumeration function, we have to provide two parameters:
                                                            # The data structure that we want to iterate
                                                            # The index from where we want to start our iteration
                                                            # Note: The iterable must be an object that supports iteration
for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please buy {item}")

list_1=["code","with","harry"]
for index,val in enumerate(list_1):
    print(index,val)

'''
Using Enumerate() on a list with start Index:
In the below example, the starting index is given as 5. The index of the first item will start from the given starting index.
'''
list_2 = ["Python", "Programming", "Is", "Fun"]
#Counter value starts from 5
result = enumerate(list_2, 5)
print(list(result))
# If we do not provide the index, we want to start the iteration from then it automatically starts its iteration from zero index i.e., the beginning of the data structure.

