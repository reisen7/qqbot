#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
import os
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init(apscheduler_autostart=True)
nonebot.init(apscheduler_config={
    "apscheduler.timezone": "Asia/Shanghai"
})


nonebot.load_plugins("src/plugins")

# nonebot.load_plugin("nonebot_plugin_heisi")
# nonebot.load_plugin("nonebot_plugin_remake")
# nonebot.load_plugin("nonebot_plugin_antiflash")
# nonebot.load_plugin("nonebot_plugin_randomtkk")
nonebot.load_plugin("nonebot_plugin_htmlrender")
nonebot.load_plugin("nonebot_plugin_boardgame")
nonebot.load_plugin("nonebot_plugin_cchess")
nonebot.load_plugin("nonebot_plugin_gamedraw")
nonebot.load_plugin("nonebot_plugin_horserace")
# main = ('go-cqhttp.exe')
# f = os.popen(main)
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins()


# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
# nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
