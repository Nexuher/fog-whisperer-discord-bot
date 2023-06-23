import random
import discord 
import bot

def on_message(message): 
    username = message.author.display_name # Retrieving username

    response = (f'Welcome {username}!\nMy name is Fog Whisperer and I will be assisting you in your gameplay in Dead By Daylight!')
    return response 

def randSurvPerksDefault(message):
    username = message.author.display_name # Retrieving username
    response = "List of the perks for this match: \n"

    possibleResponses = [
        'Dark Sense',
        'Déjà Vu',
        'Guardian',
        'Hope',
        'Inner Healing',
        'Kindred',
        'Kinship',
        'Lightweight',
        'No One Left Behind',
        'Plunderer`s Instinct',
        'Premonition',
        'Renewal',
        'Resilience',
        'Self-Aware',
        'Situational Awareness',
        'Slippery Meat',
        'Small Game',
        'Spine Chill',
        'This Is Not Happening',
        'We`ll Make It'
    ]

    for x in range(4):
        perkNumber = random.randint(0, len(possibleResponses) - 1)
        response += possibleResponses[perkNumber] + "\n"
        x += 1

    return response

def handle_response(message) -> str:
    p_message = message.content.lower()

    if p_message == '!fw-hello':
        return 'Hey There!'
    
    if p_message == '!fw-roll':
        return str(random.randint(1,6))
    
    if p_message == '!fw-roll-4':
        returnValue = ""

        for x in range(6):
            randNumber =  str(random.randint(1,6))
            returnValue += randNumber + " "
            x += 1

        return returnValue    
        
    if p_message == '!fw-help':
        return on_message(message)

    if p_message == '!fw-randsurvperksdefault':
        return randSurvPerksDefault(message)
    
    return 'incorrect command'