# We cannot change tuples values like other collections methods after creating the tuple
# workaround : convert tuple into list, change the values and then again convert it back into tuple
x = (1,2,3,4,5)
y = list(x)
# print(type(y))
y[1] = 10
y.append(100)
x = tuple(y)
# print(x, type(x))

# another way

thisTuple = ("Apple", "Orange", "Banana")
y = ("Pineapple",)
thisTuple += y
# print(thisTuple)

del thisTuple
# print(thisTuple)

## looping on tuples
# for i in x:
#     print(i)

## using while loop : len() counts from 1 not from 0 that's why we do i < len(tuple)
# i = 0
# while i < len(x):
#     print(x[i])
#     i += 1

## joining the tuples 
fruits = ("Apple", "Banana", "Pineapple", "Kiwi", "Apple")
dryFruits = ("Cashew", "Almond", "Pista", "Geen Pista", "Dry Figs")

allInOne = fruits + dryFruits
# print(allInOne)

# print(fruits * 2)
# print(fruits.count("Apple"))
# print(fruits.index("Apple")) # 0 