#I dont care its a shitty selfbot I know but atleast I didnt skid it like nightly
import asyncio
import discord
from discord.ext import commands
import os
from colorama import Fore, Back, Style
from mailtm import Email
import random
import requests
from plyer import notification
import subprocess
import json

verexta = commands.Bot(command_prefix='!', self_bot=True)

print(Fore.GREEN + "oooooo     oooo                                              .             ")
print(Fore.RED + " `888.     .8'                                             .o8             ")
print(Fore.BLUE + "  `888.   .8'    .ooooo.  oooo d8b  .ooooo.  oooo    ooo .o888oo  .oooo.   ")
print(Fore.MAGENTA + "   `888. .8'    d88' `88b `888""8P   d88' `88b  `88b..8P'    888   `P  )88b  ")
print(Fore.CYAN + "    `888.8'     888ooo888  888     888ooo888    Y888'      888    .o8P888  ")
print(Fore.YELLOW + "     `888'      888    .o  888     888    .o  . o8888b     888 . d8(  888  ")
print(Fore.WHITE + "      `8'       `Y8bod8P' d888b    `Y8bod8P' o88'   888o   888   `Y888""8o    1.1.0 | STABLE")



    


with open('config.json') as f:
    config = json.load(f)
token = config['token']

@verexta.event
async def on_connect():
    notification.notify(
    title = 'Verexta',
    message = 'Logged in succesfully!',
    app_icon = None,
    timeout = 10,
)

    #Pages
@verexta.command()
async def cmds(ctx):
    await ctx.message.delete()
    await ctx.send("**List of all cmds**\n *1:*  troll\n *2:*  useful\n *3:*  Credits\n *4:*  Raid\n *5:*  Misc")
    print("Executed cmds")


    #troll
@verexta.command()
async def troll(ctx):
    await ctx.send("**Trolling CMDS**\n *1:*  textchunk\n *2:*  scare\n *3:*  fucku\n *4:*  ghostping")
    print("Executed Troll")


    #useful
@verexta.command()
async def useful(ctx):
    await ctx.message.delete()
    await ctx.send("**USEFUL CMDS**\n *1:*  mail\n *2:*  whois\n *3:*  nrand (num1 num2)\n *4:*  cleardms\n *5:*  exit")
    print("Executed Useful")


    #credits
@verexta.command()
async def credits(ctx):
    await ctx.message.delete()
    await ctx.send("**Made by if.0n**\n Inspired by Ethone xyss is a G btw\n No this is not skidded from anything all my code lol")
    print("Executed Credits")


    #raid
@verexta.command()
async def raid(ctx):
    await ctx.message.delete()
    await ctx.send("**RAID CMDS**\n *1:*  DelChannels\n *2:*  Purge\n *3:*  Cspam\n *4:*  webhook (WEBHOOK, MESSGAE, NUM OF MESSAGES)")
    print("Executed Raid")

    #MISC
@verexta.command()
async def misc(ctx):
    await ctx.message.delete()
    await ctx.send("**MISC CMDS**\n *1:* Poll\n *2:* Lenny\n *3:* nick")
    print("Executed MISC")

    #cmds

@verexta.command()
async def exit(ctx):
    await ctx.message.delete()
    verexta.close()

@verexta.command()
async def ghostping(ctx, *, args):
    await ctx.message.delete()
    await ctx.send('', delete_after=0.00005)
    print("Executed ghostping")

@verexta.command()
async def webhook(ctx, webhook_url, message, number_of_messages):
    await ctx.message.delete()
    for i in range(int(number_of_messages)):
        response = requests.post(webhook_url, json={'content': message})
    print("Executed webhook")

    #textchunks
