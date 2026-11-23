# level one : basic understanding 
# 1 ......... Create a list of five fruits. Add "Mango" to the end of the list using append().
fruits = ["apple", "banana", "kiwi", "pineapple", "orange"]
fruits.append("mango")
# print(fruits)
# 2.... count elements -- find how many 10s are in the list
numbers = [10, 20, 10, 30, 10, 40, 50]
numCount = numbers.count(10)
# print(numCount)           #3
# print(numbers.count(10))  #3

# 3.....finding the index - find index using the index method.
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
# print(colors.index("Green"))      # 2

# 4....... insert -- Insert "Rohan" at index 2 without replacing any existing element.
students = ["Aryan", "Rahul", "Sujal", "Amit"]
students.insert(2, "Rohan")
# print(students)

# pridict the output - 
numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(1, 15)

# print(numbers) # [10, 15, 20, 30, 40]

### Level 2 - removeing and modifing elements ###
## 6 - romem by value, Remove "Tata" using remove().
cars = ["BMW", "Audi", "Tata", "Honda", "BMW"]
cars.remove("Tata")
# print(cars)

### 7 - Remove the element at index 2 using pop().
numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
# print(numbers)
## 8 - remove last element
languages = ["Python", "Java", "Kotlin", "C++"]
languages.pop()
# print(languages)
### 9 - reverse a list
marks = [85, 90, 75, 60, 95]
marks.reverse()
# print(marks)

## 10--- clear the list
subjects = ["Python", "Java", "DBMS", "Networking"]
subjects.clear()
# print(subjects)

## level 3 : 
## 11 - Create a separate copy of this list. Add 50 to the copied list., Print both lists. Check whether the original list changes.
original = [10, 20, 30, 40]

original2 = original.copy()
original2.append(50)
# print(f"{original} and {original2}")
# 12 -- combine both the lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
# print(list1)

## 13 --- sort in ascending prder
numbers = [45, 12, 89, 23, 5, 67]
numbers.sort()
# print(numbers)

## 14 --- Use the same list from Q13 and sort it from largest to smallest.
numbers.sort(reverse= True)
# print(numbers)

# 15-- case insentive sorting : Sort the names alphabetically without considering uppercase and lowercase differences.
names = ["banana", "Apple", "cherry", "Mango", "orange"]
names.sort(key = str.lower)
# print(names)

#### level 4 =  logocal thinking
##16 -- Create a new list containing only unique values.
numbers = [10, 20, 10, 30, 20, 40, 50, 30]
uniqueNum = []
for num in numbers:
    if num not in uniqueNum:
        uniqueNum.append(num)

# print(uniqueNum)

## 17 --- Student marks management
marks = [75, 82, 90, 65, 82, 95, 70]
# Perform these operations:
# 1. Add 88 to the list.
marks.append(88)
# 2. Count how many times 82 appears.
marks.count(82)
# 3. Remove 65.
marks.remove(65)
# 4. Sort the marks in descending order.
marks.sort(reverse= True)
# 5. Print the final list
# print(marks)

## 18 - shoping cart
cart = ["Laptop", "Mouse", "Keyboard"]
# Perform these operations:
# 1. Add "Monitor" to the cart.
cart.append("Monitor")
# 2. Insert "USB Cable" at index 1.
cart.insert(1, "USB cable")
# 3. Remove "Mouse".
cart.remove("Mouse")
# 4. Print the final cart.
# print(cart)

## 19 -- find the second largest number
#Find the second-largest unique number using list methods.
numbers = [10, 50, 20, 80, 40, 80, 60]

largest = float("-inf")
secondLargest = float("-inf")
for x in numbers:
    if x > largest:
        secondLargest = largest
        largest = x
    elif x > secondLargest and x != largest:
        secondLargest = x

# print(f" largest {largest} and second Largest {secondLargest}")

## 20 -- list manipulation 
numbers = [5, 10, 15, 20, 25, 30]
# Perform the following:
# 1. Create a copy of the list.
num2 = numbers.copy()
# 2. Add 35 to the copied list.
num2.append(35)
# 3. Remove 15 from the copied list.
num2.remove(15)
# 4. Reverse the copied list.
num2.reverse()
# 5. Extend the original list using the copied list.
numbers.extend(num2)
# 6. Sort the final original list in ascending order.
numbers.sort()
# print(numbers)