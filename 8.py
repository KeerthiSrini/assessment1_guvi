#Python program to delete an element from a list by index

a=[1,2,3,4,5,6]
n = int(input())
length = len(a)
# print(length)
if(n<length):
    a.pop(n)
    print("Index Found")
else:
    print("No Index Found")
print(a)