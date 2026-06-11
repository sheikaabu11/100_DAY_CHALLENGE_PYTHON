n = int(input(" enter a number  : "))

# sum of number
sum = n * (n+1)//2
print(sum)

# table

for i in range (1,10) :
  print(f" {n} X  {i} =  {n*i}")


# Factorial 
factorial = 1
for i in range (1,n+1):
  factorial  =factorial * i

print(factorial)