def find_target_num(arr,target): # init arr and target 
    empty_arr = [] # init empty array 
    for i in range(len(arr)): # length of arr 
        current = arr[i]   # current index [0,1,2,] like that
        difference = target - current  # difference between target and current 
        if difference in empty_arr:  # is empty array in the number 
            return current, difference   # then print that current number & diffence number
        else :
            empty_arr.append(current)  # else append the current number 

    return f'not in the list '  # not here then print 

print(find_target_num([2,4,5,63,56,78,9],72))