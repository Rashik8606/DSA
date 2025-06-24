def twoSum_sorted_arr(array, target):
    left = 0   # left = 0 (points to 2)
    right = len(array)-1   # right = 3 (points to 15)

    while left < right :
        currentSum = array[left] + array[right]
        if currentSum > target:
            right -= 1
        elif currentSum < target:
            left +=1
        else:
            return [left+1,right+1]
    return []
            

print(twoSum_sorted_arr([2,7,11,15],9))