# Count Digit

n = int(input("Enter the Number : "))
count = 0
while n != 0:
    n //= 10
    count += 1

print("Digits: ",count)