#Python program to find the factorial of a number using recursion

num = int(input())
factorial = 1
for i in range(1,num + 1):
  factorial = factorial*i
print("Factorial of a Number",factorial)