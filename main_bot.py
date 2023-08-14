import discord
import asyncio
import datetime
import os
from pytz import timezone
from discord.ext import commands, tasks
from CPNG_price.services.logic import cpng_price
from CPNG_price.parser import msg_template, only_mention_msg_template

CHANNEL_ID = os.environ['CHANNEL_ID']
TOKEN = os.environ['TOKEN']
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

engine = commands.Bot(command_prefix='!', intents=intents)


@engine.event
async def on_ready():
    print(f'{engine.user.name}봇 기동')


@engine.event
async def on_message(message):
    if message.author == engine.user:
        return

    if engine.user.mentioned_in(message):
        if '쿠팡' in message.content.lower():
            data = cpng_price()
            msg = msg_template(data)
            await message.channel.send(f'안녕하세요 {message.author.mention}님! :wink: {msg}')
        else:
            msg = only_mention_msg_template()
            await message.channel.send(f'안녕하세요 {message.author.mention}님! {msg}')

    await engine.process_commands(message)


@tasks.loop(hours=12)
async def send_messages():
    channel = engine.get_channel(CHANNEL_ID)
    if channel:
        data = cpng_price()
        msg = msg_template(data)
        await channel.send(msg)
    else:
        print(f"{CHANNEL_ID}: 채널 ID 확인 요망")


@send_messages.before_loop
async def before_send_messages():
    await engine.wait_until_ready()
    now = datetime.datetime.now(timezone('Asia/Seoul'))
    target_time_am = now.replace(hour=9, minute=0, second=0, microsecond=0)
    target_time_pm = now.replace(hour=21, minute=0, second=0, microsecond=0)

    if now > target_time_am:
        target_time_am += datetime.timedelta(days=1)
    if now > target_time_pm:
        target_time_pm += datetime.timedelta(days=1)

    seconds_until_am = (target_time_am - now).seconds
    seconds_until_pm = (target_time_pm - now).seconds

    await asyncio.sleep(min(seconds_until_am, seconds_until_pm))


async def start_bot():
    await engine.start(TOKEN)

# 배치를 위한 루프 처리
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())