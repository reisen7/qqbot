from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Event
from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Bot

test = on_command('你好', rule=to_me(), priority=0)


@test.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["city"] = args
        weather=await get_hello()
        await test.send(weather)


async def get_hello():
    return '你好'


who = on_keyword({'你是'}, rule=to_me())


@who.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["city"] = args
        weather=await get_weather()
        await test.send(weather)


async def get_weather():
    return '我是小奏'


wanan = on_command("晚安")


@wanan.handle()
async def wanan_first_send(event:Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["city"] = args
        weather=await get_wanan()
        await wanan.send(weather)


async def get_wanan():
    return "晚安喵~小奏要睡觉了"


zaoan = on_command("早安")


@zaoan.handle()
async def wanan_first_send(event:Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["city"] = args
        weather=await get_zaoan()
        await wanan.send(weather)


async def get_zaoan():
    return "早安喵~小奏早就起了"


huanying = on_command("欢迎", rule=to_me())


@huanying.handle()
async def wanan_first_send(event:Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["city"] = args
        weather=await get_huanying()
        await wanan.send(weather)


async def get_huanying():
    return "谢迎喵~ 艾特我回复菜单可以看更多功能哦"


wenhao = on_command("？")


@wenhao.handle()
async def wanan_first_send(event:Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["city"] = args
        weather=await get_wenhao()
        await wanan.send(weather)


async def get_wenhao():
    return "?~ 喵喵喵~"