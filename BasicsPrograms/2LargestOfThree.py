
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))

if a > b and a > c:
    print(f"{a} is greater")
elif b > a and b > c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")

