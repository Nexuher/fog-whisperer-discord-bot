import discord
import welcoming_messages
import random
from helper_functions import *
from responses import *
from threading import Thread
from discord.ext import commands, tasks

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!fw-', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

    channel_id = read_guild_id("working_commands")
    channel = bot.get_channel(channel_id)
    await channel.send(f"{welcoming_messages.response}")

    send_standalone_message_loop.start()


@bot.event
async def on_command_error(ctx, error):
    print(f"Incorrent command: {error}")


@bot.command(name="wikiinfo")
async def wikiinfo(ctx, wiki_entry: str):
    response_message = perkWiki(wiki_entry)
    await ctx.send(response_message)


@bot.command(name="hello")
async def wikiinfo(ctx):
    await ctx.send('Hey There!')


@bot.command(name="roll")
async def roll(ctx):
    await ctx.send(str(random.randint(1,6)))


@bot.command(name="help_message")
async def help_message(ctx):
    await ctx.send(help(ctx))


@bot.command(name="roll-4")
async def roll_4(ctx):
    await ctx.send(str(random.randint(1,6)))
    

@bot.command(name="randSurvPerksDefault")
async def randSurvPerksDef(ctx):
    await ctx.send(randSurvPerksDefault(ctx))


@bot.command(name="randKillerPerksDefault")
async def randKillerPerksDef(ctx):
    await ctx.send(randKillerPerksDefault(ctx))


@bot.command(name="Wiki")
async def WikiWeb(ctx):
    await ctx.send(Wiki(ctx))


@bot.command(name="randBuildSurvivor")
async def randBuildSurv(ctx):
    await ctx.send(randBuildSurvivor(ctx))


@bot.command(name="randBuildKiller")
async def randBuildKillerr(ctx):
    await ctx.send(randBuildKiller(ctx))


@bot.command(name="randMapOffering")
async def randMapOffer(ctx):
    await ctx.send(randMapOffering(ctx))


@bot.command(name="add_reminder")
async def add_reminder(ctx, year: str, month: str, day: str, hour: str, minute: str, info: str):
    result = add_new_reminder(ctx, year, month, day, hour, minute, info)
    await ctx.send("New reminder added")    


@bot.command(name="perkWiki")
async def perkWiki(ctx, wiki_entry: str):
    await ctx.send(perkWiki(wiki_entry))   


@bot.command(name="read_reminders")
async def read_all_reminders(ctx):
    try:
        all_reminders = reminder.read_reminders(ctx)
        user_name = ctx.author.mention

        await ctx.send(f"# Reminders for: {user_name}\n ## Time / Info / Id \n{all_reminders}\n")
    except Exception as Error:
        raise Exception(f"Error: {Error}").with_traceback(Error.__traceback__)   

@bot.command(name="delete_reminder")
async def delete_reminder(ctx, identificator: str):
    try:
        await ctx.send(reminder.delete_reminder_data(ctx.author.display_name, identificator))
    except Exception as Error:
        await ctx.send(f"Error while deleting a reminder: {Error}")    

#Command made purely for testing the ID creation

@bot.command(name="create_id")
async def create_id(ctx):
    await ctx.send(reminder.get_random_id())    


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@tasks.loop(seconds=10)
async def send_standalone_message_loop():
    try:
        reminders_to_send = reminder.check_reminder_timers()
    except Exception as Error:
        print(Error)
        return

    for reminder_data in reminders_to_send:
        channel = bot.get_channel(reminder_data["channel_id"])
        
        if channel:
            user_name = reminder_data["name"]
            reminder_info = reminder_data["info"]
            await channel.send(f":warning: Reminder set by @{user_name}: {reminder_info} :warning:")


bot.run(read_token())