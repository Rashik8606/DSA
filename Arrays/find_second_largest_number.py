def second_largest_number(lis):
    first_largest = float('-inf')
    second_largest = float('-inf')
    for i in lis:
        if i > first_largest :
            second_largest = first_largest
            first_largest = i
        if i < first_largest and i > second_largest:
            second_largest = i
    return second_largest
print(second_largest_number([1,2,3,4,5,6,-1,2.8]))