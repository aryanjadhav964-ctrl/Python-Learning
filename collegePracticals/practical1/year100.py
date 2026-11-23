import datetime

# taking input form users
name = input("Enter your name : ")
age = int(input("Enter your age : "))

#get the current year dynamically 
current_date = datetime.date.today().year

year_turn_100 = current_date + (100 - age)

print(f" Hello {name} you'll turn 100 in {year_turn_100}.")