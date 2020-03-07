# bot.py
import os
import discord
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

#soup
def getCases():
    url = "https://www.worldometers.info/coronavirus/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    count = soup.find("div", {"class": "maincounter-number"})
    return count.text.strip()

def getDeaths():
    url = "https://www.worldometers.info/coronavirus/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    count = soup.findAll("div", {"class": "maincounter-number"})
    return count[1].text.strip()

def getRecovered():
    url = "https://www.worldometers.info/coronavirus/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    count = soup.findAll("div", {"class": "maincounter-number"})
    return count[2].text.strip()


#bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# !cases command
    total_cases = getCases()
    cases_text = "There are currently " + total_cases + " total cases of Coronavirus worldwide. :mask:"
    if message.content == '!cases':
        response = cases_text

# !deaths command
    total_deaths = getDeaths()
    deaths_text = total_deaths + " people have died from Coronavirus so far. :skull:"
    if message.content == '!deaths':
        response = deaths_text

# !recovered command
    total_recovered = getRecovered()
    recovered_text = total_recovered + " people have recovered from Coronavirus so far. :angel_tone1:"

# !hello command
    shocked_text = ":open_mouth:"

# !ThanksCoronaBot command
    thanks_text = "You're welcome dude."

# Send message based on command
    if message.content == "!scary":
        response = shocked_text
    elif message.content == "!cases":
        response = cases_text
    elif message.content == "!deaths":
        response = deaths_text
    elif message.content == "!recovered":
        response = recovered_text
    elif message.content == "!ThanksCoronaBot":
        response = thanks_text
    elif message.content == "!cmds":
        response = "Commands available: !scary, !cases, !deaths, !recovered"
    elif message.content == "!FuckCoronaBot":
        response = "Hippity Hoppity, you are now Coronavirus' property."
    await message.channel.send(response)



client.run(TOKEN)
