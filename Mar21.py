import json
import requests

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
ottawa_dict = ottawa_wards_response.json()

for item in ottawa_dict['objects']:
    print(item["name"])

response = requests.get('https://represent.opennorth.ca/candidates')
dicto = response.json()

for candidate in dicto["objects"]:
    first_name = candidate["first_name"]
    last_name = candidate["last_name"]
    print('{},{}'.format(last_name, first_name))
