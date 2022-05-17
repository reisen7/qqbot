import random
import requests
import json
import os
from nonebot.typing import T_State
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Bot, Message
import requests
from nonebot.plugin import on_command
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.rule import to_me
da = on_command('原神',rule=to_me(),aliases={"原神烧鸡","原批", "genshin"})

@da.handle()
async def h(bot: Bot, event: Event, state: T_State):
    msg = await se()
    try:
        await da.send(Message(msg))

    except CQHttpError:
        pass


class WebSpider(object):
    def __init__(self):
        self.url = 'https://bbs-api.mihoyo.com/post/wapi/getForumPostList?forum_id=49'

        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/92.0.4515.107 Safari/537.36'
    }

    def parse(self):
        img_dict_data = {}


async def se():
    self=WebSpider()
    proxies = {"http": None, "https": None}
    res = requests.get(self.url, headers=self.headers, verify=False, proxies=proxies).content.decode('utf-8')
    res = json.loads(res)
    res = res['data']['list']
    subject_name = [i['post']['subject'] for i in res]
    cover_url = [i['post']['cover'] for i in res]  # 遍历图片的URL地址
    # print(cover_url, subject_name)
    # 获取对应的标题以及图片地址

    tu = f"[CQ:image,file={cover_url[random.randint(0,len(cover_url)-1)]}]"
    return tu


