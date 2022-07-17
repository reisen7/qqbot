from datetime import datetime

import nonebot
from nonebot.adapters import Event
from nonebot import on_command, logger, on_keyword
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message
from nonebot.internal.matcher import Matcher
from nonebot.internal.params import ArgPlainText, Arg
from nonebot.params import CommandArg

from ..ConfigSql import OperationMysql


shop = on_command('商店')

@shop.handle()
async def lookfor_shop(bot :Bot ,event :Event):

    await bot.send(event=event,message='正在获取商店物品')
    selectsql = "select name,price,atk,dep,gain,star from obj where gain = 'shop'"

    op_mysql = OperationMysql()
    shopObj = op_mysql.search_all(selectsql)

    shopAll = '    名称                价格  攻击力  防御力   品质' + '\n'
    i = 0
    while i < len(shopObj):
        shopAll += '{:　<9}'.format(str(shopObj[i]['name'])) + '{: <2}'.format(
            str(shopObj[i]['price'])) + '        ' + '{: <2}'.format(str(shopObj[i]['atk'])) + '        ' + '{: <2}'.format(
            str(shopObj[i]['dep'])) + '         ' + '{:　<3}'.format(shopObj[i]['star'] + '星') + '\n'
        i += 1
    print(shopAll)
    await shop.send(message=Message(shopAll))


by = on_command("购买")


@by.handle()
async def by_objecttoBag(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    print(plain_text)
    if plain_text:
        matcher.set_arg("obj", args)  # 如果用户发送了参数则直接赋值


@by.got("obj", prompt="想要买什么？")
async def object(event: Event, obj: Message = Arg(), obj_name: str = ArgPlainText("obj")):

    sql1 = "select id,name,price,atk,dep,gain,star from obj where gain = 'shop' and name ="
    select_sql = sql1 +"'"+ obj_name+"'"

    op_mysql = OperationMysql()
    byobj = op_mysql.search_one(select_sql)


    sql2 = 'select * from sign where user_qq = '
    # logger.info(sql+user_qq)
    sql_select = sql2+event.get_user_id()

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)

    if user == None:
        await by.send("请先进行签到~")

    elif user['integral'] >=  byobj['price']:
        sql3 = "insert into bag values (null,"+str(user['user_qq'])+' ,'+ str(byobj['id']) +' )'
        op_mysql = OperationMysql()
        op_mysql.insert_one(sql3)

        sql_update = 'update sign set  integral = integral -' + str(byobj['price']) + ' where user_qq =' + str(
            user['user_qq'])

        op_mysql = OperationMysql()
        op_mysql.updata_one(sql_update)
        await by.send('-'+str(byobj['price'])+'枚金币  '+'购买成功欢迎下次光临喵~')

    else:
        await by.send("您的金币不够啦~请输入'金币获取'来查看获取方式吧")


bag = shop = on_command('我的背包',aliases={"我的金币",'查看背包'})
@bag.handle()
async def lookBag(bot:Bot , event:Event):

    sql = 'select * from sign where user_qq = '
    sql_select = sql+event.get_user_id()

    op_mysql = OperationMysql()
    user = op_mysql.search_one(sql_select)

    sql_bag = 'select  count(*)sum, name from bag b INNER join obj o on b.obj_id = o.id WHERE user_qq ='+ event.get_user_id() +" group by name"

    print(sql_bag)
    op_mysql = OperationMysql()
    bags = op_mysql.search_all(sql_bag)

    if user:
        message = '你的金币: ' + str(user['integral']) + '\n'

        b = ''
        i = 0
        while i < len(bags):
            b += bags[i]['name'] + '  *' + str(bags[i]['sum']) + '\n'
            i += 1

        message = message + b
        await bot.send(event, Message(message))
    else:
        await by.send("请先进行签到~")

