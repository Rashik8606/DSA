def reversed_string(str1):
    reversed_str = ''  #empty str
    i = len(str1)-1 # start with end
    while i >= 0: # end to start
        reversed_str = reversed_str + str1[i]  
        i = i-1  # increase end to start
    return reversed_str
print(reversed_string('rashik'))