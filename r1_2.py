doc = 'Blackfish'
drama = 'Roma'
comedy = 'Airplane'
dramed = 'The Apartment'

print("Do you like Documentaries? Rate between 1-5")
ans1 = float(input())

print("Do you like Drama? Rate between 1-5")
ans2 = float(input())

print("Do you like Comedy? Rate between 1-5")
ans3 = float(input())


if ans1 >= 4:
    print("I would recommend {}".format(doc))
elif ans1 <= 3 and ans2 >= 4 and ans3 >= 4:
    print("I would recommend {}".format(dramed))
elif ans1 < 4 and ans2 >= 4 and ans3 < 4:
    print("I would recommend {}".format(drama))
elif ans1 < 4 and ans2 < 4 and ans3 >= 4:
    print("I would recommend {}".format(comedy))
elif ans1 <= 3 and ans2 <= 3 and ans3 <= 3:
    if (ans1 > ans2) & (ans1 > ans3):
        print("I would recommend {}".format(doc))
    elif (ans2 > ans1) & (ans2 > ans3):
        print("I would recommend {}".format(drama))
    elif (ans3 > ans1) & (ans3 > ans2):
        print("I would recommend {}".format(comedy))
else:
    print("Try reading A Game of Thrones instead!")
