def count_Of_Vowls(arr):
    count = 0
    consonant = 0
    for i in range(len(arr)):
        if arr[i] in 'aeiouAEIOU':
            count+=1
        else:
            consonant +=1
    return f'Vowels count is {count} and consonant {consonant}'

s =  "racecar", "madam", "hello", "listen", "silent"
for i in s:
    print(count_Of_Vowls(i))


def count_vowls_consontant(exp):
    count = 0
    consonant = 0
    for i in range(len(exp)):
        if exp[i] in 'aeiouAEIOU':
            count+=1
        else:
            consonant +=1
    return count,consonant
print(count_vowls_consontant('rashik'))