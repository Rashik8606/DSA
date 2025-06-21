def is_palindrome_check(arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        if arr[start] != arr[end]:
            return False
        else:
            start +=1
            end -=1
    return True

s = 'maams','farsana','apple','mani','maam','pop','faf'
for i in s: 
    print(is_palindrome_check(i))