from nonebot.adapters.onebot.v11 import Message
from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError

jis = on_keyword({'每日一句'},priority=0, rule=to_me())


@jis.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await ji()
    try:
        await jis.send(Message(msg))

    except CQHttpError:
        pass


async def ji():
    url = 'https://api.ixiaowai.cn/api/ylapi.php'
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies)
    data = resp.text

    # time = '时间：' + data.get('time') + '       '
    # note = '中文：' + data.get('note') + '       '
    # content = '英文:' + data.get('content')
    # ur = 'http://api.52guleng.cn/api/wzztp/api.php?s=325&ss=00A8FF&nr=' + time+'\n'+note+'\n'+content
    # t = requests.get(ur).text
    # tu = f"[CQ:image,file={t}]"
    return data

# jis = on_keyword({'头像'})
#
#
# @jis.handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     # bot = nonebot.get_bot()
#     msg = await tou()
#     try:
#         await jis.send(Message(msg))
#
#     except CQHttpError:
#         pass
#
#
# async def tou():
#     url = 'https://api.66mz8.com/api/rand.portrait.php?type=%E5%A5%B3&format=json'
#     resp = requests.get(url)
#     data = resp.json()
#     u = data.get('pic_url')
#     tu = f"[CQ:image,file={u}]"
#     return tu


# jis = on_keyword({'垃圾分类'})
#
# @jis.handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     msg = await fen()
#     try:
#         await jis.send(Message(str(msg)))
#
#     except CQHttpError:
#         pass
#
# async def fen(*param):
#     url = ' https://api.66mz8.com/api/garbage.php?name='+param
#     resp = requests.get(url)
#     data = resp.json()
#     u=data.get('data')
#     y=data.get('name')+':'
#     return y,u

# jis = on_keyword({'ni'})
#
#
# @jis.handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     # bot = nonebot.get_bot()
#     msg = await yi()
#     try:
#         await jis.send(Message(str(msg)))
#
#     except CQHttpError:
#         pass
#
#
# async def yi():
#     url = ' https://api.66mz8.com/api/translation.php?info=I come from China'
#     resp = requests.get(url)
#     data = resp.json()
#     u = data.get('info')
#     y = data.get('fanyi')
#     return y, u
