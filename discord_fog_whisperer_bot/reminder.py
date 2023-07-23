import json
import os
import random
import time
import asyncio
import string
import secrets
import testing.test_data as test_data
from datetime import datetime, timedelta
from responses import * 

'''
+ przyjmowac od usera date(rok,miesiac,dzien,godzina,minuta) i nazwe eventu
+ 1 plik json ktorzy przechowywuje informacje o zapisanych eventach kazdego usera

+ timer ktory co minute wywoluje funkcje sprawdzajaca czy jakis reminder powinien zostac wyslany 

+ randomizowanie id dla kazdego remindera,
+ usuwanie eventu po tym jak sie wykona i opinguje usera1995
+ wypisywanie listy reminderow danego uzytkownika
'''

reminders_file_name = "reminders_event_data.json"
reminder_check_interval_in_seconds = 10


def add_data_to_json(user_name, reminder_date, reminder_info, user_id, channel_id):
    
    # Check if the file exists
    if os.path.exists(reminders_file_name) and os.path.getsize(reminders_file_name) > 0:
        # Load the existing JSON data from the file
        with open(reminders_file_name) as file:
            data = json.load(file)
    else:
        # Create a new empty data dictionary
        data = {}

    new_reminder_id = get_random_id()
    
    # Check if the user already exists in the data dictionary
    if user_name in data:
        # Existing user data
        existing_user_data = data[user_name]

        new_event_data = { 
            "date": reminder_date,
            "info": reminder_info,
            "channel_id": channel_id
        }
        
        # Append a value to reminder_events
        existing_user_data["reminder_events"][new_reminder_id] = new_event_data
    else:
        new_user_data = {
            "name": user_name,
            "user_id" : user_id,
            "reminder_events": {
                new_reminder_id: {
                    "date": reminder_date,
                    "info": reminder_info,
                    "channel_id": channel_id
                }
            }
        }

        data[user_name] = new_user_data

    # Save the updated data to the JSON file
    with open(reminders_file_name, 'w') as file:
        json.dump(data, file, indent=4, default=str)


def verify_date_input(year, month, day, hours, minutes):

    current_date = datetime.now()
    current_year = current_date.year

    year = int(year)
    month = int(month)
    day = int(day)
    hours = int(hours)
    minutes = int(minutes)

    if year < current_year or month < 1 or day < 1:
        return False

    current_month = int(current_date.month)

    # check month value
    if month > 12:
        return False
    
    if current_month in (1,3,5,7,8,10,12) and day > 31:
        return False
        
    if current_month in (4,6,9,11) and day > 30:
        return False
        
    if hours > 24:
        return False
    
    if minutes >= 60:
        return False

    return True


def delete_reminder_data(user_name, identificator):

    reader_file = open(reminders_file_name, "r")
    data = json.load(reader_file)
    
    try:
        user_section = data[user_name]
    except Exception as UserDoesNotExists:
        raise Exception("User does not exists in reminder_data").with_traceback(UserDoesNotExists)
    
    all_user_reminders = data[user_name]["reminder_events"]
    reminder_to_delete = all_user_reminders[identificator]

    if reminder_to_delete is None:
        print("Reminder does not exist thus cannot be deleted. To be or not to be. This is the question.")
        return
    
    # remove element of dictionary with key that is identifier of reminder
    all_user_reminders.pop(identificator)

    # override the all_user_reminder in data
    data[user_name]["reminder_events"] = all_user_reminders

    # Save the updated data to the JSON file
    with open(reminders_file_name, 'w') as file:
        json.dump(data, file, indent=4, default=str)

    return f"Reminder of identificator {identificator} was succesfully deleted"    
            

def get_random_datetime():
    # Define the start and end dates for the range
    now = datetime.now() + timedelta(minutes=1) 
    start_date = datetime(now.year, now.month, now.day, now.hour, now.minute)
    now += timedelta(minutes=5) 
    end_date =   datetime(now.year, now.month, now.day, now.hour, now.minute)

    # Generate a random timedelta within the range
    random_timedelta = random.randint(0, int((end_date - start_date).total_seconds()))
    random_date = start_date + timedelta(seconds=random_timedelta)

    input_date = datetime(random_date.year, random_date.month, random_date.day, random_date.hour, random_date.minute, 0)

    return input_date


