'''
If __name__==__main__ usage & necessity
'''

def printhar(string):
    return f"ye string harry ko de de thakur {string}"

def add(num1, num2):
    return num1 + num2 + 5





print("and the name is", __name__) # this line is usued for only explanation purpose only .

if __name__ == '__main__':         # creatin this main line shotcut is to - type   main + enter key
    print(printhar("harry1"))
    o = add(4, 6)
    print(o)
# This main file is used to stop the run of  the only content which is present inside it whenever we are importing the  file into another place .
#  This main file content only runs here , were it is present in its original file. it doesnt run anywhere else.
