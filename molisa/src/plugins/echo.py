
import aiocqhttp
from nonebot.adapters.onebot.v11 import Message, MessageSegment, MessageEvent
from nonebot.rule import to_me
from nonebot.params import CommandArg
from nonebot.plugin import on_command

echo = on_command("echo", to_me())


@echo.handle()
async def echo_escape(event:MessageEvent ,message: Message = CommandArg()):


    await echo.send(message='你好')