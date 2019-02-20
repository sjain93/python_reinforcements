def odd_sum_return(num_list):
    odd_sum = 0
    for number in num_list:
        if number%2 != 0:
            odd_sum += number
    return odd_sum

test = [0,1,2,3,4,5,6]
print(odd_sum_return(test))
