numbers = [12, 2, 35, 34, 86]

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

print(linear_search(numbers,34 ))
print(linear_search(numbers,0 ))