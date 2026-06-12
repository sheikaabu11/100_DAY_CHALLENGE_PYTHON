# Count Digit

# n = int(input("Enter the Number : "))
# count = 0
# while n != 0:
#     n //= 10
#     count += 1

# print("Digits: ",count)

#  Check prime 
n = int(input("Enter a Number : "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")
