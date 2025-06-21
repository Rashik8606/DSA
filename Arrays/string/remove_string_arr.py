def remove_duplicate_string(arr):
    found = []
    for i in arr:
        if i not in found:
            found.append(i)
    return ''.join(found)
print(remove_duplicate_string('programming'))