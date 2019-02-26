
new = { 'data': { 'rooms':
    [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 }, { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],
    'events': [
      { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
      { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
      { 'id': 3, 'room_id': 1, 'start_time': 11, 'end_time': 18, 'attendees': 20 },
      { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}

room201_cap = new['data']['rooms'][0]['capacity']
room201_id = new['data']['rooms'][0]['id']

events_sched = new['data']['events']
# print(events_sched)

for item in events_sched:
    if item['room_id'] == room201_id:
        if item['attendees'] <= room201_cap:
            print("Room is Ok for event at {}".format(item['start_time']))
        else:
            print("Room too small ")
