import random
from datetime import datetime

import requests
from nonebot.internal.params import Arg, ArgPlainText
from nonebot.matcher import Matcher
from nonebot import on_command, on_message, on_regex, export, logger
from nonebot.params import CommandArg, RegexMatched
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11.event import MessageEvent, GroupMessageEvent
from nonebot.adapters.onebot.v11.utils import unescape
from nonebot.adapters.onebot.v11.permission import GROUP_OWNER, GROUP_ADMIN, PRIVATE_FRIEND,GROUP_MEMBER
from .data_source import OPTIONS, word_bank as wb
from .util import parse, parse_cmd
from .MyBotSql import OperationMysql
reply_type = "random"

export().word_bank = wb

wb_matcher = on_command('', rule=to_me(), priority=20)
word = None


@wb_matcher.handle()
async def _(bot: Bot, event: MessageEvent):
    if isinstance(event, GroupMessageEvent):
        index = event.group_id
    else:
        index = event.user_id

    message = str(event.get_message()).strip()
    print(message)

    if message == '':
        gun = '小奏在哟~'
        await bot.send(event, message=gun)
    else:
        msgs = wb.match(index, unescape(message))
        if msgs:
            if reply_type == 'random':
                msg = Message(unescape(parse(msg=random.choice(msgs),
                                             nickname=event.sender.card or event.sender.nickname,
                                             sender_id=event.sender.user_id)))
                print(msg)
                await bot.send(event, message=Message(msg))

            else:
                for msg in msgs:
                    await bot.send(event,
                                   message=Message(
                                       unescape(
                                           parse(msg=msg,
                                                 nickname=event.sender.card or event.sender.nickname,
                                                 sender_id=event.sender.user_id)
                                       )
                                   )
                                   )
        else:
            # words = response(message)
            # print(words)
            words = None
            word1 = await chat(message)
            word2 = await ch(message)
            print(word1)
            print(word2)

            # ran = random.randint(0, 1)
            # if ran == 1:
            #     words = word1
            # if ran == 0:
            #     words = word2

            await bot.send(event, message=Message(word1))


async def chat(city : str):
    cityname = city
    url='http://api.qingyunke.com/api.php?key=free&appid=0&msg='+cityname
    proxies = {"http": None, "https": None}
    answer = requests.get(url, verify=False, proxies=proxies).json()
    a = answer['content']
    words = str(a)
    if '{face:' in words:
        yuju = words.split('}')
        face = yuju[0].split(':')[1]
        words = "[CQ:face,id={}]{}".format(face, yuju[1])
    words = words.replace('菲菲', '小奏').replace('雪梅', '魔理沙').replace('小菲', '小奏')
    return words


async def ch(city: str):
    cityname = city
    url = 'https://api.ownthink.com/bot?appid=65b18965ecfe378cd868f114690a95e2&userid=7PmXS0bj&spoken=' + cityname
    answer = requests.get(url=url).json()
    a = str(answer['data']['info']['text'])
    a = a.replace("思思", "小奏").replace("小思", "小奏")
    return str(a)

wb_set_cmd = on_regex(r"^(?:全局|模糊|正则)*问(.+?)答", permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN | PRIVATE_FRIEND | GROUP_MEMBER, )


