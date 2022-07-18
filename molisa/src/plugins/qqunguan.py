import random

import aiocqhttp
import requests
from nonebot import on_notice, on_keyword, on_command, logger
from nonebot.adapters.onebot.v11 import Bot, GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent, GroupUploadNoticeEvent, \
    GroupAdminNoticeEvent, Message, GroupMessageEvent, MessageSegment

from nonebot.permission import SUPERUSER
from nonebot.typing import T_State

GroupIncrease = on_notice()


# 检测群成员增加
@GroupIncrease.handle()
async def handle_first_receive(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    rely = [
        {
            "type": "text",
            "data": {
                "text": "欢迎"
            }
        },
        {
            "type": "at",
            "data": {
                "qq": f"{event.user_id}"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "进群"
            }
        },
        {
            "type": "image",
            "data": {
                "file": f"https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "进来就是一家人啦，进群不说话就踢了，有问题自己多问，我会定时踢不活跃成员"
            }
        },
        {
            "type": "face",
            "data": {
                "id": "13"
            }
        }
    ]
    await bot.send(event=event, message=Message(str(aiocqhttp.Message(rely))))


# 检测离开群成员
group_decrease = on_notice()


@group_decrease.handle()
async def handle_first_receive(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    rely = [
        {
            "type": "text",
            "data": {
                "text": "这位群菜鸟"
            }
        },
        {
            "type": "at",
            "data": {
                "qq": f"{event.user_id}"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "退群咯哦"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "good bye呀，永别了这位小鸡仔"
            }
        },
        {
            "type": "face",
            "data": {
                "id": "13"
            }
        }
    ]
    await bot.send(event=event, message=Message(str(aiocqhttp.Message(rely))))


# 检测文件上传
unload = on_notice()


@unload.handle()
async def handle_first_receive(bot: Bot, event: GroupUploadNoticeEvent, state: T_State):
    rely = [
        {
            "type": "text",
            "data": {
                "text": "这位小可爱"
            }
        },
        {
            "type": "at",
            "data": {
                "qq": f"{event.user_id}"
            }
        },
        {
            "type": "image",
            "data": {
                "file": f"https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "上传了新文件哦!"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "感谢你一直为群里做贡献"
            }
        },
        {
            "type": "face",
            "data": {
                "id": "13"
            }
        }
    ]
    await bot.send(event=event, message=Message(str(aiocqhttp.Message(rely))))


# 检测管理变动
guanli = on_notice()


@guanli.handle()
async def handle_first_receive(bot: Bot, event: GroupAdminNoticeEvent, state: T_State):
    user = event.user_id

    # print(user)
    at_ = MessageSegment.at(user)
    if event.sub_type == 'set':
        rely = at_ + '成为新管理捏，恭喜喵~'
    if event.sub_type == 'unset':
        rely = at_ + '你已被取消管理身份，好似喵~'
    # print(rely)
    await guanli.finish(message=Message(rely))


# recall=on_notice()
# @recall.handle()
# async def handle_first_receive(bot: Bot, event:GroupRecallNoticeEvent):
#     id=event.message_id
#     msg = await bot.get_msg(message_id=id)
#     biaoqing = f"[CQ:face,id=13]"  # 表情包使用
#     # mid =Message(msg["message"]["file"])
#     # await recall.send(f"CQ:image,file={mid}")
#     print(msg)
#     print(msg["message"])
#     print(type(msg))
#     await recall.send(Message("这是您撤回消息："+msg["message"]+"\n\n气不气"+biaoqing),at_sender=True)

# 被戳一戳事件
# poke = on_notice()
#
#
# @poke.handle()
# async def _(bot: Bot, event: PokeNotifyEvent):
#     if event.is_tome() and event.user_id != event.self_id:
#         msg=await hui()
#         await poke.send(Message(msg))
#
# async def hui():
#     url = 'https://res.abeim.cn/api-text_yiyan?export=json'
#     r = requests.post(url)
#     data = r.json()
#     content = data.get('content')
#     return content

# @poke.handle()
# async def _(bot: Bot, event: GroupRecallNoticeEvent):
#     mid = event.message_id
#     gid = event.group_id
#     uid = event.user_id
#     oid = event.operator_id
#     res = await bot.get_msg(message_id=mid)
#     msg = Message(res["message"])
#     user_dic = await bot.get_group_member_info(group_id=gid, user_id=uid)
#     print(user_dic)
#     user_card = user_dic['card'] if user_dic['card'] else user_dic['nickname']
#     if oid == uid:
#         await poke.send(f'{user_card}({uid})撤回了消息:\n ' + msg)
#     else:
#         # await poke.send(f'管理员撤回了{user_card}({uid})的消息:\n '+msg)
#         await poke.finish()



# 单人禁言
ban = on_keyword({'广告', '沙雕', '广告', 'md'}, priority=60)


@ban.handle()
async def b(bot: Bot, event: GroupMessageEvent, state: T_State):
    gid = event.group_id
    uid = event.user_id
    url = 'https://api.oioweb.cn/api/qq.php?qq=%s' % uid
    d = requests.get(url=url).json()
    img = d['imgurl']
    # ni=d['name']
    tu = f"[CQ:image,file={img}]"
    await ban.send(message=MessageSegment.at(uid) + Message(tu) + '请不要打广告或者使用不良语言哦！禁言十分钟警告处理!!')
    await bot.set_group_ban(group_id=gid, user_id=uid, duration=600, st_sender=True)


# 匿名禁言
nban = on_keyword({'广告', '沙雕', '广告', 'md', '妈的', }, priority=60)


@nban.handle()
async def n(bot: Bot, event: GroupMessageEvent, state: T_State):
    gid = event.group_id
    nm = event.anonymous.json()
    data = eval(nm)
    flag = data['flag']
    # print(data)
    # print(flag)
    # print(gid)
    await nban.send('请不要打广告或者使用不良语言哦！消息已经被撤回，下不为例，禁言十分钟警告处理!!')
    await bot.set_group_anonymous_ban(group_id=gid, anonymous=nm, anonymous_flag=flag, duration=600)


# 撤回消息
che = on_keyword({'广告', '沙雕', '广告', 'md', '妈的',  '操你妈', '操你',} ,priority=60)


@che.handle()
async def c(bot: Bot, event: GroupMessageEvent, state: T_State):
    mid = event.message_id
    print(mid)
    await bot.delete_msg(message_id=mid)


# # 踢人
# ti = on_keyword({'加vx'})
# @ti.handle()
# async def c(bot: Bot, event: GroupMessageEvent, state: T_State):
#     gid = event.group_id
#     uid = event.user_id
#     sid=event.self_id
#     await bot.set_group_kick(group_id=gid, user_id=uid,self_id=sid)


shu = on_keyword({'头衔'},priority=60)

@shu.handle()
async def s(bot: Bot, event: GroupMessageEvent, state: T_State):
    gid = event.group_id
    uid = event.user_id
    await bot.set_group_special_title(group_id=gid, user_id=uid, special_title='小奏的亲人', duration=6666)


# 全员禁言
vip = on_command('全员禁言', permission=SUPERUSER)


# vip=on_keyword({'全员禁言'})
@vip.handle()
async def s(bot: Bot, event: GroupMessageEvent, state: T_State):
    gid = event.group_id
    # oid = event.operator_idz
    await vip.send('现在已经全员禁言了哦，不要吵了！')
    await bot.set_group_whole_ban(group_id=gid, enable=True)


# 取消禁言
vip = on_command('取消禁言', permission=SUPERUSER)


@vip.handle()
async def s(bot: Bot, event: GroupMessageEvent, state: T_State):
    gid = event.group_id
    await vip.send('现在已经取消禁言了哦，大家在群里文明聊天哦')
    await bot.set_group_whole_ban(group_id=gid, enable=False)


dian=on_keyword({'垃圾','广告','傻逼','草','cao','操'},priority=60)
@dian.handle()
async def h(bot: Bot, event: GroupMessageEvent):
    mid=event.message_id
    uid=event.user_id
    gid=event.group_id
    msg='这位小可爱，请不要说不良词汇，您的消息已经被撤回，请注意语言哦'
    await bot.delete_msg(message_id=mid)
    await bot.send_msg(user_id=uid,message=msg,group_id=gid)

dian=on_keyword({'帅哥','群主最帅','群主最美','群主最棒','我爱张杰'},priority=60)
@dian.handle()
async def h(bot: Bot, event: GroupMessageEvent):
    mid=event.message_id
    await bot.set_essence_msg(message_id=mid)


dian=on_command('发送群公告',permission=SUPERUSER)
@dian.handle()
async def h(bot: Bot, event: GroupMessageEvent):
    gid=event.group_id
#     msg="""
#     温馨，和谐，礼貌，真诚，不欢迎广告!
# 你见，或者不见我，我就在那里，不悲不喜
# 你念，或者不念我，情就在那里，不来不去
# 你爱，或者不爱我，爱就在那里，不增不减
# 你跟，或者不跟我，我的手就在你手里，不舍不弃
# 来了，就是兄弟，姐妹。
#
#     """
    msg1="""
1、不得在群内骂人斗嘴等具有人身攻击性质行为，可私下单挑解决。如被暴打请拨打110或向管理员求助，但管理员不负责替人出头。

2、在上半年里、火可以试金，从而使咱群走上可持续发展的伟大道路，灌水有新思路。有来必言，我们紧密扎根在群里，出路没有。

3、但凡入群的小伙伴，都需先自报三围、身高，外加玉照一张，婚恋情况等，不遵守者留群察觉看三天；另外不得在群里潜水，要勇于冒泡、灌水，否则视管理员心情好坏给予溺毙处理。

4、山不在高，有石头就行；水不在深，有鱼就行；群里不在乎有多少人，有你们就行。来吧，我们是一个有爱的家族，因为你们的存在更精彩！

5、进群者都必须发照片一张以供大家鉴赏，如果对自己长相没有把握者，需先把照片发给管理员，待管理员估算群内成员承受力后才可公开发放！望周知！
    """
    await bot._send_group_notice(group_id=gid,content=msg1)


t=on_keyword({'获取群文件信息','群文件信息'})
@t.handle()
async def j(bot:Bot,event:GroupMessageEvent):
    gid=event.group_id
    d=await bot.get_group_file_system_info(group_id=gid)
    fc='目前文件数量：'+str(d.get('file_count'))
    lc='文件数量上限：'+str(d.get('limit_count'))
    us='使用空间：'+str(d.get('used_space')/1000000000)+'G'
    ts='总共空间：'+str(d.get('total_space')/1000000000)+'G'
    gi='群号：'+str(d.get('group_id'))
    await t.send(message=str(fc+'\n'+lc+'\n'+us+'\n'+ts+'\n'+gi))

t=on_keyword({'龙王'},priority=60)
@t.handle()
async def j(bot:Bot,event:GroupMessageEvent):
    gid=event.group_id
    d=await bot.get_group_honor_info(group_id=gid,type='all')
    # print(d)
    lw=d.get('current_talkative')
    l=lw.get('user_id')
    # print(lw)
    at_ = f"[CQ:at,qq={l}]"
    dc=lw.get('day_count')
    print(dc)
    if d :
        await t.send(Message('恭喜' + at_ + '为今日龙王' + '\n' + '持续天数为：' + str(dc)))
    else:
        await t.send(Message('没有龙王'))

