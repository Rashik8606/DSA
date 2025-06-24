# find two sum from target array 
def twoSumArray(array, target):
    empty_array = []

    for i in range(len(array)):
        current =  array[i]
        difference = target - current

        if difference in empty_array:
            return current, difference
        else:
            empty_array.append(array[i])

    return empty_array

print(twoSumArray([3,4,5,8,7,6],13))