#find Second largest number of a list 
def largest_number_list(lis):
    largest_num = float('-inf')
    second_largest = float('-inf')
    for i in lis:
        if i > largest_num:
            second_largest = largest_num # i > largest number then assign second largest 
            largest_num = i  
        if i < largest_num and i > second_largest:  #chack i less than and i greater than second then second - i
            second_largest = i
    return f'First Largest number of list {largest_num} and Second Largest number is {second_largest}'

print(largest_number_list([1,2,3,4,5,6]))