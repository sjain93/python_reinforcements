class_room =[
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]


counter = 0
while counter < len(class_room):
    obj = class_room[counter]
    for index, items in enumerate(obj):
        if items == None:
            seat_num = index + 1
            row_num = counter + 1
            print("Row {} seat {} is free, Do you want to sit there? (y/n)".format(row_num, seat_num))
            ans = input()
            if ans == 'y':
                print("What is your name?")
                name = input()
                obj[index] = name
            else:
                continue
        else:
            continue
    counter +=1

print(class_room)
