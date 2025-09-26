def largest_number_smallest_number(arr):
    result = arr.sort()

    smallest = arr[0]
    largest = arr[-1]

    return smallest, largest

lis = [1,28,34,67,89,43,90]
print(largest_number_smallest_number(lis))