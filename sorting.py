# Bubble Sort

def bub_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [5, 3, 8, 7 , 9 , 0]
bub_sort(nums)

print(nums)


# Selection sort
def select_sort(nums):

    for i in range(len(nums)):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [5, 3, 8, 7 , 9 , 0]
select_sort(nums)

print(nums)


# Insertion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j]  = arr[j], arr[j - 1]
            j -= 1

arr = [ 2, 6, 5, 1, 3, 4]
insertion_sort(arr)
print(arr)



# Merge  sort
