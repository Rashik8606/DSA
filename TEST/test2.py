array = [2,4,6,7,8,11,13,15]
target = 19

def sorted_array_two_sum(arr,target):
    left = 0
    right = len(arr)-1

    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum > target:
            right -= 1

        elif currentSum < target:
            left += 1
        
        else:
            return [left+1, right+1]
    return []

print(sorted_array_two_sum(array,target))