# Print list of Number

n = int(input("Enter the Number: "))

# for num in range(2, n + 1):
    # count = 0
# 
    # for i in range(1, num + 1):
        # if num % i == 0:
            # count += 1
# 
    # if count == 2:
        # print(num)

# Reverse a Number

# rev = 0
# while n != 0:
#     dig = n % 10
#     rev = rev*10 + dig
#     n //= 10

# print(rev)

# Palindrome number Check

# rev = 0
# org = n 
# while org != 0:
#     dig = org % 10 
#     rev = rev * 10 + dig
#     org //=10

# if rev == n:
#     print(f"{n} Its Palindrome Number")
# else:
#     print("Its Not Palindrome Number")

# Armstrong Number

org = n
arm = 0
while n != 0:
    dig = n % 10
    arm = dig ** 3 + arm
    n //=10

if arm == org:
    print(f"{arm} is armstrong Number")
else:
    print("Not Armstrong Number")
