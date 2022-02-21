#Python program to find the product of a set of real numbers

number = int(input())
multiples = int(input())
for n in range(1,multiples+1):
  result = number*n
  print("Product of set of Real Numbers is",result, end=" ")