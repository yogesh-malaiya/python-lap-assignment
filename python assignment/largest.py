a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))

if a > b and a > c:
    print(a, " is the largest number")
elif b > a and b > c:
    print(b, " is the largest number")
else:
    print(c, " is the largest number")