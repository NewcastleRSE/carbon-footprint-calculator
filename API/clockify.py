import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
Workspace_ID = os.getenv("Workspace_ID")
BASE_URL = 'https://api.clockify.me/api/v1'
headers = {
    'X-Api-Key': API_KEY
}

"""
stringSplit: This function is meant to split the given string
into a list of strings removing all invalid letters. 

sample input - "PT123H456M78S"
sample output - ["123", "456", "78"]
"""
def stringSplit(duration):
    # The translation table replaces all characters in a given string with spaces
    translation_table = str.maketrans("PTHMS", "     ") # (old_str, new_str)
    translated_string = duration.translate(translation_table)
    times = translated_string.strip().split(" ")

    return times


"""
calcEfficiency: This function is meant to calculate the average wattage per hour
on all projects. 

sample input - (a dict of projects with attributes of duration and memberships, 
                a dict of userId's and their corresponding computer wattage
sample output - null - prints results to terminal
"""
def calcEfficiency(projects, data):
     for project in projects:
         # retrieve the duration of a project - "PT123H456M78S"
        duration = project["duration"]
        timesList = stringSplit(duration)
        # Convert each item of the list into the total minutes of each project
        if len(timesList) == 3:
            hour = int(timesList[0]) * 60
            min = int(timesList[1])
            sec = int(timesList[2]) / 60
            total = hour + min + sec
        elif len(timesList) == 2:
            min = int(timesList[0])
            sec = int(timesList[1]) / 60
            total = min + sec
        else:
            total = int(timesList[0]) / 60

        # calculate the avg wattage per project based on data (specs.json)
        wattage = 0
        users = project["memberships"]
        for user in users:
            if user["userId"] in data:
                wattage += int(data[user["userId"]])
        avg_watt = wattage / len(users)
        print(f" Project name: {project['name']}. Avg wattage per hr: {round(avg_watt * total, 2)}Wh")



response = requests.get(f'{BASE_URL}/workspaces/{Workspace_ID}/projects', headers=headers)
if response.status_code == 200:
    projects = response.json()
    with open("specs.json", mode="r") as file:
        data = json.load(file)
    print("This Script Displays:")
    print("The total amount of watts per hour of each project. (Based on personal devices alone)")
    calcEfficiency(projects, data)
else:
    print(f"Error: {response.status_code} - {response.text}")