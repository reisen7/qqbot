
from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Bot, Message
import requests
from aiocqhttp.exceptions import Error as CQHttpError
from .ConfigSql import OperationMysql

da = on_keyword({'二次元'}, rule=to_me())

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



