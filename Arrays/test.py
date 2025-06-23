# def find_largest_num(num):
#     max_num = num[0]
#     for i in num:
#         if i > max_num:
#             max_num = i
#     return max_num

# print(find_largest_num([10, 5, 8, 20, 3, 50, 43]))

# def array_sorted_or_not(arr):
#     is_sorted = True
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i]:
#             is_sorted = False
#             break
#     if is_sorted :
#         print('this is sorted !')
#     else:
#         print('this is not sorted !')

# print(array_sorted_or_not([1,2,3,4,5]))

# def reverse_array(arr):
#     set_array = []
#     for i in range(len(arr)-1,-1,-1):
#         set_array.append(arr[i])
#     return set_array

# print(reverse_array([10, 5, 8, 20, 3]))

# def find_min_num(lis):
#     min_list = lis[1]
#     for i in lis:
#         if i < min_list:
#             min_list = i
#     return min_list
# print(find_min_num([10,20,30,5,7]))


# def find_second_largest_num(arr):
#     max_num = float('-inf')
#     min_num = float('-inf')
#     for i in arr:
#         if i > max_num:
#             min_num = max_num
#             max_num = i
#         if i < max_num and i > min_num:
#             min_num = i
#     return min_num

# print(find_second_largest_num([1,2,3,4,5,6,7]))


# def count_even_odd(arr):
#     even = 0
#     odd = 0
#     for i in range(len(arr)):
#         if i %2 == 0:
#             even +=1
#         elif i %2 == 1:
#             odd += 1
#     return f'Even Number is {even} and Odd {odd}'
# print(count_even_odd([1,2,3,4,5,6,7]))


# def sec_largest(arr):
#     largest = float('-inf')
#     sec_smallest = float('-inf')
#     for i in arr:
#         if i > largest:
#             sec_smallest = largest
#             largest = i
#         elif i > sec_smallest and i != largest:
#             sec_smallest = i
#     return f'second largest {sec_smallest}'
# print(sec_largest([1,2,3,4,5,6]))

# def if_array_sorted_or_not(arr):
#     if_sorted = True
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             if_sorted = False
#             break
#     if if_sorted:
#         print(f'Sorted array ')
#     else:
#         print(f'its not sorted array')
#     return if_sorted
# print(if_array_sorted_or_not([3,16,8,4,2]))



# def remove_duplicate(arr):
#     lft = 1
#     for rgt in range(1,len(arr)):
#         if arr[rgt] != arr[lft-1]:
#             arr[lft] = arr[rgt]
#             lft+=1
#     return arr[:lft]

# print(remove_duplicate([1,1,2,2,2,3,3,4,5,6,7,7,7,9,8,8]))


# def search_binary_search(nums, target):
#     left, right, = 0 , len(nums)-1  #fetch first index and last index

#     while left <= right:
#         mid = (left+right)//2
#         if target == nums[mid]: # find target number or not 
#             return mid # then return
        
#         if left <= nums[mid]: # left side number is lessthan middle number 
#             if target < nums[left] or target > nums[mid]: # and target number lessthan left side number or middle number
#                 left = mid+1 # to skip left side
#             else:
#                 right = mid -1 # to skip right side
#         else:
#             if target > nums[right] or target < nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid +1 # if not in the array return -1

#     return -1

# print(search_binary_search([4,5,6,7,0,1,2],1))


# def is_palidrome_check(arr):
#     start = 0
#     end = len(arr)-1

#     while start <= end:
#         if arr[start] != arr[end]:
#             return False
#         else:
#             start +=1
#             end -=1
#     return True
# print(is_palidrome_check('maas'))

# def count_vowels(arr):
#     count = 0
#     consonant = 0
#     for i in range(len(arr)):
#         if arr[i] in 'aeiouAEIOU':
#             count+=1
#         else:
#             consonant+=1
#     return count , consonant
# print(count_vowels('rashiki'))

# def find_anagram(str1,str2):
#     if len(str1) != len(str2):
#         return False
#     dict1 = {}
#     dict2 = {}

#     for i in str1:
#         if i in dict1:
#             dict1[i] +=1
#         else:
#             dict1[i] = 1
#     for i in str2:
#         if i in dict2:
#             dict2[i] +=1
#         else:
#             dict2[i] = 1

#     return dict1 == dict2

# print(find_anagram('listen','silent'))


# def find_anagram_or_not(str1,str2):
#     if len(str1) != len(str2):
#         return False
#     dict1 = {}
#     dict2 = {}

#     for i in str1:
#         if i in dict1:
#             dict1[i] +=1
#         else:
#             dict1[i] = 1
#     for i in str2:
#         if i in dict2:
#             dict2[i] +=1
#         else:
#             dict2[i] = 1
#     return dict1 == dict2

# print(find_anagram_or_not('listen','silent'))


# def find_second_largest(nums):
#     first_largest = float('-inf')
#     second_largest = float('-inf')

#     for i in nums:
#         if i > first_largest:
#             second_largest = first_largest
#             first_largest = i
#         elif i < second_largest and i > first_largest:
#             second_largest = i
#     return f'First largest number is {first_largest} and second number is {second_largest}'
# print(find_second_largest([1,2,3,4,5,6,7,7,7,6,6,4]))


# def remove_duplicates(num):
#     fisrt_largest = float('-inf')
#     second_largest = float('-inf')

#     for i in num:
#         if i > fisrt_largest:
#             second_largest = fisrt_largest
#             fisrt_largest = i

#         elif i < second_largest or i != fisrt_largest:
#             second_largest = i

#     return f' the first largst number is { fisrt_largest} and second largest number is {second_largest}'

# print(remove_duplicates([1,2,3,4,5,6,7]))


# def is_palindrome(arr):
#     left = 0
#     right = len(arr)-1

#     while left < right:
#         if arr[left] != arr[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# string = ['farsana','rashik','maam','manim','akaash','kruk','jeej']
# for i in string:
#     print(f'{i} is {is_palindrome(i)}')

def count_vowls_consonant(arr):
    vowels = 0
    consonant = 0
    for i in range(len(arr)):
        if arr[i] in 'aeiouAEIOU':
            vowels += 1
        elif i:
            consonant +=1
    return vowels, consonant

print(count_vowls_consonant('rashik'))
    