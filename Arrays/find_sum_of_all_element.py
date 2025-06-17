def find_sum(num):
    sum_num = 0
    for i in range(len(num)):
        sum_num = sum_num + num[i]
    return sum_num

print(find_sum([10, 5, 8, 20, 3]))