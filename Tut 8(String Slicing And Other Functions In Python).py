        #0123456789...     18
mystr = "Nilay is a good,boy"  #here N index is "0" that means counting starts from 0.
      #-19      ........-2-1

print(len(mystr))
print(mystr[4])
print(mystr[0:5])     # [0:5] it is  0 including but 5 excluding.
"""
How to skip characters in a word 
"""
#Positive Indexes
print(mystr[0:19:2])     #just adding (:2) at end to skip single characters of a word. if we want to skip more characters then add more no.

#Negative Indexes

print(mystr[-4:])
        #OR
print(mystr[15:18])

#To make your string  REVERSE (ULTA)
print(mystr[::-1])        #just put (-1) at end to make your sting REVERSE.
         #  ||           But if we put(-2) at end then the string will be reversed,also it skip single character of a word while reversing it.
        #   VV
      #   [0:19:-1]     # i.e. taking whole string.
"""
Here are some  String functions.
"""
mystr = "nilay is a good boy"
print(mystr.isalnum())         # numeric  - there should be no space in a sentence.
        # This gives boolean variable/characters (i.e.True or False)
      #OR

print(mystr.isalpha())       # alphanumeric - there should be no space in a sentence.
print(mystr.endswith("boy"))   # Ans - True
print(mystr.endswith("bdoy"))   # Ans - False
print(mystr.count("o"))
print(mystr.capitalize())   # -> makes the first  alphabet of word capital of a sentence ,if it is written small.
print(mystr.find ("is"))
print(mystr.lower())         # makes all alphabet of a sentence small.
print(mystr.upper())         # makes all alphabet of a sentence capital.
print(mystr.replace("is","are"))

"""
Home work
 Search for - Python string function on google
"""

"""
# Practise    |||
              VVV
"""
