from nonebot import on_keyword, on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.onebot.v11.message import MessageSegment
import requests
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError
yulu = on_keyword({'今日哔哩哔哩排行'},priority=0, rule=to_me())


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await ji()
    try:
        await yulu.send(msg)

    except CQHttpError:
        pass


async def ji():
    url = 'https://api.muxiuge.cn/API/bilitop.php?n='
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).json()
    data=resp['data'][0]
    data1=resp['data'][1]
    data2=resp['data'][2]
    data3=resp['data'][3]
    data4 = resp['data'][4]
    return str('1.'+data+'\n2.'+data1+'\n3.'+data2+'\n4.'+data3+'\n5.'+data4)