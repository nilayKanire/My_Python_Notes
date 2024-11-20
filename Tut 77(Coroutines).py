'''
Coroutines IN Python
'''
'''
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)                      # iss line ka meaning hai ki hum apne ' searcher ' function ko as a coroutine use karne wale hai.
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()                  # yeaha humne search naam ka instance create kiya.
next(search)                        # next(search) ye leta hai delay time ka jo humne dia hai , q ki ye line pure start se run hoti hai fir iske bad k koi bhi line direct while loop se start hogi.
search.send("harry")                    # Coroutine me sabse pahle yaha tak pura run hoga starting se if , else tak.
                                      # but uske baad jo bhi hum niche likhenge iske bad wo time.sleep() matlab starting se run na hoke bich me se hi run hoga
                                        # matlab  while True wali line se.

search.close()                  # ek baar jab book me se ya kahi aur se pura text read karna ho jata hai toh, close karna bhi jaroori hai.

# input("Press any key\n")
# search.send("code")
'''

'''
Question
'''

def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "Dog is my pet . but he is so lazy and alway lying on floor and sleeping, His name is Rana"
    time.sleep(1)

    while True:
        text = (yield)
        if text in book:
            print("Yes,your text is in the book")
        else:
            print("No,your text is not in the book")

search = searcher()
next(search)
search.send("lazy")



inp = input("please enter the word u want to search\n")
search.send(inp)
search.close()

'''
def names():
    import time
    names = "akash harry haris carry amit ajey bhuvan shubham rahul aftab hrithik vivek ujjawal mohit rohit"
    time.sleep(2)

    while True:
        text = (yield)
        if text in names:
            print("Your name is in the list.")
        else:
            print("Your name is not in the list.")

name = names()
next(name)
name.send(input("Type your Name: "))
name.close()
'''