#Python program to find the largest number in a list without using built-in functions

List = []
size = int(input())
for i in range(size):
    numbers = int(input())
    List.append(numbers)
largest = 0
for numbers in List:
    if numbers > largest:
        largest = numbers
print("Largest Number in List is", largest)