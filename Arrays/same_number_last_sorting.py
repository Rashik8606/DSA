lis1 = [7,5,4,3,2,10,9,8,7,6,5]
def same_num_last(array):
    count_of_num = {}
    for i in array:
        if i in count_of_num:
            count_of_num[i]+=1
        else:
            count_of_num[i]=1
    
    unique_arr = []
    duplicate_arr = []

    for i in array:
        if count_of_num[i] == 1:
            unique_arr.append(i)
        else:
            duplicate_arr.append(i)
    unique_arr.sort()
    duplicate_arr.sort()

    return unique_arr + duplicate_arr

print(same_num_last(lis1))