lis1 = [5,7,6,2,3,1,4]
def bubble_sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num
print(bubble_sort(lis1))