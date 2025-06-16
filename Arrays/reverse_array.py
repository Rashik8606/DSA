arrays = [1,2,4,5,7,8,3,70,54,55,-66,7,8,9]
# reverse = []
# for j in range(len(arrays)-1,-1,-1):  #this will start from last index and go down to 0 back wards
#     reverse.append(arrays[j])
# print(reverse)
    

def reverse_list(lis):
    empty_list = []
    for i in range(len(lis)-1,-1,-1):
        empty_list.append(lis[i])
    return empty_list
print(reverse_list(arrays))