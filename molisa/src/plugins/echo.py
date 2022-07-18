
import aiocqhttp
from nonebot.adapters.onebot.v11 import Message, MessageSegment, MessageEvent
from nonebot.rule import to_me
from nonebot.params import CommandArg
from nonebot.plugin import on_command

echo = on_command("echo", to_me())


@echo.handle()
async def echo_escape(event:MessageEvent ,message: Message = CommandArg()):
    img = 'https://img.m4a1.top/imgapi.cn/[%E8%BD%BB%E5%85%B0%E6%98%A0%E7%94%BB]%20Grand.008%20%E6%97%A5%E7%B3%BB%E6%B0%B4%E6%89%8B%E6%9C%8D%E5%AD%A6%E5%A6%B9/60.jpg'
    tu = f"[CQ:image,file={img}]"
    repy = [
        {
            "type": "image",
            "data": {
                "file": img
            }
        }
    ]
    await echo.send(message=Message(str(aiocqhttp.Message(repy))))