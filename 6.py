#Python program to implement binary search

def binary(List, request):
    low = 0
    mid = 0
    high = len(List) - 1 
    while low <= high:
        mid = high + low
        if List[mid] < request:
            low = mid + 1
        elif List[mid] > request:
            high = mid - 1
        else:
            return mid
    return 0


List = []
size = int(input("Enter the Size of the List "))
for i in range(size):
    numbers = int(input("Enter the Elements to add in List "))
    List.append(numbers)
request = int(input("Enter the Element to Find "))
output = binary(List, request)
if(output == 0):
    print("Element not Found")
else:
    print("Index of the Element is", output)