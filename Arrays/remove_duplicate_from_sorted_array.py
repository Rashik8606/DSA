def remove_duplicate(list1):
    sorted_array = []
    for i in range(len(list1)):
        if i == 0:
            sorted_array.append(list1[i])
        elif list1[i] != sorted_array[-1]:
            sorted_array.append(list1[i])
    return sorted_array
print(remove_duplicate([1,1,1,2,2,3,3,4,5]))




# LEETCODE QUESTION 27 Remove Elements

def remove_Elements(array, val):

    pointer = 0
    for i in range(0,len(array)):
        if array[i] != val:
            array[pointer] = array[i]
            pointer+=1
    return pointer

test = [3,2,2,3]
val = 3

print(remove_Elements(test, val))