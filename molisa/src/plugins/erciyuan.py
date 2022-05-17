
from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Bot, Message
import requests
from aiocqhttp.exceptions import Error as CQHttpError

da = on_keyword({'二次元'}, priority=0, rule=to_me())

@da.handle()
async def h(bot: Bot, event: Event, state: T_State):
    msg = await se()
    try:
        await da.send(Message(msg))

    except CQHttpError:
        pass


async def se():
    url = 'https://api.ixiaowai.cn/api/api.php?return=json'
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).text
    x = resp.split(',')
    y = x[1].split('"')
    # test = resp['imgurl']
    test = y[3].replace("\\", "")
    tu = f"[CQ:image,file={test}]"
    return tu



