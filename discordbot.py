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
'02:12',
]



@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def pop(ctx):
    await ctx.send('pong')

@bot.command()
async def 草蛇(ctx):
    await ctx.send('ジャローダ')

@client.event
async def on_ready():
    print('ready')

# 指定時間に走る処理
async def SendMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')

# 30秒に一回ループ
@tasks.loop(seconds=30)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now in dateTimeList :
        print(now)
        await SendMessage()
        #該当時間だった場合は２重に投稿しないよう３０秒余計に待機
        await asyncio.sleep(30)



#ループ処理
time_check.start()


bot.run(token)

