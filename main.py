from asyncio import tasks
import datetime
from itertools import cycle
import json
import re
import string
import sys
import threading
import time
import aiohttp
from bs4 import BeautifulSoup
from colorama import Fore
import discord
import eel
from discord.ext import commands
from plyer import notification
from mailtm import Email
import random
import asyncio
import requests
import urllib.parse
import concurrent.futures
import tls_client
from pypresence import Presence
from PIL import Image, ImageDraw, ImageFont
import io

eel.init('web')

bot = commands.Bot(command_prefix='!', self_bot=True)
bot.remove_command("help")


# Load the config
config = None
config_path = 'config.json'
if eel.os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)





@bot.event
async def on_connect():
    bot.start_time = datetime.datetime.now()
    userid = bot.user.id
    global login_time
    await bot.change_presence(status=discord.Status.dnd)
    login_time = time.time()         
    eel.js_update_uptime()


    print(f'Logged in as {bot.user}')
    command_count = len(bot.commands)
    print(f'Total commands: {command_count}')


    notification.notify(
        title='Verexta v3.0.2',
        message='Connected To Discord',
        app_icon=None,
        timeout=10,
    )


PIPES = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"


IMAGE = 'https://cdn.discordapp.com/attachments/1081999276852387981/1230943954732847124/logo1.png?ex=663528e4&is=6622b3e4&hm=616925b2f8d9fe202550de89c936917206ccd5b911a6ed69ffa74840a0f387a6&'

def make_embed(content, section, image=None):
    parsedcontent = urllib.parse.quote(content)

    parsedauthor = urllib.parse.quote("VEREXTA V3")
    parsedcolor = urllib.parse.quote("#FF4343")
    url = f"{section}{PIPES}https://embedl.ink/?deg&provider=&providerurl=&author={parsedauthor}&color={parsedcolor}&media=thumbnail&mediaurl={image}&desc={parsedcontent}"
    return url


@eel.expose
def save_token(token):
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    config['token'] = token

    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    return 'success'

@eel.expose
def launch():
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}

    token = config.get('token', None)

    try:
        if token:
            bot.run(token)
    except Exception as e:
        eel.start('login.html', size=(900, 550), mode='chrome', port=8080)
        print(f"An error occurred while launching the bot: {e}")
        return 'failure'

# Commands
mode = config['mode']
rpc_status = config['RPC']

