# chack if array is sort or not ?
def is_sorted(lis1):
    sorted_array = True
    for i in range(len(lis1)-1):
        if lis1[i] > lis1[i+1]:
            sorted_array = False
            break
    if sorted_array:
        print('This list is sorted !')
    else:
        print('This list is not sorted !!')
    return sorted_array
print(is_sorted([1,2,3,4,5,6,7,9,8]))