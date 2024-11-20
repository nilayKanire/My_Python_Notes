'''
F-Strings & String Formatting In Python
'''
import math


me = "Nilay"
a1 = 3
a = "This is  %s"%me

a = "This is %s %s"%(me, a1)
a = "This is {1} {0}"                 # Here 1 wale may (me) ko fit kar diya aur 0 wale may (a1) ko fit kardiya.
b = a.format(me, a1)

print(b)

'''
F-Strings   concept|||                            # this f-string means fast basically because it executes operations in lesser line and saves time for writing. 
                   vvv
'''

a= f"this is {me} {a1} {4*65} {math.cos(65)}"                         # Here we can use python's variable expression like 4*65
print(a)

# explore time module   <<<---  Practise

# c = {45*2}
# print(c)