import discord
from discord import app_commands
from helper_functions import *
from responses import *

class fog_whisperer(discord.Client):
    
    def __init__(self, guild_id):
        self.guild_id = guild_id
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.synced = False
        self.tree = app_commands.CommandTree(self) 
        self.create_slash_commands()

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync(guild=discord.Object(id=self.guild_id))
            self.synced = True
        print(f"We have logged in as {self.user}.")

    async def on_message(self, message_object):
        if message_object.author == self.user:
            return
            
        username = str(message_object.author)
        user_message = str(message_object.content)
        channel = str(message_object.channel)

        print (f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:] 
            await send_message(message_object, user_message, is_private=True)
        elif user_message[0:4] == '!fw-' or user_message[0:1] == '/':
            message_to_send = handle_response(message_object) 
            await send_message(message_object, message_to_send, is_private=False)
        else:
            print('Not Related To Me')
    
    def create_slash_commands(self):
        @self.tree.command(name="wikiinfo", description="Find information for dbd related topic", guild=discord.Object(id=self.guild_id))
        async def wikiinfo_command(interaction: discord.Interaction, name: str):
            response_message = perkWiki(name)
            await interaction.response.send_message(response_message)

        # @self.tree.command(name="dupa", description="Find information for dupa related topic", guild=discord.Object(id=self.guild_id))
        # async def dupa_command(interaction: discord.Interaction, name2: str):
        #     response_message = "gowniany temat"
        #     await interaction.response.send_message(response_message)    