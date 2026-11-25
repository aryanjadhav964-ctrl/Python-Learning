## all about conditional statement 

## simple if statement 
age = 20 
if age >= 18 :
    print("You are adult")

## if else statement

num = 10
if (num % 2 == 0):
    print("Number is even")
else :
    print("Number is odd")


marks = 85

if marks >= 90 and marks <= 100:
    print("grate A")
elif marks >= 80:
    print("grade B")
elif marks >= 70:
    print("grade C")
elif marks >= 60:
    print("grade D")
elif marks >= 35:
    print("grade E")
elif marks <= 35 and marks >= 0:
    print("grade F")

yourAge = 19
hasLicence = True

if yourAge >= 18:
    if hasLicence:
        print("You can drive")
    else :
        print("You need a licence to drive")
else :
    print("you are underages")

## ternary conditional statemnet
print("Audault "if yourAge >= 18 else "you are child") 

## techniques to write conditional statements [ and, or, not]

if yourAge >= 18 and hasLicence:
    print("you can drive")

if age >= 18 or age <= 60:
    print("special category")

is_loged_in = False
if not is_loged_in:
    print("Please login!")

## using comparison operarion
number = 50
if number == 50:
    print("equal")
if number > 20:
    print("grater")
if number != 100:
    print("not equal")

#### using membership operation in, not in #####

fruits = ["Apple", "Banana", "Kiwi", "Pineapple"]

if "Apple" in fruits:
    print("Apple found")

if "Mango" not in fruits:
    print("Mango not found")

#### Uisng identity operator  is, is not ######

x = None
if x is None:
    print("Value is not assign")


### using loop in conditional 

number = [1,2,3,4,5,6,7,8,9,10]

for num in number:
    if num % 2 == 0:
        print(num, " is even")
    else:
        print(num, " is odd")


########## using match case  ###############

day = 5

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednsday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")