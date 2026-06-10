print("Find largest of 3 number")
a = int(input(" Enter a "))
b = int(input(" Enter b "))
c = int(input(" Enter c "))

if a > b:
    if a > c:
        print(f" {a} is largest of 3 number")
    else:
        print(f"{c} is largest of 3 number")
else:
    if b > c: 
        print(f" {b} is largest of 3 number")
    else:
        print(f" {c} is largest of 3 number")

