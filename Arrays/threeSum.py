# three sum – find all triplets that sum to zero
array = [-1,0,1,2,-1,-4]   # output will be [-1,-1,2],[-1,0,1]
array1 = [0,1,1]   # output will be []
array2 = [0,0,0]   # output will be [[0,0,0]]

target = 0

def threeSum(array, target=0):
    empty_list = []
    array = sorted(array)   
    nums = len(array)

    for i in range(nums):
        if array[i] > 0:
            break
        if i > 0 and array[i] == array[i-1]:
            continue

        low = i+1
        high = nums -1

        while low < high:
            currentSum = array[i] + array[low] + array[high]
            if currentSum == 0:
                empty_list.append([array[i], array[low], array[high]])
                low+=1
                high-=1
                while low < high and array[low] == array[low-1]:
                    low +=1
                while low < high and array[high] == array[high +1]:
                    high -=1
            elif currentSum > 0:
                low +=1
            else:
                high -=1
    return empty_list
            

print(threeSum(array,target))
print(threeSum(array1,target))
print(threeSum(array2,target))

