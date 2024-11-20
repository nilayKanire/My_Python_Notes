# Prime number program
'''
n = int(input("Enter Number \n"))

for i in range(2,n):
    if n%i == 0:
        print(n, "is not a prime number")
        break
else:
    print(n, "is Prime number")



# Linear search

pos = -1

def search(list, n):
    i = 0;

    while i < len(list):
        if list[i] == n:
            globals() ['pos'] = i
            print("Found at", pos)
            return True
        i = i + 1
    else:
        print("Not Found")
        return False

list = [5, 8, 4, 6, 9, 2]
n = 2

search(list, n)

'''


# Binary Search
pos = -1

def binary_search(list, n):

    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals() ['pos'] = mid
            print("Found at", pos)
            return True
        else:
            if list[mid] < n:
                l = mid;
            else:
                u = mid;
    else:
        print("Not Found")

list = [5, 8, 4, 6, 9, 2]
n = 9

binary_search(list, n)


    


