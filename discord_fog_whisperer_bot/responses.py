import random
import discord 
import bot

def on_message(message): 
    username = message.author.mention # Retrieving username

    response = (f'**Welcome {username}!**\n\nMy name is Fog Whisperer and I will be assisting you in your gameplay in Dead By Daylight!\n\nYou can use me by starting the command with "**!fw-**" and following it with you request, my current commands are:\n<---------- Simple Commands ---------->\n-> hello\n-> roll\n-> roll-4\n <---------- Game Related Commands ----------> \n-> randSurvPerksDefault\n-> randKillerPerksDefault\n-> RandBuildSurvivor\n-> RandBuildKiller\n<---------- Creation Related ---------->\n-> Wiki\n\nGo ahead! Try asking me to `!fw-roll`, please keep in mind that Im still in development, which means that some bugs might occur\n\n**See you in the fog!**')    
    return response 

def randSurvPerksDefault(message):
    username = message.author.mention # Retrieving username
    
    response = (f"{username} List of the Surv perks for this match: \n")

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
        sizeAfterDeleting = len(possibleResponses) - 1

        perkNumber = random.randint(0, sizeAfterDeleting) # Randomising a number in list, to pick a perk

        response += "-> " + possibleResponses[perkNumber] + "\n"

        possibleResponses.remove(possibleResponses[perkNumber]) # Removing added items in case the number would duplicate
        sizeAfterDeleting -= 1

        x += 1

    return response

def randKillerPerksDefault(message):
    username = message.author.mention # Retrieving username
    
    response = (f"{username} List of the Killer perks for this match: \n")

    possibleResponses = [
        'Bitter Murmur',
        'Claustrophobia',
        'Deerstalker',
        'Distressing',
        'Fearmonger',
        'Hex: No One Escapes Death',
        'Hex: Thrill of the Hunt',
        'Insidious',
        'Iron Grasp',
        'Jolt',
        'Monstrous Shrine',
        'Scourge Hook',
        'Shattered Hope',
        'Sloppy Butcher',
        'Spies from the Shadows',
        'Unrelenting',
        'Whispers',
    ]

    for x in range(4):
        sizeAfterDeleting = len(possibleResponses) - 1

        perkNumber = random.randint(0, sizeAfterDeleting) # Randomising a number in list, to pick a perk

        response += "-> " + possibleResponses[perkNumber] + "\n"

        possibleResponses.remove(possibleResponses[perkNumber]) # Removing added items in case the number would duplicate
        sizeAfterDeleting -= 1

        x += 1

    return response

def Wiki(message):
    username = message.author.mention # Retrieving username
    response = (f"{username} \n\nEverything about Dead By Daylight is coming straight from the game's wiki: https://deadbydaylight.fandom.com/wiki/Dead_by_Daylight_Wiki")
    return response

def perkList():
    response = ""

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
        sizeAfterDeleting = len(possibleResponses) - 1

        perkNumber = random.randint(0, sizeAfterDeleting) # Randomising a number in list, to pick a perk

        response += "-> " + possibleResponses[perkNumber] + "\n"

        possibleResponses.remove(possibleResponses[perkNumber]) # Removing added items in case the number would duplicate
        sizeAfterDeleting -= 1

        x += 1

    return response

def perkListKiller():
    response = ""

    possibleResponses = [
        'Bitter Murmur',
        'Claustrophobia',
        'Deerstalker',
        'Distressing',
        'Fearmonger',
        'Hex: No One Escapes Death',
        'Hex: Thrill of the Hunt',
        'Insidious',
        'Iron Grasp',
        'Jolt',
        'Monstrous Shrine',
        'Scourge Hook',
        'Shattered Hope',
        'Sloppy Butcher',
        'Spies from the Shadows',
        'Unrelenting',
        'Whispers',
    ]

    for x in range(4):
        sizeAfterDeleting = len(possibleResponses) - 1

        perkNumber = random.randint(0, sizeAfterDeleting) # Randomising a number in list, to pick a perk

        response += "-> " + possibleResponses[perkNumber] + "\n"

        possibleResponses.remove(possibleResponses[perkNumber]) # Removing added items in case the number would duplicate
        sizeAfterDeleting -= 1

        x += 1

    return response


