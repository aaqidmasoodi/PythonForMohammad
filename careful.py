list1 = [1,2,3] # mutatate - list are mutable
list_copy = list1.copy()

print(f'ID of list 1: {id(list1)}')
print(f'ID of list 2: {id(list_copy)}')

print(list1)
print(list_copy)


list_copy.append(156)

print(list1)
print(list_copy)
