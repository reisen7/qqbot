from nonebot.adapters.onebot.v11 import Message
from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError

lishi = on_keyword({'历史今天'}, priority=0, rule=to_me())


@lishi.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await ji()
    try:
        await lishi.send(Message(msg))
    except CQHttpError:
        pass


async def ji():
    url = 'http://api.wpbom.com/api/today.php'
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).text
    # ur = 'http://api.52guleng.cn/api/wzztp/api.php?s=325&ss=00A8FF&nr=' + resp
    # t=requests.get(ur).text
    # tu = f"[CQ:image,file={t}]"
    return resp


