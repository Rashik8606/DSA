target_num = 20
array = [10,120,20,30,40,50]

def targeted_Number(tar, arr):
    for i in range(len(arr)):
        if arr[i] == tar:
            return i
    return f'Its not here'

print(targeted_Number(target_num,array))