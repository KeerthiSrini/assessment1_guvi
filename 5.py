#Python program to implement linear search

length = ""
def linear(List,length,request):
    for i in range(0, length):
        if (List[i] == request):
            return i
    return 0
    

List = []
size = int(input("Enter the Size of the List "))
for i in range(size):
    numbers = int(input("Enter the Elements to add in List "))
    List.append(numbers)
    length = len(List)
request = int(input("Enter the Element to Find "))
output = linear(List,length,request)
if(output == 0):
    print("Element not Found")
else:
    print("Index of the Element is", output)
