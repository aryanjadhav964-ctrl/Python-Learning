fibonacci = []
a = 0
b = 1
while a < 50:
    fibonacci.append(a)
    a, b = b, a+b

print(fibonacci)