def remove_duplicate(list1):
    sorted_array = []
    for i in range(len(list1)):
        if i == 0:
            sorted_array.append(list1[i])
        elif list1[i] != sorted_array[-1]:
            sorted_array.append(list1[i])
    return sorted_array
print(remove_duplicate([1,1,1,2,2,3,3,4,5]))

