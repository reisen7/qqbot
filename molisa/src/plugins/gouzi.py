import json

import nonebot
from nonebot import get_driver, logger
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.message import run_postprocessor

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
    message = '已经连上了~'
    global flag
    flag = True
    str1 = start_group

