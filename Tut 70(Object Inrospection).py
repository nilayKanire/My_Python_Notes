'''
Object Inrospection   - object instrospection ka matlab hota hai ki kisi bhi object k baare me janna, uske baare me jankari lena ki vo kis class se aya hai, kis type ka hai , kaise store ho raha hai,vo sab jo ho raha hai uski jankari ko prapt karne ko kahte hai object Introspection.
'''
skillf = Employee("Skilll", "F")
print(skillf.email)
# Python me sab kuch object hote hai , jaise str,int object hai. aur uss object ka type nikalne ke liye hamare pass ek function hota hai.

print(type(skillf))                   #jab hum type(skillf) run kar rahe hai toh hum ek tarah se object introspection kar rahe hai.
print(type("this is a string"))      # ye hume object ka type bata raha hai, jo ki string hai.

print(id("That that"))              # ye hume object ki 'id' bata raha hai run karne par. Har object ko ek unique id di jati hai.
# ye batata hai ki kis ' id ' se save hua hai apna object back-end me.

'''
Object introspection karne ke tarike
'''
#------------1. type  ------------------
#------------2. id    ------------------

#------------3. Dir   ------------------  iss module k andar agar apan koi bhi object daalte hai toh vo bata denga ki hum uske saath kya kya khilwad kar sakte hai.

o = "This is a string"
print(dir(0))                   # run karne k bad ye hume vo saare method denga ,Jo iske andar define hai. Hum kya kya kar sakte hai uske andar vo sab hume dega.

print(dir(skillf))       # Run karne k bad hume ye skillf k saare function de denga. usme fname,lname, attributes bhi milenge, jo bhi saare k saare function hai vo batayega ye.

import inspect
print(inspect.getmembers(skillf))     # run karne k baad vo saare members show kar dega.

'''
search for inspect module in google for knowing different functions of inspect module and try run diff. function of this module.
'''