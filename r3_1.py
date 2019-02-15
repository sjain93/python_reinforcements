trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]
#1
train_111 = trains[-1]['direction']
#2
freq_80B = trains[-3]['frequency_in_minutes']
#3
train_610 = trains[2]['direction']

#4
northbound = []
for index, train in enumerate(trains):
    if trains[index]['direction'] == "north":
        northbound.append(trains[index]['train'])

# print(northbound)

#5
eastbound = []
for index, train in enumerate(trains):
    if trains[index]['direction'] == "east":
        eastbound.append(trains[index]['train'])

# print(eastbound)

#6
def train_finder(direc):
    bound = []
    for index, train in enumerate(trains):
        if trains[index]['direction'] == direc:
            bound.append(trains[index]['train'])
    print(bound)

train_finder("north")
train_finder("east")

#7
trains[0]['first_departure_time'] = 6
print(trains)