if rpc_status == "on":
    rpc = Presence("1188277538150162514")
    rpc.connect()
    rpc.update(state="Fucking Discord at .gg/tycfNPuYKu", large_image="logo1")

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```List of all cmds\n\n 1:  troll\n 2:  utility\n 3:  Raid\n 4:  Misc```")
        await ctx.send("```fix\nVerexta V3```")
    elif mode == 'embed':
        content = "List of all cmds\n\n 1:  troll\n 2:  utility\n 3:  Raid\n 4:  Misc"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def troll(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```Trolling Commands\n\n 1:  textchunk\n 2:  scare\n 3:  fucku\n 4:  ghostping```")
        await ctx.send("```fix\nVerexta V3```")
    elif mode == 'embed':
        content = "Trolling Commands\n\n 1:  textchunk\n 2:  scare\n 3:  fucku\n 4:  ghostping"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def utility(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```Utility 2 Cmds\n\n 1:  mail\n 2:  whois (Ping User)\n 3:  nrand (num1 num2)\n 4:  cleardms\n 5:  exit\n 6: speechbubble\n 7: copy (destination server's id)```")
        await ctx.send("```fix\nVerexta V3```")
    elif mode == 'embed':
        content = "Utility Commands\n\n 1:  mail\n 2:  whois\n 3:  nrand (num1 num2)\n 4:  cleardms\n 5:  exit\n 6: speechbubble\n 7: copy (destination server's id)"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def utility2(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```Utility 2 Cmds\n\n 1: listguilds\n 2: vanish\n 3: stopwatch (options: start, pause, end)\n 4: mute (@user)```")
        await ctx.send("```fix\nVerexta V3```")
    elif mode == 'embed':
        content = "Utility 2 Cmds\n\n 1: listguilds\n 2: vanish\n 3: stopwatch (options: start, pause, end)\n 4: mute (@user)"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def raid(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```RAID CMDS\n\n 1:  DelChannels\n 2:  Purge\n 3:  Cspam (channel name, Number of channels)\n 4:  webhook (WEBHOOK, MESSGAE, NUM OF MESSAGES)\n 5:  createhook (Name)\n 6:  spam (Num of msgs, message)(\n 7:  webraid (Number, Channel Name, limit, messsage)\n!raid2 For Next Page```")
        await ctx.send("```fix\nVerexta V3```")
    elif mode == 'embed':
        content = "RAID CMDS\n\n 1:  DelChannels\n 2:  Purge\n 3:  Cspam (channel name, Number of channels)\n 4:  webhook (WEBHOOK, MESSGAE, NUM OF MESSAGES)\n 5:  createhook (Name)\n 6:  spam (Num of msgs, message) (Amount Of Times To Spam It)\n 7:  webraid (Number, Channel Name, limit, messsage\n!raid2 For Next Page"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)
    
@bot.command()
async def raid2(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```RAID 2 CMDS\n\n 1: rolespam (amount)\n 2: threadspam (Name, Amount)\n 3: pinspam (Amount)\n 4: pollspam (Amount)```")
        await ctx.send("```fix\nVerexta V3```")
    elif mode == 'embed':
        content = "RAID 2 CMDS\n\n 1: rolespam (amount)\n 2: threadspam (Name, Amount)\n 3: pinspam (Amount)\n 4: pollspam (Amount)"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def misc(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```MISC CMDS\n\n 1: Poll\n 2: Lenny\n 3: nick\n 4: rgif\n 5: info\n 6: pfp (@user)\n 7: roll```")
        await ctx.send("```fix\nVerexta V3```")
    elif mode == 'embed':
        content = "MISC CMDS\n\n 1: Poll\n 2: Lenny\n 3: nick\n 4: rgif\n 5: info\n 6: pfp (@user)\n 7: roll"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def misc2(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```MISC CMDS\n\n 1: uptime```")
        await ctx.send("```fix\nVerexta V3```")
    elif mode == 'embed':
        content = "MISC CMDS\n\n 1: uptime"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)




with open('config.json') as f:
    config = json.load(f)
varient = config['varient']
version = config['version']
message1 = config['massmention']
nitro_status = config['Nitro_toggle']



@bot.command()
async def uptime(ctx):
    await ctx.message.delete()
    current_time = datetime.datetime.now()
    uptime_duration = current_time - bot.start_time

    days = uptime_duration.days
    hours, remainder = divmod(uptime_duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    uptime_str = f"Uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds."
    await ctx.send(uptime_str)



@bot.command()
async def mute(ctx, member: discord.User, duration: int):
    await ctx.message.delete()
    if ctx.author.guild_permissions.manage_roles:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")

        await member.add_roles(muted_role)
        await ctx.send(f"{member.mention} has been muted for {duration} seconds.")

        try:
            await member.send(f"You have been muted in the server for {duration} seconds.")
        except discord.Forbidden:
            await ctx.send("I couldn't send a DM to the user.")

        await asyncio.sleep(duration)
        await member.remove_roles(muted_role)
        await ctx.send(f"{member.mention} has been unmuted after {duration} seconds.")

    else:
        await ctx.send("You do not have permission to use this command.")




@bot.command()
async def stopwatch(ctx, opt):
    await ctx.message.delete()
    if opt.lower() == "start":
        await start_stopwatch(ctx)
    elif opt.lower() == "stop":
        await stop_stopwatch(ctx)
    else:
        await ctx.send("Invalid option. Please use `start` or `stop`.")

async def start_stopwatch(ctx):
    global start_time
    start_time = time.time()
    await ctx.send("Stopwatch started.")

async def stop_stopwatch(ctx):
    if 'start_time' in globals():
        end_time = time.time()
        elapsed_time = end_time - start_time
        await ctx.send(f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds.")
        del globals()['start_time']
    else:
        await ctx.send("Stopwatch was not started.")

@bot.command()
async def vanish(ctx):
    await ctx.message.delete()
    guild_id = ctx.guild.id
    author_id = ctx.author.id

    url = f'https://discord.com/api/v9/guilds/{guild_id}/messages/search?author_id={author_id}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()

        if "messages" in json_data:
            deleted_count = 0
            for message_list in json_data["messages"]:
                for message in message_list:
                    if "id" in message and "channel_id" in message:
                        message_id = message["id"]
                        channel_id = message["channel_id"]

                        delete_url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}'

                        delete_response = requests.delete(delete_url, headers=headers)

                        if delete_response.status_code == 204:
                            deleted_count += 1
                            print(f"Deleted message ID {message_id} in channel ID {channel_id}")
                            if deleted_count % 10 == 0:
                                print("Pausing for 5 seconds...")
                                await asyncio.sleep(5)

            print("Total messages deleted:", deleted_count)
        else:
            print("No messages found.")
    else:
        print("Failed to retrieve messages. Status code:", response.status_code)



        
        


@bot.command()
async def pollspam(ctx, amount: int):
    await ctx.message.delete()
    channel = bot.get_channel(ctx.channel.id)
    url = f'https://discord.com/api/v9/channels/{channel.id}/messages'

    headers = {
        "Authorization": f"{TOKEN}",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.6",
        "Content-Type": "application/json",
        "Origin": "https://canary.discord.com",
        "Referer": "https://canary.discord.com/channels/1159128651443482774/1199051726045581332",
        "Sec-Ch-Ua": "\"Brave\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Sec-Gpc": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "en-US",
        "X-Discord-Timezone": "America/Araguaina",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3NlYXJjaC5icmF2ZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6InNlYXJjaC5icmF2ZS5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9zZWFyY2guYnJhdmUuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6InNlYXJjaC5icmF2ZS5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyODQxMjksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

    payload = {
        "content": "",
        "poll": {
            "question": {"text": "Verexta V3 On Top"},
            "allow_multiselect": False,
            "answers": [
                {"poll_media": {"text": "Yes"}},
                {"poll_media": {"text": "Yes"}},
                {"poll_media": {"text": "Yes"}},
                {"poll_media": {"text": "Yes"}},
                {"poll_media": {"text": "Yes"}},
                {"poll_media": {"text": "Yes"}},
                {"poll_media": {"text": "Yes"}},
                {"poll_media": {"text": "Yes"}},
                {"poll_media": {"text": "Yes"}},
                {"poll_media": {"text": "Yes"}}
            ],
            "duration": 168,
            "layout_type": 1,
            "question": {"text": "Verexta V3 On Top"},
            "text": "Verexta V3 On Top"
        }
    }

    async def send_poll():
        for _ in range(amount):
            json_payload = json.dumps(payload)
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=json_payload) as response:
                    status = response.status
                    print(f"Sent poll with status: {status}")

    await send_poll()

@bot.command()
async def listguilds(ctx):
    await ctx.message.delete()
    url = 'https://discord.com/api/v9/users/@me/guilds'

    headers = {
        "authorization": TOKEN 
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        guilds_data = response.json()
        
        message = "List of Guilds:\n"
        for guild in guilds_data:
            guild_info = f"{guild['name']} - ID: {guild['id']}\n"

            if len(message) + len(guild_info) <= 2000:
                message += guild_info
            else:
                await ctx.send(message)
                message = guild_info


        if message:
            await ctx.send(message)
    else:
        await ctx.send(f"Failed to fetch guilds. Status code: {response.status_code}")


@bot.command()
async def roll(ctx):
    await ctx.message.delete()
    result = random.randint(1, 6)
    await ctx.send(f"🎲 You rolled: {result}")


@bot.command()
async def speechbubble(ctx):
    await ctx.message.delete()
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image to use this command.")
        return
    attachment = ctx.message.attachments[0]
    if not attachment.filename.endswith(('png', 'jpg', 'jpeg', 'gif')):
        await ctx.send("Please attach a valid image file (PNG, JPG, JPEG, or GIF).")
        return
    try:
        image_bytes = await attachment.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
    except Exception as e:
        await ctx.send(f"Error opening the image: {e}")
        return
    speech_bubble = Image.open("extra/tail_center.png").convert("RGBA")
    new_width = image.width
    speech_bubble = speech_bubble.resize((new_width, int(new_width * speech_bubble.height / speech_bubble.width)))

    image.paste(speech_bubble, (0, 0), mask=speech_bubble)
    result_bytes = io.BytesIO()
    image.save(result_bytes, format='GIF', save_all=True, append_images=[image], duration=100, loop=0)
    result_bytes.seek(0)
    
    await ctx.send(file=discord.File(result_bytes, filename='speech_bubble.gif'))


# Thank you korxyy for making the server copy module
@bot.command()
async def copy(ctx, destination_guild_id: int):
    await ctx.message.delete()
    try:
        await ctx.send(f"Copying {ctx.guild.name} ⌛")
       
        source_guild = ctx.guild

      
        destination_guild = bot.get_guild(destination_guild_id)

        if not destination_guild:
            await ctx.send("Invalid destination guild ID.")
            return

     
        for channel in destination_guild.channels:
            await channel.delete()

      
        await destination_guild.edit(name=source_guild.name + " [COPY]")

    
        for category in source_guild.categories:
            new_category = await destination_guild.create_category(category.name, position=category.position)

           
            for channel in category.channels:
                if isinstance(channel, discord.VoiceChannel):
                    await new_category.create_voice_channel(channel.name)
                elif isinstance(channel, discord.TextChannel):
                    await new_category.create_text_channel(channel.name)

                
                await asyncio.sleep(1)  

        await ctx.send("Server has been copied ✅")

    except discord.Forbidden:
        await ctx.send("You dont have the required permissions to perform this action.")
    except discord.HTTPException as e:
        if e.status == 429:  
            await ctx.send("Rate-limited. Waiting for 1 second...")
            await asyncio.sleep(1)
            await copy(ctx, destination_guild_id) 
        else:
            await ctx.send(f"An error occurred: {e}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {e}")



@bot.command()
async def tokenspam(ctx, num: int, *, message):
    channel_id = ctx.message.channel.id

    with open("tokens.txt") as file:
        tokens = [line.strip() for line in file]

    def send_message(token):
        headers = {
            "Authorization": token
        }

        data = {
            "content": message
        }

        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        for _ in range(num):
            r = requests.post(url, headers=headers, data=data)
            r.raise_for_status()
            print(f"Message sent using {token}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for token in tokens:
            executor.submit(send_message, token)



with open("proxies.txt", "r") as file:
    proxies = [line.strip() for line in file.readlines()] 







# I skidded a lot of this joiner. Actually about 99% of it was taken from https://github.com/kekeds/discord-joiner so big shoutout to them
from dataclasses import dataclass
import tls_client

@dataclass
class JoinerData:
    pass

@dataclass
class Instance(JoinerData):
    client: tls_client.sessions
    token: str
    invite: str
    headers: dict

class OtherInfo:
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'sv,sv-SE;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9016 Chrome/108.0.5359.215 Electron/22.3.12 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'sv-SE',
        'x-discord-timezone': 'Europe/Stockholm',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDE2Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InN2IiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMTYgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMTIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMTIiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyMTg2MDQsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjM1MjM2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
    }

# I skidded a lot of this joiner. Actually about 99% of it was taken from https://github.com/kekeds/discord-joiner so big shoutout to them

class Joiner:
    def __init__(self, data: Instance) -> None:
        self.session = data.client
        self.session.headers = data.headers
        self.get_cookies()
        self.instance = data

    def rand_str(self, length: int) -> str:
        return ''.join(random.sample(string.ascii_lowercase + string.digits, length))

    def get_cookies(self) -> None:
        site = self.session.get("https://discord.com")
        self.session.cookies = site.cookies

    def join(self) -> None:
        self.session.headers.update({"Authorization": self.instance.token})
        result = self.session.post(f"https://discord.com/api/v9/invites/{self.instance.invite}", json={
            'session_id': self.rand_str(32),
        })

        if result.status_code == 200:
            print("Joined lul.")
        else:
            print("Some error or some shit")

class intilize:
    @staticmethod
    def start(i):
        Joiner(i).join() 

@bot.command()
async def joiner(ctx, invite):
    await ctx.message.delete()
    with open("tokens.txt") as file:
        tokens = [line.strip() for line in file]

    instances = []
    max_threads = 5
# I skidded a lot of this joiner. Actually about 99% of it was taken from https://github.com/kekeds/discord-joiner so big shoutout to them
    try:
        invite=invite.split("/")[-1]
    except:
        pass

    for token_ in tokens:
        header = OtherInfo.headers
        instances.append(
            Instance(
                client=tls_client.Session(
                    client_identifier=f"chrome_{random.randint(110, 115)}",
                    random_tls_extension_order=True,
                ),
                token=token_,
                headers=header,
                invite=invite,
            )
        )
# I skidded a lot of this joiner. Actually about 99% of it was taken from https://github.com/kekeds/discord-joiner so big shoutout to them
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        for i in instances:
            executor.submit(intilize.start, i)
# JOINER 





            


if nitro_status == 'on':
    TOKEN = config.get('token', '')
    headers = {
        "authorization": TOKEN
    }

    @bot.event
    async def on_message(message):
        if message.guild is not None:
            channel_id = message.channel.id
            guild_id = message.guild.id
            message_id = message.id

            guild = bot.get_guild(int(guild_id))
            channel = guild.get_channel(int(channel_id))

            data = {
                'channel_id': channel_id
            }

            try:
                if isinstance(channel, discord.TextChannel):
                    async for msg in channel.history(limit=None):
                        if msg.id == int(message_id):
                            if "discord.gift/" in msg.content:
                                code = msg.content.split("discord.gift/")[1][-16:]
                                if len(code) == 16 and code.isalnum():
                                    print("Found Nitro Code | Attempting To Redeem...")
                                    url = f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem'
                                    response = requests.post(url, headers=headers, json=data)
                            break
            except discord.Forbidden:
                print("Permission error - Unable to fetch messages. | NITRO SNIPER")
            except AttributeError as e:
                if "StageChannel" in str(e):
                    pass
                else:
                    raise

        await bot.process_commands(message)
                    
def toggleAFK():
    afk_status = config['AFK_toggle']
    afk_msg = config['AFK']
    if afk_status == 'on':
        @bot.event
        async def on_message(message):
            if message.guild is None and message.author != bot.user:
                await message.channel.send(afk_msg)    












@bot.command()
async def pinspam(ctx, count: int):
    await ctx.message.delete()
    amount = 0
    channel = bot.get_channel(ctx.channel.id)
    history = await channel.history(limit=count).flatten()

    headers = {
        'Authorization': TOKEN
    }

    for message in history:
        amount += 1
        url = f"https://discord.com/api/v9/channels/{channel.id}/pins/{message.id}"
        r = requests.put(url, headers=headers)



@bot.command()
async def threadspam(ctx, name, amount):
    await ctx.message.delete()

    headers = {
        'Authorization': TOKEN
    }

    data = {
        'name': name,
        'type': '11'
    }
    
    for i in range(int(amount)):
        url = f'https://discord.com/api/v9/channels/{ctx.channel.id}/threads'
        response = requests.post(url, headers=headers, data=data)



@bot.command()
async def rolespam(ctx, amount):
    await ctx.message.delete()
    
    headers = {
        'Authorization': TOKEN
    }
    
    for i in range(int(amount)):
        url = f'https://discord.com/api/v9/guilds/{ctx.guild.id}/roles'
        response = requests.post(url, headers=headers)





@bot.command()
async def webraid(ctx, number, channel_name, limit, *, message):
    await ctx.message.delete()
    guild = ctx.guild
    tasks = []

    async def create_channel_and_send_message():
        new_channel = await guild.create_text_channel(channel_name)

        webhook = await new_channel.create_webhook(name=f"Webhook-{new_channel.name}")

        for i in range(int(limit)):
            await asyncio.sleep(random.uniform(0.2, 0.3))
            try:
                await webhook.send(content=message)
            except Exception as e:
                print(f"Error sending message in channel {new_channel.name}: {e}")


    for i in range(int(number)):
        tasks.append(create_channel_and_send_message())
    await asyncio.gather(*tasks)




@bot.command()
async def pfp(ctx, user: discord.User):
    await ctx.message.delete()
    avatar_url = user.avatar_url
    await ctx.send(avatar_url)



@bot.command()
async def spam(ctx, amount, *, message):
    await ctx.message.delete()
    try:
        amount = int(amount)
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    if amount <= 0 or amount > 125:
        print("Please enter a valid amount within a reasonable range.")
        return
    for i in range(amount):
        await ctx.send(message)


@bot.command()
async def info(ctx):
    await ctx.message.delete()
    print("Executed version")
    await ctx.send(f"{version}" + " | " + f"{varient}")



giphy_api_key = "0UTRbFtkMxAplrohufYco5IY74U8hOes"
giphy_base_url = "https://api.giphy.com/v1/gifs/"
giphy_tag = "fail"
giphy_type = "random"
giphy_rating = "pg-13"
giphy_url = f"{giphy_base_url}{giphy_type}?api_key={giphy_api_key}&tag={giphy_tag}&rating={giphy_rating}"

@bot.command()
async def rgif(ctx):
    await ctx.message.delete()
    response = requests.get(giphy_url)

    if response.status_code == 200:
        try:
            data = response.json()
            gif_url = data.get('data', {}).get('images', {}).get('original', {}).get('url')

            if gif_url:
                await ctx.send(gif_url)
            else:
                await ctx.send("Error: Couldn't find a valid GIF URL in the response.")
        except ValueError as e:
            await ctx.send(f"Error: {e}")
    else:
        await ctx.send(f"Error sending the GET request to the Giphy API. Status code: {response.status_code}")


    
    



    

@bot.command()
async def createhook(ctx, name):
    print("Executed createhook")
    channel = ctx.channel
    await ctx.message.delete()
    webhook = await channel.create_webhook(name=name)
    await ctx.send(f"Webhook created Successfully in {channel.mention}")

@bot.command()
async def exit(ctx):
    print("Executed exit")
    await ctx.message.delete()
    await bot.close()

@bot.command()
async def ghostping(ctx, *, args):
    await ctx.message.delete()
    await ctx.send('', delete_after=0.00005)
    print("Executed ghostping")

@bot.command()
async def webhook(ctx, webhook_url, message, number_of_messages):
    await ctx.message.delete()
    for i in range(int(number_of_messages)):
        response = requests.post(webhook_url, json={'content': message})
    print("Executed webhook")

#textchunks
@bot.command()
async def textchunk(ctx):
    await ctx.message.delete()
    await ctx.send("wrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahegauohpgapuhogeauegruagopreuaogeuoagruhoasgerhuasgrehuoguhosearguhgaseruhasgrasgpuhhpugsarehugpresahupgsaerhpusagerhugpsarehpusagreughsaresagraugpraguerusaghersguhrspgreuspgrusughsuhghugresuhgreuhgreuhgrespuhrgepughsrugw983570y5w9780yu2978ughjwuntrwu4586kjtbroiubnriubnrtuibnrutibnrtubnrtuibrtbuirjbnuritburtbhtruibtrbuibuitbruibhtjuirhtubtrhbutrbhtrubhtubburbjurbjrtburtjbutjbtubjtubtjbutbjtubtjbtbutjbtubjtubtjbwrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahegauohpgapuhogeauegruagopreuaogeuoagruhoasgerhuasgrehuoguhosearguhgaseruhasgrasgpuhhpugsarehugpresahupgsaerhpusagerhugpsarehpusagreughsaresagraugpraguerusaghersguhrspgreuspgrusughsuhghugresuhgreuhgreuhgrespuhrgepughsrugw983570y5w9780yu2978ughjwuntrwu4586kjtbroiubnriubnrtuibnrutibnrtubnrtuibrtbuirjbnuritburtbhtruibtrbuibuitbruibhtjuirhtubtrhbutrbhtrubhtubburbjurbjrtburtjbutjbtubjtubtjbutbjtubtjbtbutjbtubjtubtjbwrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahegauohpgapuhogeauegruagopreuaogeuoagruhoasgerhuasgrehuoguhosearguhgaseruhasgrasgpuhhpugsarehugpresahupgsaerhpusagerhugpsarehpusagreughsaresagraugpraguerusaghersguhrspgreuspgrusughsuhghugresuhgreuhgreuhgrespuhrgepughsrugw983570y5w9780yu2978ughjwuntrwu4586kjtbroiubnriubnrtuibnrutibnrtubnrtuibrtbuirjbnuritburtbhtruibtrbuibuitbruibhtjuirhtubtrhbutrbhtrubhtubburbjurbjrtburtjbutjbtubjtubtjbutbjtubtjbtbutjbtubjtubtjbwrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahegauohpgapuhogeauegruagopreuaogeuoagruhoasgerhuasgrehuoguhosearguhgaseruhasgrasgpuhhpugsarehugpresahupgsaerhpusagerhugpsarehpusagreughsaresagraugpraguerusaghersguhrspgreuspgrusughsuhghugresuhgreuhgreuhgrespuhrgepughsrugw983570y5w9780yu2978ughjwuntrwu4586kjtbroiubnriubnrtuibnrutibnrtubnrtuibrtbuirjbnuritburtbhtruibtrbuibuitbruibhtjuirhtubtrhbutrbhtrubhtubburbjurbjrtburtjbuwrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahefrrhrthrthrththh")
    print("Executed textchunk")


#cspam
@bot.command()
async def cspam(ctx, channel_name: str, number_of_channels: int):
    await ctx.message.delete()
    guild = ctx.guild

    async def create_channel(i):
        await guild.create_text_channel(channel_name)

    await asyncio.gather(*[create_channel(i) for i in range(number_of_channels)])

    await print(f"Created {number_of_channels} channels with the name {channel_name}.")

#Delete Channels
@bot.command()
async def delchannels(ctx):
    await ctx.message.delete()

    async def delete_channel(channel):
        await channel.delete()

    tasks = [asyncio.create_task(delete_channel(channel)) for channel in ctx.guild.channels]
    await asyncio.gather(*tasks)

    print("Executed DelChannels")

#ClearDms
@bot.command()
async def cleardms(ctx, number: int):
    await ctx.message.delete()
    msgs = await ctx.message.channel.history(limit=number).flatten()
    for msg in msgs:
        if msg.author.name == ctx.message.author.name:
            await msg.delete()
    print("Executed cleardms")

#scare
@bot.command()
async def scare(ctx):
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/to-everyone-that-is-looking-for-this-spider-gif-gif-20691150")
    print("Executed scare")

#fucku
@bot.command()
async def fucku(ctx):
    await ctx.message.delete()
    await ctx.send("https://media.discordapp.net/attachments/853726500371955742/869938928050921542/image0.gif")
    print("Executed fucku")

#nrand
@bot.command()
async def nrand(ctx, num1: int, num2: int):
    await ctx.message.delete()
    await ctx.send(f"Your Number is: {random.randint(num1, num2)}")
    print("Executed nrand")

#Lenny
@bot.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)
    print("Executed Lenny")

    #Poll
@bot.command()
async def poll(ctx, *args):
    await ctx.message.delete()
    if not args:
        return await ctx.send("No question was given.")
    question = " ".join(args)
    content = f"Poll: {question}\n\nReact with ✅ to vote yes or ❌ to vote no."
    url = make_embed(content, "", IMAGE)
    poll_message = await ctx.send(url)
    await poll_message.add_reaction("✅")
    await poll_message.add_reaction("❌")
    print("Executed poll")

    #mail
@bot.command()
async def mail(ctx):
    await ctx.message.delete()
    print("Executed mail")
    def listener(message):
        print("\nSubject: " + message['subject'])
        print("Content: " + message['text'] if message['text'] else message['html'])

    test = Email()
    print(Fore.CYAN + "\nDomain: " + test.domain)

    test.register()
    print(Fore.CYAN +  "\nEmail Adress: " + str(test.address))

    test.start(listener, interval=4)
    print(Fore.GREEN +  "\nWaiting for an email...")


    #whois
@bot.command()
async def whois(ctx, user: discord.User):
    await ctx.message.delete()
    content = f"Username: {user.name}#{user.discriminator}\nID: {user.id}\nCreation Date: {user.created_at}"
    url = make_embed(content, "", IMAGE)
    await ctx.send(url)
    print("Executed whois")

    #nick
@bot.command()
async def nick(ctx, *, nickname: str):
    await ctx.message.delete()
    try:
        await ctx.message.author.edit(nick=nickname)
        await ctx.send(f'Nickname changed to {nickname}!')
    except discord.Forbidden:
        await ctx.send("I don't have permission to change your nickname.")
        print("Executer nick")


    #Purge
@bot.command()
async def purge(ctx, count: int):
    await ctx.message.delete()

    async def delete_messages(messages):
        for message in messages:
            await message.delete()

    channel = bot.get_channel(ctx.channel.id)
    history = await channel.history(limit=count).flatten()
    chunk_size = 100
    chunks = [history[i:i + chunk_size] for i in range(0, len(history), chunk_size)]
    await asyncio.gather(*(delete_messages(chunk) for chunk in chunks))



def get_latest_version():
    url = 'https://raw.githubusercontent.com/If-0n/Verexta/main/version.txt'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        latest_version = response.text.strip()
        
        return latest_version
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch the latest version. {e}")
        return None
    

def grab_it():
    headers = {
        'Authorization': TOKEN
    }

    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch user information. Status code: {response.status_code}")
        print(response.text)
        return None

@eel.expose
def update_discord():
    user_info = grab_it()
    if user_info:
        username = user_info['username']
        userid = user_info['id']
        discord = f"DISCORD<br><br>Username: {username}<br><br>ID: {userid}"
        return discord
    else:
        return "Failed to get Discord information."
    

@eel.expose
def update_info():
    token_count = 0

    with open('tokens.txt', 'r') as file:
        for line in file:
            if line.strip():
                token_count += 1

    info = f"RAID INFO<br><br>Tokens: {token_count}<br><br>"
    return info

with open("config.json", 'r') as c:
    config = json.load(c)
    afk_text = config["AFK_toggle"] = "off"
    if afk_text == 'on':
        afk_status = True
    else:
        afk_status = False



        


@eel.expose
def update_motd():
    pastebin_url = 'https://pastebin.com/raw/QsjkC98j'
    try:
        response = requests.get(pastebin_url)
        motd = "MOTD\n\n" + response.text
        return motd
    except requests.RequestException as e:
        print(f"Error fetching MOTD: {e}")
        return None
    



latest_version = get_latest_version()
if version == latest_version:
    with open('config.json', 'r') as f:
        config = json.load(f)
        TOKEN = config.get('token', '')

        if not TOKEN:
            eel.start('login.html', size=(900, 550))
        else:
            eel.start('index.html', size=(900, 550))
            bot_thread = threading.Thread(target=launch)
            bot_thread.start()
else:
    choice = input("Looks Like There Is A New Update. Would You Like To Continue Anyways? (y/n) ---{ ")
    if choice == 'y':
        with open('config.json', 'r') as f:
            config = json.load(f)
            TOKEN = config.get('token', '')

            if not TOKEN:
                    eel.start('login.html', size=(900, 550), mode='chrome', port=8080)
            else:
                eel.start('index.html', size=(900, 550), mode='chrome', port=8080)
                bot_thread = threading.Thread(target=launch)
                bot_thread.start()
    else:
        sys.exit()