import discord
import responses
import json

async def send_message(original_message, message_to_send, is_private):
    try:
        await original_message.author.send(message_to_send) if is_private else await original_message.channel.send(message_to_send)
    except Exception as e:
        print(e)

def read_token():
    f = open("C:\\discord_bot_token\\token.json")

    data = json.load(f)
    token = data["token"]
    
    print("Read token: " + token)

    return token

def run_bot():
    TOKEN = read_token()

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message_object):
        if message_object.author == client.user:
            return
        
        username = str(message_object.author)
        user_message = str(message_object.content)
        channel = str(message_object.channel)

        print (f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:] 
            await send_message(message_object, user_message, is_private=True)
        elif user_message[0] == '!':
            message_to_send = responses.handle_response(message_object) 
            await send_message(message_object, message_to_send, is_private=False)
        else:
            print('Skipping message')

    client.run(TOKEN)    