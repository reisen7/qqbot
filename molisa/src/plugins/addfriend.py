from nonebot import on_notice
from nonebot.adapters.onebot.v11 import FriendAddNoticeEvent, Bot
from nonebot.typing import T_State

addFriend = on_notice()


@addFriend.handle()
async def add_friend(bot: Bot, event: FriendAddNoticeEvent, state: T_State):
    event.user_id
    bot.get_forward_msg()
    
    await bot.set_friend_add_request(approve=True)
