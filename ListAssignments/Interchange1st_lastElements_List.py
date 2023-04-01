# about Interchanging the elements in a list
# x = []
# n = input("enter length of a list: ")

# for i in range(1, int(n)):
#     k = input("enter values: ")
#     x.append(int(k))

# print(f'the list of elements are: {x}')
# x[0], x[-1] = x[-1], x[0]
# print(f'the interchanged list is: {x}')

# or

def swapList(newList):
    size = len(newList)

    # swapping
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp

    return newList

# driver code
newList = [12, 14, 45, 67, 87, 24]
print(swapList(newList))
