#Ex 1
def odd_sum_return(num_list):
    odd_sum = 0
    for number in num_list:
        if number%2 != 0:
            odd_sum += number
    return odd_sum

test = [0,1,2,3,4,5,6]
print(odd_sum_return(test))

#Ex 2

name_list = ["James", "Harry", "Lily"]

print("Please input a name and I shall check and see if the name is part of the list")
query = str(input())

for item in name_list:
    if query == item:
        print("Hello {}".format(query))
        break
    else:
        print("Who goes there?")
        break
