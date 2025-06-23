def sub_Array_Sum(array,targetSum):  # init two parameter
    start = 0           # start where it start 
    current_Sum = 0     # current sum 

    for end in range(len(array)):   #  length of array
        current_Sum = current_Sum + array[end]   # add number

        while current_Sum > targetSum and start <= end:   # current_sum greaterthan and start lessthan equal end
            current_Sum = current_Sum - array[start]    # subtract current_sum to array[start]
            start += 1      # increase +1
        if current_Sum == targetSum:   # if equal   
            return array[start:end+1]  #  return start and end this print which numbers 
        
    return f'Not found yet'

print(sub_Array_Sum([1, 4, 20, 3, 10, 5], 33))
