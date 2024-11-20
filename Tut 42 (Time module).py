'''
Time module in Python
'''

import time

# for i in range(45):
#      print("This is nilay bhai")

initial = time.time()                     # time.time() is tick of clock second's hand.

k = 0
# while(k<45):
#     print("This is nilay bhai")
#     time.sleep(0.9)
#     k+=1                         # This line is same as, K = k + 1

print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(45):
    print(" nilay bro OP")
print("For loop ran in ", time.time() - initial2, "Seconds")
'''
2nd function          This function will give us a exact time in present with date, day and year.
'''
localtime = time.asctime(time.localtime(time.time()))
print(localtime)


seconds = time.time()

# time.localtime(seconds)

'''
Practise
'''

# seconds = time.time()
# print("Seconds since epoch =", seconds)
# time.asctime()


# time.localtime([1])
#
# print("time.localtime() returns: %s",time.localtime())

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

y = datetime.datetime.now()   # When we execute the code from the  beside example  the result will be:
print(y)                       #        2021-07-08 17:30:35.919653
                               #The date contains year, month, day, hour, minute, second, and microsecond.
