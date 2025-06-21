def find_anagram(str1,str2):
    if len(str1) != len(str2):
        return False   #if the character not same output will be false
    
    dict1 = {}
    dict2 = {}

    for i in str1:
        if i in dict1:
            dict1[i]+=1  #If the character is already in the dictionary, increment its count by 1.
        else:
            dict1[i] = 1  #If not, add the character to the dictionary with a count of 1.
    for j in str2:
        if j in dict2 :
            dict2[j] +=1
        else:
            dict2[j] = 1
    return dict1 == dict2

print(find_anagram("anagram","nagaram"))