def randBuildSurvDefault(message):
    survivorList = [
        "Dwight Fairfield",
        "Meg Thomas",
        "Claudette Morel",
        "Jake Park",
        "Nea Karlsson",
        "Laurie Strode",
        "Ace Visconti",
        "William Bill Overbeck",
        "Feng Min",
        "David King",
        "Quentin Smith",
        "Detective David Tapp",
        "Kate Denson",
        "Adam Francis",
        "Jeffrey Jeff Johansen",
        "Jane Romero",
        "Ashley J. Williams",
        "Nancy Wheeler",
        "Steve Harrington",
        "Yui Kimura",
        "Zarina Kassir",
        "Cheryl Mason",
        "Felix Richter",
        "Élodie Rakoto",
        "Yun-Jin Lee",
        "Jill Valentine",
        "Leon S Kennedy",
        "Mikaela Reid",
        "Jonah Vasquez",
        "Yoichi Asakawa",
        "Haddie Kaur",
        "Ada Wong",
        "Rebecca Chambers",
        "Vittorio Toscano",
        "Thalita Lyra",
        "Renato Lyra",
        "Gabriel Soma",
    ]

    item_list = [
        "No Item"
        "Toolbox",
        "Flashlight",
        "Map",
        "Medkit",
    ]

    rarity_list = [
        "Grey",
        "Yellow",
        "Green",
        "Purple",
    ]

    chosenSurvivor = survivorList[random.randint(1, len(survivorList) - 1)]
    chosenItem = item_list[random.randint(1, len(item_list) - 1)]
    chosenRarity = rarity_list[random.randint(1, len(rarity_list) - 1)]

    if chosenItem == "No Item":
        chosenRarity= "No item, then no addons duh ¯\_(ツ)_/¯"

    response = (f"**Character**: {chosenSurvivor}\n**Perks**:\n{perkList()}\n**Item**: {chosenRarity} {chosenItem}\n**Addons**: {chosenRarity} {rarity_list[random.randint(1, len(rarity_list) - 1)]}")

    return response

def randBuildKillerDefault(message):

    killerList = [
        "Trapper",
        "Wraith",
        "Hillbily",
        "Nurse",
        "Shape",
        "Hag",
        "Doctor",
        "Huntress",
        "Cannibal",
        "Nightmare",
        "Pig",
        "Clown",
        "Spirit",
        "Legion",
        "Plague",
        "Ghost Face",
        "Demogorgon",
        "Oni",
        "Deathslinger",
        "Executioner",
        "Blight",
        "Twins",
        "Trickster",
        "Nemesis",
        "Cenobite",
        "Artist",
        "Onryo",
        "Dredge",
        "Mastermind",
        "Knight",
        "Skull Merchant",
        "Singularity",
    ]

    rarity_list = [
        "Grey",
        "Yellow",
        "Green",
        "Purple",
    ]

    chosenKiller = killerList[random.randint(1, len(killerList) - 1)]
    chosenRarity = rarity_list[random.randint(1, len(rarity_list) - 1)]

    response = (f"**Character**: {chosenKiller}\n**Perks**:\n{perkListKiller()}\n**Addons**: {chosenRarity} {rarity_list[random.randint(1, len(rarity_list) - 1)]}")

    return response

def handle_response(message) -> str:
    p_message = message.content.lower()

    match p_message:
        case '!fw-hello':
            return 'Hey There!'
        
        case '!fw-roll':
            return str(random.randint(1,6))
        
        case '!fw-roll-4':
            returnValue = ""

            for x in range(6):
                randNumber =  str(random.randint(1,6))
                returnValue += randNumber + " "
                x += 1

            return returnValue  
        
        case '!fw-help':
            return on_message(message)
        
        case '!fw-randsurvperksdefault':
            return randSurvPerksDefault(message)
        
        case '!fw-randkillerperksdefault':
            return randKillerPerksDefault(message)
        
        case '!fw-wiki':
            return Wiki(message)
        
        case '!fw-randbuildsurvivor':
            return randBuildSurvDefault(message)
        
        case '!fw-randbuildkiller':
            return randBuildKillerDefault(message)
    
    return 'incorrect command'