from asyncio import tasks
from itertools import cycle
import json
import time
from colorama import Fore
import discord
import eel
from discord.ext import commands
from plyer import notification
from mailtm import Email
import random
import asyncio
import requests

bot = commands.Bot(command_prefix='!', self_bot=True)


# Load the config
config = None
config_path = 'config.json'
if eel.os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)

eel.init('web')

@bot.event
async def on_connect():
    global login_time
    login_time = time.time()
    notification.notify(
        title='Verexta',
        message='Logged in successfully!',
        app_icon=None,
        timeout=10,
    )

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

@bot.command()
async def cmds(ctx):
    await ctx.message.delete()
    await ctx.send("```List of all cmds\n\n 1:  troll\n 2:  utility\n 3:  Raid\n 4:  Misc```")
    await ctx.send("```fix\nVerexta V2```")
    print("Executed cmds")

@bot.command()
async def troll(ctx):
    await ctx.message.delete()
    await ctx.send("```Trolling Commands\n\n 1:  textchunk\n 2:  scare\n 3:  fucku\n 4:  ghostping```")
    await ctx.send("```fix\nVerexta V2```")
    print("Executed Troll")

@bot.command()
async def utility(ctx):
    await ctx.message.delete()
    await ctx.send("```Useful Commands\n\n 1:  mail\n 2:  whois\n 3:  nrand (num1 num2)\n 4:  cleardms\n 5:  exit```")
    await ctx.send("```fix\nVerexta V2```")
    print("Executed utility")

@bot.command()
async def raid(ctx):
    await ctx.message.delete()
    await ctx.send("```RAID CMDS\n\n 1:  DelChannels\n 2:  Purge\n 3:  Cspam (channel name, Number of channels)\n 4:  webhook (WEBHOOK, MESSGAE, NUM OF MESSAGES)\n 5:  createhook (Name)\n 6:  massmention (message)\n 7:  spam (Message To Spam) (Amount Of Times To Spam It)\n 7:  webraid (Number, Channel Name, Message)\n 8:  massmention [Change your message in the config]```")
    await ctx.send("```fix\nVerexta V2```")
    print("Executed Raid")

@bot.command()
async def misc(ctx):
    await ctx.message.delete()
    await ctx.send("```MISC CMDS\n\n 1: Poll\n 2: Lenny\n 3: nick\n 4: rgif\n 5: info\n 6: pfp (@user)```")
    await ctx.send("```fix\nVerexta V2```")
    print("Executed MISC")





with open('config.json') as f:
    config = json.load(f)
varient = config['varient']
version = config['version']
mmmessage = config['massmention']

# Loading Proxies
with open("proxies.txt", "r") as file:
    proxies = [line.strip() for line in file.readlines()]

@bot.command()
async def spamroles(ctx):
    await ctx.message.delete()
    


@bot.command()
async def massmention(ctx):

    await ctx.message.delete()
    members = await ctx.guild.fetch_members()

    for member in members:
        if member.name and member.status != discord.Status.offline and not member.bot:
            message = f"""{mmmessage}""" + member.mention

            try:
                await ctx.send(message)
            except discord.errors.HTTPException as e:
                if e.status != 200:
                    print("TimeOut: Waiting 5 secs..")
                    await asyncio.sleep(5)  # Wait for 10 seconds
    notification.notify(
    title = 'Verexta V2',
    message = 'Mass Mention Completed!',
    app_icon = None,
    timeout = 1,
)

@bot.command()
async def webraid(ctx, number, channel_name, message):
    guild = ctx.guild
    tasks = []

    async def create_channel_and_send_message():
        new_channel = await guild.create_text_channel(channel_name)

        # Create a unique webhook for each channel
        webhook = await new_channel.create_webhook(name=f"Webhook-{new_channel.name}")

        while True:
            await asyncio.sleep(random.uniform(0.1, 0.3))
            try:
                await webhook.send(content=message)
                print(f"Message sent using webhook in channel {new_channel.name}")
            except Exception as e:
                print(f"Error sending message in channel {new_channel.name}: {e}")

    for i in range(int(number)):
        tasks.append(create_channel_and_send_message())

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)




@bot.command()
async def pfp(ctx, user: discord.User):
    avatar_url = user.avatar.url
    await ctx.send(avatar_url)



@bot.command()
async def spam(ctx, message, amount):
    try:
        amount = int(amount)
    except ValueError:
        await ctx.send("Invalid amount. Please enter a valid number.")
        return
    if amount <= 0 or amount > 100:
        await ctx.send("Please enter a valid amount within a reasonable range.")
        return
    for i in range(amount):
        await ctx.send(message)



gif_urls = [
    "https://media.discordapp.net/attachments/951919254041686087/976814223604727808/IMG_3598.gif",
    "https://tenor.com/view/meme-music-fortnite-lebron-james-gif-25492927",
    "https://tenor.com/view/wiggle-dance-wyoming-snake-gif-8014362",
    "https://tenor.com/view/hitam-atau-black-laugh-white-teeth-gif-16766958",
    "https://tenor.com/view/black-man-jumping-big-black-man-twerk-black-gif-22678838",
    "https://tenor.com/view/black-man-meme-gif-26066035",
]

@bot.command()
async def info(ctx):
    print("Executed version")
    await ctx.send(f"{version}" + " | " + f"{varient}")

@bot.command()
async def rgif(ctx):
    print("Executed rgif")
    random_gif_url = random.choice(gif_urls)
    await ctx.send(f"{random_gif_url}")

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
    for i in range (number_of_channels):
        channel = await guild.create_text_channel(channel_name)

    #Delete Channels
@bot.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.delete()
    print("Executed DelChannels")

    #ClearDms
@bot.command()
async def cleardms(ctx, number: int):
    await ctx.message.delete()
    msgs = await ctx.message.channel.history(limit=number).flatten()
    for msg in msgs:
        if msg.author.name == ctx.message.author.name:
            await asyncio.sleep(3)
            await msg.delete()
    print("Executed cleardms")

    #scare
@bot.command()
async def scare(ctx):
    await ctx.message.delete()
    await ctx.send("https://media.discordapp.net/attachments/1053585082369179699/1057042872832106537/image0-2-1.gif")
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
async def purge(ctx):
    await ctx.message.delete()
    messages = await ctx.channel.history(limit=200).flatten()
    my_messages = [m for m in messages if m.author == ctx.author] 
    await ctx.channel.delete_messages(my_messages)
    print("Executed purge")

if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)
        TOKEN = config.get('token', '')

        if not TOKEN:
            eel.start('login.html', size=(900, 550))
        else:
            eel.start('index.html', size=(900, 550))
            launch()