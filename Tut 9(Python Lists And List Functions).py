grocery = ["Harpic","vim bar" ,"deodrant","Bhindi",
           "Chocolate", 98]
print(grocery[5])
numbers = [2,7,9,11,3,5]
"""
   ||||       This lines changes the original list.    
   VVVV    
"""
numbers.sort()
numbers.reverse()
"""
   ^^^^
   ||||
"""

print(numbers[2])
"""
Slicing  ||||   THis lines doesnt changes the original list.
         VVVV
"""
"""
print(numbers[0:6])   # OR   print(numbers[:6])   OR  print(numbers[:])
print(numbers[::1])   # OR   print(numbers[::])
print(numbers[::2])    # Here we put 2 , to skip letters by 1 words. If we increase the no. then the skipping of no. increases.
print(numbers[::-1])  # -> this -1 reverse the list and it is called as Negative Slicing.
# Tip - dont use less than -1 integer if we dont written any including & excluding Number in bracket for +ve slicing
"""
"""
Some Imp.  List function in strings 
"""
"""
print(len(numbers))
print(min(numbers))
print(max(numbers))
"""
numbers_x = []
numbers_x.append(89)
numbers_x.append(89)
numbers_x.append(89)
numbers_x.append(98)
numbers_x.append(89)
numbers_x.append(77)
print(numbers_x)
numbers_x.insert(2,69)
#numbers_x.remove(9)
numbers_x.pop()
print(numbers_x)
numbers_x[1] = 98   # -->> it replaces the 1th term no. to 98   which is on 2nd position.
print(numbers_x)
"""
Mutable - can change
Immutable - cannot change
"""
#tp = (1,2,3)        # tp - tupple  , () - paranthesis , [] - square bracket
#tp[1] = 8       -->>  tupple is immutable. It gives  paranthesis bracket() after runing in output.
#tp = (1,)
#print(tp)
"""
|||How to swap a two number values
VVV
"""
a = 1
b = 8
#  ||| By Traditional Method
#  VVV
"""
temp = a
a = b
b = temp
print(a,b)
"""
# |||  By Phython Method
# VVV
a,b = b,a
print(a, b)
"""
# Practise    |||
              VVV
"""
