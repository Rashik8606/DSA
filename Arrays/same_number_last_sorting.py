lis1 = [10,20,30,40,50,40,20,80,90]
def sort_arr_last(array):
    count_dict = {}
    for i in array:
        if i in count_dict:
            count_dict[i] +=1
        else:
            count_dict[i] = 1

    # return count_dict

    unique_arr = []
    duplicate_arr = []

    for i in array:
        if count_dict[i] == 1:
            unique_arr.append(i)
        else:
            duplicate_arr.append(i)

    for i in range(len(unique_arr)):
        for j in range(len(unique_arr)-i-1):
            if unique_arr[j] > unique_arr[j+1]:
                temp = unique_arr[j]
                unique_arr[j] = unique_arr[j+1]
                unique_arr[j+1] = temp

    for i in range(len(duplicate_arr)):
        for j in range(len(duplicate_arr)-i-1):
            if duplicate_arr[j] > duplicate_arr[j+1]:
                temp = duplicate_arr[j]
                duplicate_arr[j] = duplicate_arr[j+1]
                duplicate_arr[j+1] = temp

    return unique_arr + duplicate_arr

print(sort_arr_last(lis1))