def count_even_odd(arr):
    even = 0
    odd = 0
    for i in range(len(arr)):
        if i %2 == 0:
            even +=1
        elif i %2 == 1:
            odd +=1
    return f'Even {even} Odd {odd}'

print(count_even_odd([1,2,3,4,5,6,7]))