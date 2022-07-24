import random

import aiocqhttp
from nonebot.adapters.onebot.v11 import Message
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.plugin import on_command
import requests
import re
from nonebot.rule import to_me
import os
from .ConfigSql import OperationMysql

os.environ['NO_PROXY'] = 'stackoverflow.com'


yulu = on_command('美女', rule=to_me())


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):


    user_qq = event.get_user_id()
    sql = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)


    if user:
        if user['integral'] <= 0:
            await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))

        else:

            try:

                msg = await qian()
                print(msg)
                await yulu.send(Message('金币-1'+msg))
                sql_update = 'update sign set  integral = integral -' + '1' + ' where user_qq =' + str(
                    user_qq)

                op_mysql = OperationMysql()
                op_mysql.updata_one(sql_update)

            except CQHttpError:
                await yulu.send(Message('发送失败，请再试一次'))

    else:
        await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))




async def qian():
    url = 'https://imgapi.cn/api.php?zd=mobile&fl=meizi&gs=json'
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).text
    x = resp.split(',')
    y = x[1].split('"')
    # test = resp['imgurl']
    test = y[3].replace("\\", "")
    tu = f"[CQ:image,file={test}]"
    return tu


yulu = on_command('烧鸡', aliases={ "美少女", "涩图", "色图"}, rule=to_me())


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):

    user_qq = event.get_user_id()
    sql = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)

    if user:
        if user['integral'] <= 0:
            await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))

        else:

            try:

                a = random.randint(0, 1)
                if a == 1:
                    msg = await mei()
                if a == 0:
                    msg = await heisi()
                print(msg)
                await yulu.send(Message('金币-1'+msg))
                sql_update = 'update sign set  integral = integral -' + '1' + ' where user_qq =' + str(
                    user_qq)

                op_mysql = OperationMysql()
                op_mysql.updata_one(sql_update)

            except CQHttpError:
                await yulu.send(Message('发送失败，请再试一次'))

    else:
        await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))



async def mei():
    url = 'https://imgapi.cn/cos.php?return=url'
    proxies = {"http": None, "https": None}
    try:
        resp = requests.get(url=url, verify=False, proxies=proxies).url

        repy = [
            {
                "type": "image",
                "data": {
                    "file": resp
                }
            }
        ]

    except BaseException:
        tu = '现在暂时没有烧鸡呢~请稍后再试'

    # x = resp.split(',')
    # y = x[1].split('"')
    # # test = resp['imgurl']
    # test = y[3].replace("\\", "")

    return str(aiocqhttp.Message(repy))


async def heisi():
    url = 'https://imgapi.cn/cos2.php?return=json'
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).text
    x = resp.split(',')
    y = x[1].split('"')
    # test = resp['imgurl']
    test = y[3].replace("\\", "")

    repy = [
        {
            "type": "image",
            "data": {
                "file": test
            }
        }
    ]

    return str(aiocqhttp.Message(repy))


yulu = on_command('湿身', rule=to_me())


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):

    user_qq = event.get_user_id()
    sql = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)


    if user:
        if user['integral'] <= 0:
            await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))

        else:

            try:

                msg = await rousi()
                print(msg)
                await yulu.send(Message('金币-1'+msg))
                sql_update = 'update sign set  integral = integral -' + '1' + ' where user_qq =' + str(
                    user_qq)

                op_mysql = OperationMysql()
                op_mysql.updata_one(sql_update)

            except CQHttpError:
                await yulu.send(Message('发送失败，请再试一次'))

    else:
        await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))
    
    


async def rousi():
    url = "https://api.r10086.com/img-api.php?type=P%E7%AB%99%E7%B3%BB%E5%88%972"
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).url
    # x = resp.split(',')
    # y = x[1].split('"')
    # # test = resp['imgurl']
    # test = y[3].replace("\\", "")

    repy = [
        {
            "type": "image",
            "data": {
                "file": resp
            }
        }
    ]

    return str(aiocqhttp.Message(repy))


yulu = on_command('女同', priority=0)


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):

    user_qq = event.get_user_id()
    sql = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)


    if user:
        if user['integral'] <= 0:
            await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))

        else:

            try:

                msg = await baisi()
                print(msg)
                await yulu.send(Message('金币-1'+msg))
                sql_update = 'update sign set  integral = integral -' + '1' + ' where user_qq =' + str(
                    user_qq)

                op_mysql = OperationMysql()
                op_mysql.updata_one(sql_update)

            except CQHttpError:
                await yulu.send(Message('发送失败，请再试一次'))

    else:
        await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))



async def baisi():
    url = "https://api.r10086.com/img-api.php?type=%E6%A9%98%E9%87%8C%E6%A9%98%E6%B0%94%E6%A8%AA%E5%B1%8F%E7%B3%BB%E5%88%971"
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).url
    # x = resp.split(',')
    # y = x[1].split('"')
    # # test = resp['imgurl']
    # test = y[3].replace("\\", "")

    repy = [
        {
            "type": "image",
            "data": {
                "file": resp
            }
        }
    ]

    return str(aiocqhttp.Message(repy))


yulu = on_command('其他',priority=0)


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):

    user_qq = event.get_user_id()
    sql = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)


    if user:
        if user['integral'] <= 0:
            await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))

        else:

            try:

                msg = await qitas()
                print(msg)
                await yulu.send(Message('金币-1'+msg))
                sql_update = 'update sign set  integral = integral -' + '1' + ' where user_qq =' + str(
                    user_qq)

                op_mysql = OperationMysql()
                op_mysql.updata_one(sql_update)

            except CQHttpError:
                await yulu.send(Message('发送失败，请再试一次'))

    else:
        await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))




async def qitas():
    url = "https://api.r10086.com/img-api.php?type=CG%E7%B3%BB%E5%88%973"
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).url
    # x = resp.split(',')
    # y = x[1].split('"')
    # # test = resp['imgurl']
    # test = y[3].replace("\\", "")

    repy = [
        {
            "type": "image",
            "data": {
                "file": resp
            }
        }
    ]

    return str(aiocqhttp.Message(repy))



yulu = on_command('cos')


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):

    user_qq = event.get_user_id()
    sql = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)


    if user:
        if user['integral'] <= 0:
            await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))

        else:

            try:

                msg = await cos()
                print(msg)
                await yulu.send(Message('金币-1'+msg))
                sql_update = 'update sign set  integral = integral -' + '1' + ' where user_qq =' + str(
                    user_qq)

                op_mysql = OperationMysql()
                op_mysql.updata_one(sql_update)

            except CQHttpError:
                await yulu.send(Message('发送失败，请再试一次'))

    else:
        await yulu.send(Message('你的金币不足哦~快向小奏签到获取吧'))




async def cos():
    url = "https://api.r10086.com/img-api.php?type=%E6%97%A5%E6%9C%ACCOS%E4%B8%AD%E5%9B%BDCOS"
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).url
    # x = resp.split(',')
    # y = x[1].split('"')
    # # test = resp['imgurl']
    # test = y[3].replace("\\", "")

    repy = [
        {
            "type": "image",
            "data": {
                "file": resp
            }
        }
    ]

    return str(aiocqhttp.Message(repy))