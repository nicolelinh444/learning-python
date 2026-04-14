# Computes the sum of all odd numbers between a and b (inclusive) using a while loop.

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

if a % 2 == 0:
   a += 1
   
sum = 0
number = a

while number <= b:
   sum += number
   number += 2
   
print("The sum of odd numbers between", a, "and", b, "is:", sum)