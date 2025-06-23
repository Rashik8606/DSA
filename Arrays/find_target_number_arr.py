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

#Find if a pair exists with a given sum in an array

def if_pair_exists(arr,targetSum):  # init arr and target 
    seenNumber = []   # empty list 
    for i in range(len(arr)):  # range of arr list 
        difference = targetSum - arr[i]  # difference between target number and seenNumber list 
        if difference in seenNumber:  # if in print true 
            return True
        else:  # if not in append seenNumber list 
            seenNumber.append(arr[i])
    return False

print(if_pair_exists([10, 15, 3, 7],17))


# Count all pairs with a given sum
def count_pair(arr,target): # init arr and target
    count_number = 0  # create 0 
    seenNumber = []  # create empty list

    for i in range(len(arr)):  # length of arr
        difference = target - arr[i]  # difference between target and arr

        for j in range(len(seenNumber)):  # length of seenNumber list 
            if seenNumber[j] == difference:  # if there count number increase
                count_number +=1  # increment
        
        seenNumber.append(arr[i])  # else append arr if i [this append all index]
        
    return count_number  # return count number 

print(count_pair([1, 5, 7, -1, 5],6))




