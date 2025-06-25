# three sum – find all triplets that sum to zero
array = [-1,0,1,2,-1,-4]   # output will be [-1,-1,2],[-1,0,1]
array1 = [0,1,1]   # output will be []
array2 = [0,0,0]   # output will be [[0,0,0]]

target = 0

def threeSum(array, target):
    result_arr = []
    array.sort()
    num = len(array)

    for i in range(num):
        if array[i] > 0 :  # break early — because all future numbers will be positive, and the sum can't be 0.
            break
        if i > 0 and array[i] == array[i-1]:  #  skip to avoid duplicates.
            continue
        
        low = i+1
        high = num-1

        while low < high :
            currentSum = array[i] + array[low] + array[high]
            if currentSum == 0:
                result_arr.append([array[i], array[low], array[high]])
                low +=1
                high -=1

                while low < high and array[low] == array[low-1]:
                    low +=1
                while low < high and array[high] == array[high+1]:
                    high -=1
            elif currentSum < 0:
                low +=1
            else:
                high -=1

    return result_arr

print(threeSum(array,target))
print(threeSum(array1,target))
print(threeSum(array2,target))

