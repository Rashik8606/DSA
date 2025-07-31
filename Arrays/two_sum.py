# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target


lis1 = [1,2,3,4,5,6]
target = 9
def two_Sum(arr1, tar):
    nums = len(arr1)
    i = 0
    while i < nums:
        j = i+1
        while j < nums:
            if arr1[i] + arr1[j] == tar:
                return [i,j]
            j+=1
        i+=1
    return [-1,-1]

print(two_Sum(lis1, target))