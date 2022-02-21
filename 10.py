#Python program to find the average of 10 numbers using while loop

inputs = int(input())
iterator = 0
add = 0
number = int(input())
while iterator < 10:
    add = add + number
    iterator+=1
average = add/10
print("Average of 10 Numbers",average)