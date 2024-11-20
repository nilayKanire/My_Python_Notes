'''
Pickle Module
'''
# pickling means preserve rakhna aur time k liye

import pickle

# Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki", "Bugati"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')          # wb - writing of binary  , q ki ye binary file format hota hai.
# pickle.dump(cars, fileobj)          # dump function ye do Aruguments leta hai. 1st ye lete hai vo object jo hum pack karna chahte hai aur 2nd leta hai vo file object not a file.
#
# fileobj.close()


file ="mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)     # pickle.loads() argument me bytes object leta hai
print(mycar)
print(type(mycar))

# pickle.loads() is used to load pickled data from a bytes string
#
# dumps() will convert them into an byte format
# loads() will convert the byte into previous format data
