# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target


lis1 = [1,2,3,4,5,6]
target = 9

def two_Sum(arr1, target):
    nums = len(arr1)
    count_num = 0
    while count_num < nums:
        sec_count_num = count_num + 1
        while sec_count_num < nums:
            if arr1[count_num] + arr1[sec_count_num] == target:
                return [count_num, sec_count_num]
            sec_count_num+=1
        count_num+=1
    return [-1, -1]

print(two_Sum(lis1, target)) 