a = int(input("enter a number = "))

b = 0

while a != 0:
    digit = a % 10
    b = b * 10 + digit
    a //= 10

print("Reversed Number: " + str(b))