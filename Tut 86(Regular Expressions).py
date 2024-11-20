'''
Regular Expressions
'''

import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''                  # how to search using regular expression inside a string

# Regular Expression k andar k functions -   fundall , search, split, sub, finditer
''' Meta Characters

pattern = re.compile(r'fass')            # r'' - raw string hoti hai , iske andar agar humne \n ya koi bhi escape sequence character likha toh bhi vo normally print hoga koi new line create nahi hogi.

patt = re.compile(r'.adm')                    # .        Any charcter (except newline character)
patt = re.compile(r'^adm')                    # ^        Starts with
patt = re.compile(r'^Tata')                   # agar starts with Tata ho rahi hai ye mystr toh ye return karega kuch varna nahi karega.
patt = re.compile(r'Tata$')                   # $          End with

patt = re.compile(r'ai*')                   # *               Zero or more occurences. star ka matlab hai kitne bhi characters , a fir uske bad i aur i kitne bhi ho , q ki humne i k baad * lagaya hai agar hum a k baad * lagaye jaise a*i fir a kitne bhi ho i ke pahle.
patt = re.compile(r'ai+')                   # +                   one or more occurences

patt = re.compile(r'ai{2}')                 # {}        Exactly the specified number of occurences
patt = re.compile(r'(ai){2}')               # ()     Capture and group
'''
# Special Sequences

# patt = re.compile(r'\bFax')
# patt = re.compile(r'\d{5}-\d{4}')
#
# matches = patt.finditer(mystr)        # here we r finding the ' fass ' word in mystr.
# for match in matches:
#     print(match)
    # print(mystr[448:452])                   # 448 , 452 is the span value we got from match.

# Task
'''
Given a string with a lot of indian phone numbers starting from +91
'''
phonelist = ''' phone1 : +91-6345432453
phone2 = +91-9878978684
phone3 : +91-7887657678
phone4 = +980-8087987'''

find = re.compile(r'[+]91-\d{10}')

matches = find.finditer(phonelist)
for match in matches:
    print(match)