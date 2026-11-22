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

print(numbers) # [10, 15, 20, 30, 40]

