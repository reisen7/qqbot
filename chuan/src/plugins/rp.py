from nonebot.typing import T_State
from nonebot.adapters import Event
from random import *
from nonebot.adapters.onebot.v11 import Bot, Message
from nonebot import on_keyword

# rp = on_command("今日人品", rule=to_me(), priority=5)
rp = on_keyword({'今日人品'})


@rp.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    replay = await get_randint()
    msg = at_ + " " + '今日人品为：' + replay
    msg = Message(msg)
    await rp.finish(message=msg)


async def get_randint():
    # print('called!')
    return str(randint(60, 100))
