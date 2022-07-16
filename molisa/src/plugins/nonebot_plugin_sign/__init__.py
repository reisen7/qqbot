from datetime import datetime

import nonebot
from nonebot.adapters import Event
from nonebot import on_command, logger, on_keyword
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message
from .config import OperationMysql


sign = on_command('签到')


@sign.handle()
async def sign_user(bot: Bot, event: Event):
    user_qq = event.get_user_id()
    sql = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)

    time = datetime.now().strftime("%Y-%m-%d")
    # logger.info(time)
    # logger.info(user['last_insertDate'].strftime("%Y-%m-%d"))
    if user:
       if user['last_insertDate'].strftime("%Y-%m-%d") == time:
           # sql_update = 'update sign set count = count + ' + '1' + ', last_insertDate = now(), integral = integral + 1' + ' where user_qq =' + user_qq
           # logger.info(sql_update)
           #
           # op_mysql = OperationMysql()
           # op_mysql.updata_one(sql_update)
           #
           # logger.info("成功")
           # logger.info("已经签过了")
           at_ = "[CQ:at,qq={}]".format(user_qq)
           message = at_ + '今天已经签过到了哦~'+'\n'+'发送‘金币获取’查看获取金币的方法'
           await bot.send(event, Message(message))

       else:
           sql_update = 'update sign set count = count + ' + '1, ' + 'last_insertDate = now(), integral = integral + 1' + ' where user_qq =' + user_qq
           logger.info(sql_update)

           op_mysql = OperationMysql()
           op_mysql.updata_one(sql_update)

           logger.info("成功")
           message = await success(user_qq)
           await bot.send(event, Message(message))
    else:
        sql_insert = 'insert into sign values ' + '( ' + user_qq + ',' + '1, now(),1)'
        logger.info(sql_insert)

        op_mysql = OperationMysql()
        op_mysql.insert_one(sql_insert)

        logger.info("签到成功")

        message = await success(user_qq)
        await bot.send(event, Message(message))



async def success(user_qq: str):
    sql = 'select * from sign where user_qq = '
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)
    at_ = "[CQ:at,qq={}]".format(user_qq)
    logger.info(user['last_insertDate'])
    message = at_ + '签到成功' +'\n'+ '已连续签到 ' + str(user['count']) +' 天'+'\n'+'金币有 '+ str(user['integral']) +'\n'+'最后一次签到时间：'+str(user['last_insertDate'].strftime("%Y-%m-%d %H:%M:%S"))
    message = message + '\n' + '发送‘个人信息’即可查看'

    return message


info = on_command('个人信息', aliases={'我的背包', '我的金币'})
@info.handle()
async def info_select(bot: Bot, event: Event):
    user_qq = event.get_user_id()
    sql = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql+user_qq

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)
    at_ = "[CQ:at,qq={}]".format(user_qq)
    message = at_ +'\n' + '已连续签到 ' + str(user['count']) + ' 天' + '\n' + '金币有 ' + str(
        user['integral']) + '\n' + '最后一次签到时间：' + str(user['last_insertDate'].strftime("%Y-%m-%d %H:%M:%S"))
    await bot.send(event, Message(message))

corn = on_command('金币获取')
@corn.handle()
async def corn_method(bot: Bot, event: Event):
    await bot.send(event, Message('签到获取，玩游戏获取，联系我主人更改数据库'))