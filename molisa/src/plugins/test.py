import aiocqhttp
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Event
from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Bot, Message

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

    img = "https://gchat.qpic.cn/gchatpic_new/3410530177/993105896-3151105555-9E0F5BFDEA84C60319775F8FCAD66804/0?term=3,subType=1"
    repy = [
        {
            "type": "image",
            "data": {
                "file": img
            }
        }
    ]
    await wanan.send(Message(str(aiocqhttp.Message(repy))))


wenhao = on_command("哈哈")

@wenhao.handle()
async def wanan_first_send(event:Event, state: T_State):

    await wanan.send(Message('笑你妈'))

zhuren = on_keyword({'主人'}, rule=to_me())


@zhuren.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await test.send(Message("我主人是魔理沙"))


wenhao = on_command("小游戏")

@wenhao.handle()
async def wanan_first_send(event:Event, state: T_State):

    await wanan.send(Message('随机唐可可(可获得金币)，五子棋，围棋，黑白棋，象棋对战，象棋人机(lv1~8)，扫雷'))