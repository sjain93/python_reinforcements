doc = 'Blackfish'
drama = 'Roma'
comedy = 'Airplane'
dramed = 'The Apartment'

print("Do you like Documentaries? Y/N")
ans1 = input()
# if ans1 != 'Y' | ans1 != 'N':
#     print("Invalid input")


print("Do you like Drama? Y/N")
ans2 = input()
# if ans2 != 'Y' or ans2 != 'N':
#     print("Invalid input")
# else:
#     continue

print("Do you like Comedy? Y/N")
ans3 = input()
# if ans3 != 'Y' or ans3 != 'N':
#     print("Invalid input")

if ans1 == 'Y' and ans2 == 'N' and ans3 == 'N':
    print("I would recommend {}".format(doc))
elif ans1 == 'Y' and ans2 == 'Y' and ans3 == 'N':
    print("I would recommend {}, and {}".format(doc, drama))
elif ans1 == 'N' and ans2 == 'Y' and ans3 == 'Y':
    print("I would recommend {}".format(dramed))
elif ans1 == 'N' and ans2 == 'Y' and ans3 == 'N':
    print("I would recommend {}".format(drama))
elif ans1 == 'N' and ans2 == 'Y' and ans3 == 'N':
    print("I would recommend {}".format(drama))
elif ans1 == 'N' and ans2 == 'N' and ans3 == 'Y':
    print("I would recommend {}".format(comedy))
elif ans1 == 'N' and ans2 == 'N' and ans3 == 'N':
    print("Try reading A Game of Thrones instead!")
else:
    print("You're way to picky for this program")
