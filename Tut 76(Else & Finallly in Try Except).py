'''
Else & Finally IN Try Except
'''

f1 = open("harry.txt")
try:
    f = open("does.txt")

# except Exception as e:       # agar ' try ' fail ho gaya run karne me jo humne usse input dia ho woh . then vo except ka andar ghusega .. Magar try wala run ho gaya toh woh except me nahi ghusega.
#     print(e)

except EOFError as e:                         # EOF error is an type of error.
    print("Print eof error aa gaya hai",e)

except IOError as e:                         # IO error is an type of error.
    print("Print IO error aa gaya hai",e)


else:
    print("This will run only if except is not running")              # agar 'except' term run hui toh 'else' run nahi hoga and vice versa. inn dono may se sirf ek hii chiz run hogi.

finally:                           # finally - ye aisa hai ki chahe hamara code try me jaye ya except me par ending me finally wala run hona hii hai , bhale hi try ya except me kuch error mile.
    print("Run this anyway...")      # code clean up k liye bhi 'finally' ka istemal karte hai.
    #f.close()
    f1.close()
print("Important stuff")

