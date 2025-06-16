array = [1,2,4,5,7,8,3,70,54,55,-66,7,8,9]
max_num = array[0] # Initialize both max_num and min_num with the first element of the list:
min_num = array[1]
for i in array:
    if i > max_num:  #find i > max_num it help find largest number  of a list 
        max_num = i
    if i < min_num :  #find i < min_num it helps find smallest number of a list 
        min_num = i
print(f'The Largest number is {max_num} and minmum number is {min_num}')

