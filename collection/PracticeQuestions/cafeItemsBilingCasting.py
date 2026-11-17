## Question : Write a Python function calculate_total(items) that:
## 1. Loops through the list of strings.
## 2. Converts each valid price into a whole number (int) by dropping the decimals (for example, "249.99" becomes 249).
## 3. Safely skips any text that isn't a valid number (like "invalid" or "free") without crashing the program.
## 4. Returns the final sum of all valid items.
## Expected Output: For the list above, your function should return 519 (150 + 249 + 80 + 40).
## Hint: Combine int(float(...)) with a try / except ValueError block! Give it a shot and share your code when you're ready.
#order list

ordered_Items = ["150", "249.99", "invalid", "80.50", "free", "40"]

############### My first approach [Wrong] ####################
# def calculate_total(items):
#     for i in items:
#         global x
#         global current_total_bill
#         current_total_bill = 0
#         x = []

#         if isinstance(i, str):
#             continue
#         else:
#             y = int(i)
#             current_total_bill = current_total_bill + y
#     return current_total_bill

############## second approach ##############
def calculate_total(items):
    current_total_bill = 0

    for i in items:
        try:
            a = int(float(i))
            current_total_bill += a
            pass
        except ValueError:
            continue
    return current_total_bill


total_bill = calculate_total(ordered_Items)
print(f"Total bill is : {total_bill}")
