from asyncio import tasks
from itertools import cycle
import json
import re
import string
import sys
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


bot = commands.Bot(command_prefix='!', self_bot=True)


# Load the config
config = None
config_path = 'config.json'
if eel.os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)

eel.init('web')

rpc = Presence("1188277538150162514")
rpc.connect()
rpc.update(state="Fucking Discord at .gg/tycfNPuYKu", large_image="logo1")


@bot.event
async def on_connect():
    userid = bot.user.id
    global login_time
    # login_time = time.time()         #V3
    # eel.js_update_uptime()           #V3

    notification.notify(
        title='Verexta',
        message='Logged in successfully!',
        app_icon=None,
        timeout=10,
    )


PIPES = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"


IMAGE = 'https://cdn.discordapp.com/attachments/1178861688439721994/1188283656708575272/Screenshot_2023-12-23_213325.png?ex=6599f665&is=65878165&hm=160c99ce7c8a3e9f1b971795dee5abffa22335b6a91353d9ed36dcf92e452c28&'

def make_embed(content, section, image=None):
    parsedcontent = urllib.parse.quote(content)

    parsedauthor = urllib.parse.quote("VEREXTA V2")
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
            bot.run(token, bot=False)
            return 'success'
        else:
            return 'failure'
    except Exception as e:
        print(f"An error occurred while launching the bot: {e}")
        return 'failure'

# Commands
mode = config['mode']

@bot.command()
async def cmds(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```List of all cmds\n\n 1:  troll\n 2:  utility\n 3:  Raid\n 4:  Misc```")
        await ctx.send("```fix\nVerexta V2```")
    elif mode == 'embed':
        content = "List of all cmds\n\n 1:  troll\n 2:  utility\n 3:  Raid\n 4:  Misc"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def troll(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```Trolling Commands\n\n 1:  textchunk\n 2:  scare\n 3:  fucku\n 4:  ghostping```")
        await ctx.send("```fix\nVerexta V2```")
    elif mode == 'embed':
        content = "Trolling Commands\n\n 1:  textchunk\n 2:  scare\n 3:  fucku\n 4:  ghostping"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def utility(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```Utility Commands\n\n 1:  mail\n 2:  whois (Ping User)\n 3:  nrand (num1 num2)\n 4:  cleardms\n 5:  exit```")
        await ctx.send("```fix\nVerexta V2```")
    elif mode == 'embed':
        content = "Useful Commands\n\n 1:  mail\n 2:  whois\n 3:  nrand (num1 num2)\n 4:  cleardms\n 5:  exit"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def raid(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```RAID CMDS\n\n 1:  DelChannels\n 2:  Purge\n 3:  Cspam (channel name, Number of channels)\n 4:  webhook (WEBHOOK, MESSGAE, NUM OF MESSAGES)\n 5:  createhook (Name)\n 6:  spam (Num of msgs, message)\n 7:  webraid (Number, Channel Name, Limit, Message)\n 8:  massmention [Change your message in the config],\n!raid2 For Next Page```")
        await ctx.send("```fix\nVerexta V2```")
    elif mode == 'embed':
        content = "RAID CMDS\n\n 1:  DelChannels\n 2:  Purge\n 3:  Cspam (channel name, Number of channels)\n 4:  webhook (WEBHOOK, MESSGAE, NUM OF MESSAGES)\n 5:  createhook (Name)\n 6:  spam (Num of msgs, message)\n 7:  webraid (Number, Channel Name, Limit, Message)\n 8:  massmention [Change your message in the config],\n!raid2 For Next Page"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)
    
@bot.command()
async def raid2(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```RAID 2 CMDS\n\n 1: rolespam (amount)\n 2: threadspam (Name, Amount)\n 3: pinspam (Amount)```")
        await ctx.send("```fix\nVerexta V2```")
    elif mode == 'embed':
        content = "RAID 2 CMDS\n\n 1: rolespam (amount)\n 2: threadspam (Name, Amount)\n 3: pinspam (Amount)"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)

@bot.command()
async def misc(ctx):
    await ctx.message.delete()
    if mode == 'codeblocks':
        await ctx.send("```MISC CMDS\n\n 1: Poll\n 2: Lenny\n 3: nick\n 4: rgif\n 5: info\n 6: pfp (@user)```")
        await ctx.send("```fix\nVerexta V2```")
    elif mode == 'embed':
        content = "MISC CMDS\n\n 1: Poll\n 2: Lenny\n 3: nick\n 4: rgif\n 5: info\n 6: pfp (@user)"
        url = make_embed(content, "", IMAGE)
        await ctx.send(url)


with open('config.json') as f:
    config = json.load(f)
varient = config['varient']
version = config['version']
message1 = config['massmention']


with open("proxies.txt", "r") as file:
    proxies = [line.strip() for line in file.readlines()] 



@bot.command()
async def clear(ctx):
    lines = "᲼᲼" + "\n" * 1500 + "᲼᲼"
    await ctx.send(lines)

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
async def massmention(ctx):
    # No shit this wont work im just testing
    await ctx.message.delete()
    with open("userdata.json", 'r') as f:
        users = json.load(f) 

    for members in ctx.guild.members:
        id = members.id
        users["userid"] = {"ID":id}
        print(f"ID: {id} has been saved to json file")

    with open("userdata.json", "w") as f:
        json.dump(users, f, indent=4)

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
    await ctx.send(' ', delete_after=0.00005)
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
    poll_message = await ctx.send(f"**Poll:** {question}\n\nReact with ✅ to vote yes or ❌ to vote no.")
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
    await ctx.send(f"Username: {user.name}#{user.discriminator}\nID: {user.id}")
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
    


if __name__ == "__main__":
    latest_version = get_latest_version()
    if version == latest_version:
        with open('config.json', 'r') as f:
            config = json.load(f)
            TOKEN = config.get('token', '')

            if not TOKEN:
                eel.start('login.html', size=(850, 550))
            else:
                eel.start('index.html', size=(850, 550))
                launch()
    else:
        choice = input("Looks Like There Is A New Update. Would You Like To Continue Anyways? (y/n) ---{ ")
        if choice == 'y':
            with open('config.json', 'r') as f:
                config = json.load(f)
                TOKEN = config.get('token', '')

                if not TOKEN:
                    eel.start('login.html', size=(850, 550), options={'port': 0})
                else:
                    eel.start('index.html', size=(850, 550), options={'port': 0})
                    launch()
        else:
            sys.exit()