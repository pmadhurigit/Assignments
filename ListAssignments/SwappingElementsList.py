# about swapping elemnets in a list

def swapList(list):
    size = len(list)

    # swapping
    temp = list[0]
    list[0] = list[size-1]
    list[size-1] = temp

    return list

# driver code
list = input("enter elements: ")
print(f'list elements are: {list}')
print(swapList(list))