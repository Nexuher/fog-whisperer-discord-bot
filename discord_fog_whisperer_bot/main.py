import helper_functions
from helper_functions import *
from fog_whisperer import fog_whisperer

if __name__ == '__main__':
    guild_id = read_guild_id("development_server")
    token = read_token()
    fw = fog_whisperer(guild_id)       

    fw.run(token)