@verexta.command()
async def textchunk(ctx):
    await ctx.message.delete()
    await ctx.send("wrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahegauohpgapuhogeauegruagopreuaogeuoagruhoasgerhuasgrehuoguhosearguhgaseruhasgrasgpuhhpugsarehugpresahupgsaerhpusagerhugpsarehpusagreughsaresagraugpraguerusaghersguhrspgreuspgrusughsuhghugresuhgreuhgreuhgrespuhrgepughsrugw983570y5w9780yu2978ughjwuntrwu4586kjtbroiubnriubnrtuibnrutibnrtubnrtuibrtbuirjbnuritburtbhtruibtrbuibuitbruibhtjuirhtubtrhbutrbhtrubhtubburbjurbjrtburtjbutjbtubjtubtjbutbjtubtjbtbutjbtubjtubtjbwrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahegauohpgapuhogeauegruagopreuaogeuoagruhoasgerhuasgrehuoguhosearguhgaseruhasgrasgpuhhpugsarehugpresahupgsaerhpusagerhugpsarehpusagreughsaresagraugpraguerusaghersguhrspgreuspgrusughsuhghugresuhgreuhgreuhgrespuhrgepughsrugw983570y5w9780yu2978ughjwuntrwu4586kjtbroiubnriubnrtuibnrutibnrtubnrtuibrtbuirjbnuritburtbhtruibtrbuibuitbruibhtjuirhtubtrhbutrbhtrubhtubburbjurbjrtburtjbutjbtubjtubtjbutbjtubtjbtbutjbtubjtubtjbwrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahegauohpgapuhogeauegruagopreuaogeuoagruhoasgerhuasgrehuoguhosearguhgaseruhasgrasgpuhhpugsarehugpresahupgsaerhpusagerhugpsarehpusagreughsaresagraugpraguerusaghersguhrspgreuspgrusughsuhghugresuhgreuhgreuhgrespuhrgepughsrugw983570y5w9780yu2978ughjwuntrwu4586kjtbroiubnriubnrtuibnrutibnrtubnrtuibrtbuirjbnuritburtbhtruibtrbuibuitbruibhtjuirhtubtrhbutrbhtrubhtubburbjurbjrtburtjbutjbtubjtubtjbutbjtubtjbtbutjbtubjtubtjbwrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahegauohpgapuhogeauegruagopreuaogeuoagruhoasgerhuasgrehuoguhosearguhgaseruhasgrasgpuhhpugsarehugpresahupgsaerhpusagerhugpsarehpusagreughsaresagraugpraguerusaghersguhrspgreuspgrusughsuhghugresuhgreuhgreuhgrespuhrgepughsrugw983570y5w9780yu2978ughjwuntrwu4586kjtbroiubnriubnrtuibnrutibnrtubnrtuibrtbuirjbnuritburtbhtruibtrbuibuitbruibhtjuirhtubtrhbutrbhtrubhtubburbjurbjrtburtjbuwrgwrgrgikjwru9oigjuaiegopruhagouirhngaruygohpahpaougrhpaguphuaeruohaeruahefrrhrthrthrththh")
    print("Executed textchunk")

    #cspam
async def create_spam_channels(ctx, channel_name, number_of_channels):
    await ctx.message.delete()
    guild = ctx.guild
    for i in range(number_of_channels):
        await asyncio.sleep(random.uniform(0.4, 0.7))
        await guild.create_text_channel(f"{channel_name}-{i}")

    #cspam
@verexta.command()
async def cspam(ctx, channel_name: str, number_of_channels: int):
    await ctx.message.delete()
    await create_spam_channels(ctx, channel_name, number_of_channels)
    await ctx.send(f"Successfully created {number_of_channels} channel(s) named {channel_name}.")
    print("Executed cspam")

    #Delete Channels
@verexta.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.delete()
    print("Executed DelChannels")

    #ClearDms
@verexta.command()
async def cleardms(ctx, number: int):
    await ctx.message.delete()
    msgs = await ctx.message.channel.history(limit=number).flatten()
    for msg in msgs:
        if msg.author.name == ctx.message.author.name:
            await asyncio.sleep(3)
            await msg.delete()
    print("Executed cleardms")

    #scare
@verexta.command()
async def scare(ctx):
    await ctx.message.delete()
    await ctx.send("https://media.discordapp.net/attachments/1053585082369179699/1057042872832106537/image0-2-1.gif")
    print("Executed scare")

    #fucku
@verexta.command()
async def fucku(ctx):
    await ctx.message.delete()
    await ctx.send("https://media.discordapp.net/attachments/853726500371955742/869938928050921542/image0.gif")
    print("Executed fucku")

    #nrand
@verexta.command()
async def nrand(ctx, num1: int, num2: int):
    await ctx.message.delete()
    await ctx.send(f"Your Number is: {random.randint(num1, num2)}")
    print("Executed nrand")

    #Lenny
@verexta.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)
    print("Executed Lenny")

    #Poll
@verexta.command()
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
@verexta.command()
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
@verexta.command()
async def whois(ctx, user: discord.User):
    await ctx.message.delete()
    await ctx.send(f"Username: {user.name}#{user.discriminator}\nID: {user.id}")
    print("Executed whois")

    #nick
@verexta.command()
async def nick(ctx, *, nickname: str):
    await ctx.message.delete()
    try:
        await ctx.message.author.edit(nick=nickname)
        await ctx.send(f'Nickname changed to {nickname}!')
    except discord.Forbidden:
        await ctx.send("I don't have permission to change your nickname.")
        print("Executer nick")

    #Purge
@verexta.command()
async def purge(ctx):
    await ctx.message.delete()
    messages = await ctx.channel.history(limit=200).flatten()
    my_messages = [m for m in messages if m.author == ctx.author] 
    await ctx.channel.delete_messages(my_messages)
    print("Executed purge")

verexta.run(token)