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



def remove_duplicate(arr):
    lft = 1
    for rgt in range(1,len(arr)):
        if arr[rgt] != arr[lft-1]:
            arr[lft] = arr[rgt]
            lft+=1
    return arr[:lft]

print(remove_duplicate([1,1,2,2,2,3,3,4,5,6,7,7,7,9,8,8]))
