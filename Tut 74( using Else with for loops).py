'''
Using Else with For Loops
'''

khana = ["roti", "Sabzi", "chawal"]
#
# for item in khana:                  # for ' loop ' k saath ' else ' tabhi work karta hai ,jab for loop normally  end ho. yaniki for loop ko koi break statement na mile.
#     print(item)
#     #break
#
# else:
#     print("This for loop ended properly")

for item in khana:
   if item == "paratha":
        break

else:
    print("your item not found")