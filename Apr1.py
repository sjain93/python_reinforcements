import math
def luckCheck(str):
    first_half = 0
    second_half = 0
    if len(str)%2 == 0:
        countLimit = int(len(str)/2)
        for number in range(0, countLimit):
            first_half += int(str[number])
        for number in range(countLimit, len(str)):
            second_half += int(str[number])
    else:
        midIndex = math.ceil(len(str)/2) - 1
        for number in range(0, midIndex):
            first_half += int(str[number])
        for number in range(midIndex+1, len(str)):
            second_half += int(str[number])

    if first_half == second_half :
        print(True)
    else:
        print(False)

luckCheck('003111223') #False
luckCheck('003111') #True
luckCheck('17935') #True
