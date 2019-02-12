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


if ans1 >= 4 and ans2 < 4 and ans3 < 4:
    print("I would recommend {}".format(doc))
elif ans1 >= 4 and ans2 >= 4 and ans3 < 4:
    print("I would recommend {}, and {}".format(doc, drama))
elif ans1 < 4 and ans2 >= 4 and ans3 >= 4:
    print("I would recommend {}".format(dramed))
elif ans1 < 4 and ans2 >= 4 and ans3 < 4:
    print("I would recommend {}".format(drama))
elif ans1 < 4 and ans2 < 4 and ans3 >= 4:
    print("I would recommend {}".format(comedy))
elif ans1 < 4 and ans2 < 4 and ans3 < 4:
    print("Try reading A Game of Thrones instead!")
else:
    print("You're way to picky for this program")
