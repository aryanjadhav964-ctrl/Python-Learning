# sorting list in python learning with some examples + notes

## basic sorting the list
thisList = ["mango", "apple", "banana", "kiwi", "pineapple","orange"]
# print(thisList)
#  after sorting the list [ it sorts list according to the aplphabetical order]
thisList.sort()
# print(thisList) # acending order

# list sorting in descending order
thisList.sort(reverse= True)
# print(thisList)

numbers = [10, 2, 34, 23, 55, 100, 89, 1]
# sorting number list in ascending and descending order
numbers.sort()
# print(numbers)
numbers.sort(reverse= True)
# print(numbers)


## Customize sort function ##
def myFun(n):
    return abs(n - 50)

nums = [100, 50, 65, 82, 23]
nums.sort(key = myFun)
# print(nums) 
## here -> its sort original nums according to the return values

# Python compares characters using their Unicode values. [A = 65, B = 67, Z = 90, a = 97, b = 98, z = 122]
# example 
fruits_list = ["Kiwi", "Orange", "banana", "apple"]
fruits_list.sort() # output -> ['Kiwi', 'Orange', 'apple', 'banana']
# print(fruits_list)
fruits_list.sort(key= str.lower) # it sort lowercase first and then uppercase
# print(fruits_list)

fruits_list.reverse() # sorts list into a reverse order
print(fruits_list)