@wb_set_cmd.handle()
async def wb_set(matcher: Matcher, bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    ask = str(event.message).split("答")[0]+'答'
    da =str(event.message).split("答")[1]
    global word
    word = ask
    if da:
        matcher.set_arg("city", da)  # 如果用户发送了参数则直接赋值



    # if isinstance(event, GroupMessageEvent):
    #     index = event.group_id
    # else:
    #     index = event.user_id
    #
    # msg = event.raw_message
    #
    # kv = parse_cmd(r"([模糊全局正则]*)问(.+?)答(.+)", msg)
    #
    # if kv:
    #     flag, key, value = kv[0]
    #     type_ = 3 if '正则' in flag else 2 if '模糊' in flag else 1
    #
    #     res = wb.set(0 if '全局' in flag else index,
    #                  unescape(key),
    #                  value,
    #                  type_)
    #     if res:
    #         await bot.send(event, message='我记住了~')


@wb_set_cmd.got("city", prompt="你想让我回答什么")
async def wb_response( bot: Bot, event: MessageEvent, city: Message = Arg()):



    flag = False  # 判断是否合法TRUE表示违法
    isImg = False
    isText = False
    city = str(city).replace("\n", '').replace("\r", '')
    if 'CQ:image' in str(city):
        isImg = True
        access_t = await accessisUse()
        flag = await isHEfa(city, access_t)

    if not('[' in city and ']' in city):
        isText = True
        access_t = await accessisUse()
        w = await testisHEFA(city=city, access_t=access_t)
        if w == '不合规':
            flag = True

    if flag == True and isImg == True:
        await bot.send(event, message='图片违规,请重新发送')
    elif flag == True and  isText ==True:
        await bot.send(event, message='文本违规,请重新发送')
    elif flag ==False and isImg ==False and isText ==False:
        await bot.send(event, message='暂不支持这种格式哦，请联系我主人')
    else:
        message = word + city
        print(message)

        if isinstance(event, GroupMessageEvent):
            index = event.group_id
        else:
            index = event.user_id

        msg = str(message)

        kv = parse_cmd(r"([模糊全局正则]*)问(.+?)答(.+)", msg)

        if kv:
            flag, key, value = kv[0]
            type_ = 3 if '正则' in flag else 2 if '模糊' in flag else 1

            res = wb.set(0 if '全局' in flag else index,
                         unescape(key),
                         value,
                         type_)
            if res:
                await bot.send(event, message='我记住了~')


async def testisHEFA(city: str, access_t: str):
    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined"

    params = {"text": city}
    access_token = access_t
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    print(headers)
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        return response.json()['conclusion']
    return None
async def accessisUse():
    sql = 'select * from api where access_token = access_token'
    # logger.info(sql+user_qq)
    sql_select = sql

    op_mysql = OperationMysql()
    apiData = op_mysql.search_one(sql_select)
    time = datetime.now()
    print(apiData)
    if (apiData == None or (time - apiData['last_insertTime']).days >= 20):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client' \
               '_credentials&client_id=KyOrM3sKbfHKySfg5tq9mNtm&client_secret=GuTEvPOxZwvP41vukcSFTjPmaP5iP0Bo'
        response = requests.get(host)
        if response:
            print(response.json()['access_token'])
            sql_update = 'update api set data = ' +"\\'"+ response.json()[
                'access_token'] +"\\'"+ ',last_insertDate = now()' + ' where access_token = access_token'
            logger.info(sql_update)

            op_mysql = OperationMysql()
            op_mysql.updata_one(sql_update)

    sql = 'select * from api where access_token = access_token'
    # logger.info(sql+user_qq)
    sql_select = sql

    op_mysql = OperationMysql()
    apiData = op_mysql.search_one(sql_select)  # api所需要的值
    print(apiData['data'])
    return apiData['data']

async def isHEfa( city : str,atoken : str):
    flag = False
    citys = str(city).split('[CQ:image,')
    logger.info(citys)
    i = 0
    while i < len(citys):
        imgs = citys[i]
        # print(img)
        # print(word)
        # print(Message(city))
        imgs = imgs.replace('[', '').replace(']', '').replace("\\\'", '')
        img = imgs.split(",")
        # 获得url
        j = 0
        while j < len(img):
            if 'url' in img[j]:
                reImg = img[j].replace('url=', '')
                request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined"
                # 二进制方式打开图片文件
                params = {
                    "imgUrl": reImg}
                access_token = atoken
                request_url = request_url + "?access_token=" + access_token
                headers = {'content-type': 'application/x-www-form-urlencoded'}
                response = requests.post(request_url, data=params, headers=headers)
                if response:
                    print(response.json())
                    if response.json()['conclusion'] == '不合规':
                        flag = True

            j += 1
            print(j)

        i += 1
        print(i)
    return flag


wb_del_cmd = on_command('删除词条', permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN | PRIVATE_FRIEND | GROUP_MEMBER, )


@wb_del_cmd.handle()
async def wb_del_(bot: Bot, event: MessageEvent):
    if isinstance(event, GroupMessageEvent):
        index = event.group_id
    else:
        index = event.user_id

    msg = str(event.message)
    res = wb.delete(index, unescape(msg))
    if res:
        await bot.send(event, message='删除成功~')


wb_del_admin = on_command('删除全局词条', permission=SUPERUSER, )


@wb_del_admin.handle()
async def wb_del_admin_(bot: Bot, event: MessageEvent):
    msg = str(event.message).strip()
    if msg:
        res = wb.delete(0, unescape(msg))
        if res:
            await bot.send(event, message='删除成功~')


async def wb_del_all(bot: Bot, event: MessageEvent, state: T_State):
    msg = str(event.message).strip()
    if msg:
        state['is_sure'] = msg


wb_del_all_cmd = on_command('删除词库', permission=SUPERUSER | GROUP_OWNER | PRIVATE_FRIEND, handlers=[wb_del_all])
wb_del_all_admin = on_command('删除全局词库', permission=SUPERUSER, handlers=[wb_del_all])
wb_del_all_bank = on_command('删除全部词库', permission=SUPERUSER, handlers=[wb_del_all])


@wb_del_all_cmd.got('is_sure', prompt='此命令将会清空您的群聊/私人词库，确定请发送 yes')
async def wb_del_all_(bot: Bot, event: MessageEvent, state: T_State):
    if state['is_sure'] == 'yes':

        if isinstance(event, GroupMessageEvent):
            res = wb.clean(event.group_id)
            if res:
                await wb_del_all_cmd.finish(message='删除群聊词库成功~')

        else:
            res = wb.clean(event.user_id)
            if res:
                await wb_del_all_cmd.finish(message='删除个人词库成功~')

    else:
        await wb_del_all_cmd.finish('命令取消')


@wb_del_all_admin.got('is_sure', prompt='此命令将会清空您的全局词库，确定请发送 yes')
async def wb_del_all_admin_(bot: Bot, event: MessageEvent, state: T_State):
    if state['is_sure'] == 'yes':
        res = wb.clean(0)

        if res:
            await bot.send(event, message='删除全局词库成功~')

    else:
        await wb_del_all_admin.finish('命令取消')


@wb_del_all_bank.got('is_sure', prompt='此命令将会清空您的全部词库，确定请发送 yes')
async def wb_del_all_bank_(bot: Bot, event: MessageEvent, state: T_State):
    if state['is_sure'] == 'yes':
        res = wb._clean_all()

        if res:
            await bot.send(event, message='删除全部词库成功~')

    else:
        await wb_del_all_bank.finish('命令取消')
