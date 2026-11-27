# use "_" as the last value of the code block when you want to execute it when there are no other matches
day = 4
month = 5
match day:
    case 1:
        print("One day")
    case 2:
        print("Day two")
    case 3:
        print("Day three")
    case 4:
        print("Day four")
        ## combine values
    case 6 | 7 | 8 | 9:
        print("Leave Days")
        ## if satement as a guard
    case 10 if month == 5:
          print(" day 10 of 5th month")
    case _:
            print("No Match")

