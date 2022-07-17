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
from .ConfigSql import OperationMysql

da = on_command('原批',rule=to_me(),aliases={"原神烧鸡","原批"})

@da.handle()
async def h(bot: Bot, event: Event, state: T_State):

    user_qq = event.get_user_id()
    sql = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)

    if user:
        if user['integral'] == 0:
            await da.send(Message('你的金币不足哦~快向小奏签到获取吧'))

        else:

            try:

                msg = await se()
                await da.send(Message('金币-1'+msg))

                sql_update = 'update sign set  integral = integral -' + '1' + ' where user_qq =' + str(
                    user_qq)

                op_mysql = OperationMysql()
                op_mysql.updata_one(sql_update)

            except CQHttpError:
                await da.send(Message('现在暂时没有图片哦~'))

    else:
        await da.send(Message('你的金币不足哦~快向小奏签到获取吧'))


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



