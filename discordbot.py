from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID_WELCOME = 710111629806927943
ID_ROLE_WELCOME =710161784190795808
EMOJI_WELCOME = '✅'
dateTimeList = [
'01:00',
'05:00',
'09:00',
'13:00',
'17:00',
'21:00',
]



@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def pop(ctx):
    await ctx.send('pong')


bot.run(token)

