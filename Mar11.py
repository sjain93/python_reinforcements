test = {}
keys =  list(range(1,51))

for element in keys:
    if element%2 == 0 and element%7 == 0:
        test[element] = element*2
    elif element%2 == 0:
        test[element] = (element + 1)
    elif element%7 == 0:
        test[element] = (element - 1)
    else:
        test[element] = element

print(test)
