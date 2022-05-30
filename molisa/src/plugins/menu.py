from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Bot, Message, FriendRecallNoticeEvent
from nonebot.plugin import on_command

menu = on_command('菜单', aliases={"help", "帮助", ".\help" ,"/help"}, priority=0)


@menu.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["city"] = args
        msg = """(！！！以下命令需要艾特我才能执行)所有命令:人生重开，随机唐可可，今日人品，历史今天，今日哔哩哔哩排行，成语查询，每日一句，翻译，ip，二次元，美图，原神，美女，黑丝，cos1，cos2, 搜图"""
        id = str(event.get_user_id())
        # yuyin=f"[CQ:record,file=http://baidu.com/1.mp3]"
        # biaoqing=f"[CQ:face,id=123]"#表情包使
        at_ = f"[CQ:at,qq={id}]"  # 艾特好友使用
        await menu.send(msg)  # 发送消息使用

