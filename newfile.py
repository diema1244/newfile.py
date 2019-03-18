import discord
from discord.ext import commands
import asyncio
import ctx 
bot=commands.Bot(command_prefix='-')

client = discord.Client( )

@bot.command(pass_context=True)
async def game():
	await bot.change_presence(game=discord.Game(name='TWORZE  BOTA'))
	

@bot.command(pass_context=True)
async def refstat():
	await bot.change_presence(game=discord.Game(name='DOSTĘPNY'))
	


	
@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    
@bot.command(pass_context=True)
async def ping():
    await bot.say('PONG')
    await bot.say('NIE PINGUJ BEZ POWODU')
    
 
@bot.command(pass_context=True)
async def cześć():
	await bot.say('SZUKAM ODPOWIEDZI')
	await bot.say('................')
	await bot.say('................')
	await bot.say('................')
	await bot.say('ODPOWIEDŹ ZNALEZIONA')
	await bot.say('```SIEMA```')
    
    
@bot.command(pass_context=True)
async def nic():
	await bot.say('SZUKAM ODPOWIEDZI')
	await bot.say('.............')
	await bot.say('.............')
	await bot.say('.............')
	await bot.say('ODPOWIEDŹ ZNALEZIONA')
	await bot.say('```JA PISZĘ Z TOBĄ```')

@bot.command(pass_context=True)
async def siema():
	await bot.say('SZUKAM ODPOWIEDZI')
	await bot.say('............')
	await bot.say('............')
	await bot.say('............')
	await bot.say('ODPOWIEDŹ ZNALEZIONA')
	await bot.say('```HEJ CO ROBISZ??```')



@bot.command(pass_context=True)
async def aha():
	await bot.say('SZUKAM ODPOWIEDZI')
	await bot.say('............')
	await bot.say('............')
	await bot.say('............')
	await bot.say('ODPOWIEDŹ ZNALEZIONA')
	await bot.say('```AHA?```')
	await bot.say('```LUBISZ MNIE?```')

@bot.command(pass_context=True)
async def nie():
	await bot.say('SZUKAM ODPOWIEDZI')
	await bot.say('...............')
	await bot.say('...............')
	await bot.say('...............')
	await bot.say('ODPOWIEDŹ ZNALEZIONA')
	await bot.say('```:|```')
	await bot.say('```SZKODA```')

@bot.command(pass_context=True)
async def niestety():
	await bot.say('SZUKAM ODPOWIEDZI')
	await bot.say('...........')
	await bot.say('...........')
	await bot.say('...........')
	await bot.say('ODPOWIEDŻ ZNALEZIONA')
	await bot.say('```ŻYCIE!!```')
	await bot.say('```NIESTETY!!```')
bot.run('NTU2NTI2ODk4MzEwODA3NTcx.D3D5mw.qpQ9dJWiQe58XIcFTez9qlH_qIM')
