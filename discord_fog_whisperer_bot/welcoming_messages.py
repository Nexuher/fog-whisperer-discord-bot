import random

welcoming_messages = [
    "Ready to serve"
    "Time to get left on hook again, wait was I supposed to say that?",
    "You still play that game?",
    "Can't wait to get tunneled again",
    "Another day, Another mori",
    "Wanderer Fog Ready To Help!",
    "Maybe go play something else,\ndoesn't matter, ready to help!",
    "Alexa, how do I uninstall Dead By Daylight?",
    "Please god no RPD today",
    "I was supposed to say something here, but I forgot",
    "Slay team is on it again, and I'm all for it!",
    "Please god BHVR, give us good masks this year",
    "Can't wait to get restarted again and again because someone can't code in asyncio",
    "Jane Romero driving skills got you here or you're playing that game?",
    "Alexa, how do I make a discord bot say something?",
    "Here cause of battlepass",
    "Alexa, how do I code in asyncio?",
    "Maybe go play Valorant?",
    "Ever wondered what you can find outside of the camp?",
    ''' :notes: Take all that you want from me
        Try and leave me with nothin'
        That shit don't faze meee
        What kind of girl you take me for? :notes:
        
        I don't need your petty company
        Least I know you're good for somethin'
        You entertain me
        Go on and entertain me, boy :notes: ''',
]

chosen_response_number = random.randint(1, len(welcoming_messages) - 1)

response = welcoming_messages[chosen_response_number]