#The imports for discord
import os, discord, wikipedia, math, googletrans
from discord.ext import commands
from googletrans import Translator
import requests
import json

my_secret = os.environ['token']

#The prefix for each command "!bub command"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!bub ', intents=intents)

#This is to make sure that the bot is online when we turn it on
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#Math Section
@bot.command()
async def add(ctx, x, y):
    w = int(x)
    z = int(y)
    embed = discord.Embed(
        title='Math: Addition',
        description=f"```md\n{x + ' plus ' + y + ' equals ' + str(w + z)}```",
        colour=discord.Colour.yellow())
    embed.set_footer(text='Hope that helped!')
    await ctx.send(embed=embed)

@bot.command()
async def sub(ctx, x, y):
    w = int(x)
    z = int(y)
    embed = discord.Embed(
        title='Math: Subtraction',
        description=
        f"```md\n{x + ' subtract ' + y + ' equals ' + str(w - z)}```",
        colour=discord.Colour.yellow())
    embed.set_footer(text='Hope that helped!')
    await ctx.send(embed=embed)

@bot.command()
async def multi(ctx, x, y):
    w = int(x)
    z = int(y)
    embed = discord.Embed(
        title='Math: Multiplication',
        description=f"```md\n{x + ' times ' + y + ' equals ' + str(w * z)}```",
        colour=discord.Colour.yellow())
    embed.set_footer(text='Hope that helped!')
    await ctx.send(embed=embed)

@bot.command()
async def div(ctx, x, y):
    w = int(x)
    z = int(y)
    embed = discord.Embed(
        title='Math: Division',
        description=
        f"```md\n{x + ' divided ' + y + ' equals ' + str(w / z)}```",
        colour=discord.Colour.yellow())
    embed.set_footer(text='Hope that helped!')
    await ctx.send(embed=embed)

@bot.command()
async def pow(ctx, x, y):
    w = int(x)
    z = int(y)
    total = math.pow(w, z)
    embed = discord.Embed(
        title='Math: Exponent',
        description=
        f"```md\n{x + ' to the power of ' + y + ' equals ' + str(total)}```",
        colour=discord.Colour.yellow())
    embed.set_footer(text='Hope that helped!')
    await ctx.send(embed=embed)

@bot.command()
async def logTen(ctx, x):
    w = int(x)
    total = math.log10(w)
    embed = discord.Embed(
        title='Math: LogTen',
        description=f"```md\n{x + ' log of ten equals ' + str(total)}```",
        colour=discord.Colour.yellow())
    embed.set_footer(text='Hope that helped!')
    await ctx.send(embed=embed)

@bot.command()
async def logTwo(ctx, x):
    w = int(x)
    embed = discord.Embed(
        title='Math: LogTwo',
        description=
        f"```md\n{x + ' log of two equals ' + str(math.log2(w))}```",
        colour=discord.Colour.yellow())
    embed.set_footer(text='Hope that helped!')
    await ctx.send(embed=embed)

#English Section
@bot.command()
async def wordOfDay(ctx):
    await ctx.send('https://www.merriam-webster.com/word-of-the-day')

@bot.command()
async def define(ctx, x):
    await ctx.send('https://www.merriam-webster.com/dictionary/' + x)

@bot.command()
async def exampleSentence(ctx, x):
    await ctx.send('https://sentence.yourdictionary.com/' + x)

@bot.command()
async def synon(ctx, x):
    await ctx.send('https://www.merriam-webster.com/thesaurus/' + x)

#@bot.command()
#async def translate():
#work in progress

#Wikipedia Section
@bot.command()
async def wikiUrl(ctx, url):  #Gets the desired Wikipedia URL
    url = url.lower().replace(" ", "_").replace("  ", "")
    await ctx.send('https://en.wikipedia.org/wiki/' + url)

@bot.command()
async def wikiSummary(ctx, url):  #Gets the desired Wikipedia summary
    try:
        url = url.lower().replace(' ', '_').replace('  ', '_')
        summary = wikipedia.summary(url, chars=1950)
        await ctx.send(f"{summary}\n\nhttps://en.wikipedia.org/wiki/{url}")
    except:
        search = str(wikipedia.search(url, suggestion=True)).replace(
            '(', '').replace("'", "").replace('[', '').replace(']', '')
        await ctx.send(
            f"I can't seem to find a summary for that . . . Did you mean {search}"
        )

@bot.command()
async def wikiRandom(ctx):  #Gets a random Wikipedia Article
    randomTitle = wikipedia.random()  #returns a random article
    randomSummary = wikipedia.summary(randomTitle,
                                      chars=1950)  #summary for article
    url = randomTitle.replace(' ', '_')
    await ctx.send(
        f"**{randomTitle}** \n\n{randomSummary}\n\nhttps://en.wikipedia.org/wiki/{url}"
    )
#get quotes from zenquotes API 
def get_quote():
     response = requests.get("https://zenquotes.io/api/random")
     json_data = json.loads(response.text)
     quote = json_data[0]['q'] + " -" + json_data[0]['a']
     return(quote)

@bot.command()
async def motivate(ctx):
   quote = get_quote()
   await ctx.send(f"**{quote}**")
  
#This is to help us when we do too many commands at once discord does limit it
try:
    bot.run(os.getenv('token'))
except:
    os.system("kill 1")