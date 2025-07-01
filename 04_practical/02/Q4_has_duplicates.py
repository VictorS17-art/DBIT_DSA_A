numbers= [12,12,34,53]
numbers2= [23,43,56,12,42]
def has_duplicates(lst):
    
     for i in range(len(lst)):  
        for j in range(i + 1, len(lst)): 
            if lst[i] == lst[j]: 
                return True
        return False

print(has_duplicates(numbers))
print(has_duplicates(numbers2))
      