list1 = []
dict1 = {
    'low' : [23.65, 3451],
    'medium' : [66.32,9841],
    'high' : [652.32, 325],
    }

for x in dict1.values():
    list1.append(x)    


# here maybe a loop that's it
dict1['low'] = sum(list1[0][0:])
dict1['medium'] = sum(list1[1][0:])
dict1['high'] = sum(list1[2][0:])
  
list1.clear()

for item in dict1.items():
    list1.append(item)
    
print(list1)

# 10/10