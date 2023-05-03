list1 = []
dict1 = {
    'low' : [23.65, 3451],
    'medium' : [66.32,9841],
    'high' : [652.32, 325],
    }

for key, value in dict1.items():
    my_tup = (key, sum(value))
    list1.append(my_tup)


print(list1)