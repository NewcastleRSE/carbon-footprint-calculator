import json
import requests

API_KEY = "MDA1M2NhY2UtNjM0Mi00ZjM3LTllNDUtODE3ZWNkZmE2ZGE4"
Workspace_ID = "61f3ac40ac897025894b32ca"
BASE_URL = 'https://api.clockify.me/api/v1'
headers = {
    'X-Api-Key': API_KEY
}

def stringSplit(duration):
    translation_table = str.maketrans("PTHMS", "     ")
    translated_string = duration.translate(translation_table)
    times = translated_string.strip().split(" ")

    return times

def calcEfficiency(projects, data):
     for project in projects:
        duration = project["duration"]
        mylist = stringSplit(duration)
        if len(mylist) == 3:
            hour = int(mylist[0]) * 60
            min = int(mylist[1])
            sec = int(mylist[2]) / 60
            total = hour + min + sec
        elif len(mylist) == 2:
            min = int(mylist[0])
            sec = int(mylist[1]) / 60
            total = min + sec
        else:
            total = int(mylist[0]) / 60

        wattage = 0
        users = project["memberships"]
        for user in users:
            if user["userId"] in data:
                wattage += int(data[user["userId"]])
        avg_watt = wattage / len(users)
        print(f" Project name: {project['name']}, Avg wattage per hr: {round(avg_watt * total, 2)}Wh")



response = requests.get(f'{BASE_URL}/workspaces/{Workspace_ID}/projects', headers=headers)
if response.status_code == 200:
    projects = response.json()
    with open("specs.json", mode="r") as file:
        data = json.load(file)
    calcEfficiency(projects, data)
else:
    print(f"Error: {response.status_code} - {response.text}")