array = [16,17,4,5,2]

def leaderOfArray(array,length):
    leader = []     #create empty list
    currentMAX = array[-1]     #Target Last index 
    leader.append(currentMAX)    #last index number append to leader array


    for i in range(length-2,-1,-1): #loop length last number start and end -1
        if array[i] >= currentMAX:   # if greater than currentMAX
            leader.append(array[i])  # that array append to leader
            currentMAX = array[i]  # add to currentMAX
    return leader[::1]  # return last number to

print(leaderOfArray(array,len(array)))
