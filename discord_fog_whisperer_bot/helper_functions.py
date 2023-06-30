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

def read_guild_id(server_name):
    f = open("C:\\discord_bot_token\\token.json")

    data = json.load(f)
    guild_id = data["guild_ids"][server_name]
    
    print("Read guild_id: " + str(guild_id))

    return guild_id       