def check_reminder_timers():
    reader_file = open(reminders_file_name, "r")
    
    try:
        data = json.load(reader_file)
    except Exception as Error:
        raise Exception("File is empty, no reminders to check").with_traceback(Error.__traceback__)
    
    reminders_to_send = []

    current_date = datetime.now().replace(second=0, microsecond=0)

    print("\n-----------------------------------")
    print(f"Checking at: {current_date}")
    
    for user_data in data:

            for reminder_key in data[user_data]['reminder_events']:
                
                reminder = data[user_data]['reminder_events'][reminder_key]
                reminder_date = datetime.strptime(reminder['date'], '%Y-%m-%d %H:%M:%S').replace(second=0, microsecond=0)

                if current_date == reminder_date:
                    reminders_to_send.append({"name": data[user_data]['name'], "channel_id": reminder['channel_id'], "info": reminder['info']})

                    print(f"Reminding user {data[user_data]['name']} about a reminder: {reminder['info']}")

                    delete_reminder_data(user_data, reminder_key)
                
    return reminders_to_send


def post_on_channel(discord_client, user_id, user_reminder_info, channel_id):
    message = f"Reminding user @{user_id}"
        
    target_channel_id = int(channel_id)
    target_channel = discord_client.get_channel(target_channel_id)
    asyncio.run(target_channel.send(message))

    
def read_reminders(message):
    all_reminder = []
    reminder_date = []
    reminder_info = []
    reminder_identificator = []
    addition_to_reminder_disc = ''

    reminder_number = 1

    caller_name = message.author.display_name

    reader_file = open(reminders_file_name, "r")
    
    try:
        data = json.load(reader_file)
    except Exception as Error:
        raise Exception("File is empty, no reminders to check").with_traceback(Error.__traceback__)

    caller_data = data[caller_name]

    reminder_data = caller_data["reminder_events"]
        
    for reminder_id in reminder_data:
        reminder = reminder_data[reminder_id]

        reminder_identificator.append(reminder_id)
        reminder_date.append(str(reminder["date"]))
        reminder_info.append(str(reminder["info"]))

    if not reminder_data:
        raise Exception("No reminders to check, maybe add some?")

    for reminder_number in range(len(reminder_data)):
        addition_to_reminder_disc += f"⏰ *{reminder_date[reminder_number]}*:    **{reminder_info[reminder_number]}**    ||{reminder_identificator[reminder_number]}||\n"
        
        reminder_number += 1   

    return addition_to_reminder_disc        


def create_datetime(year, month, day, hour, minute):

    success = verify_date_input(year, month, day, hour, minute)

    if not success:
        raise ValueError("Incorrect date")

    return datetime(int(year), int(month), int(day), int(hour), int(minute))


def run_reminder_on_loop(discord_client):
    
    while True:
        check_reminder_timers(discord_client)
        time.sleep(reminder_check_interval_in_seconds)


def get_random_id(id_digits = 16):
    identificator =  ''
    letters_string = string.ascii_letters + string.digits

    for letter in range(id_digits):
        identificator += ''.join(secrets.choice(letters_string))

    return identificator

    
# Main used for testing data 
# before it was going to become a bot command
def main():
    add_data_to_json("x", get_random_datetime(), test_data.descriptions[random.randint(0, len(test_data.descriptions) - 1)])
    add_data_to_json("xy", get_random_datetime(), test_data.descriptions[random.randint(0, len(test_data.descriptions) - 1)])
    add_data_to_json("xz", get_random_datetime(), test_data.descriptions[random.randint(0, len(test_data.descriptions) - 1)])
    add_data_to_json("x2", get_random_datetime(), test_data.descriptions[random.randint(0, len(test_data.descriptions) - 1)])
    add_data_to_json("xa", get_random_datetime(), test_data.descriptions[random.randint(0, len(test_data.descriptions) - 1)])
    add_data_to_json("xd", get_random_datetime(), test_data.descriptions[random.randint(0, len(test_data.descriptions) - 1)])