
import nonebot
from nonebot import get_driver, logger
from nonebot.adapters.onebot.v11.bot import Bot

driver = get_driver()
start_group = nonebot.get_driver().config.start_group
global flag
flag =False

@driver.on_startup
async def do_something():
    message='小奏正在启动哦~'
    logger.info(message)


@driver.on_bot_connect
async def do_something(bot: Bot):
    message = '小奏正在启动哦~'
    global flag
    flag = True
    str1 = 1062564756
    # await bot.send_group_msg(group_id=str1, message=message, auto_escape=True)

