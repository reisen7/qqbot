
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

    repys = """[CQ:xml,data=<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="1" templateID="-1" action="web" brief="小奏已进群监听聊天" sourceMsgId="0" url="" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2" advertiser_id="0" aid="0"><picture cover="https://gchat.qpic.cn/gchatpic_new/328170849/993105896-2519025998-33A501D3C7EEDC30296DA0812A1A0972/0?term=3,subType=0" w="0" h="0" /><title>小奏已进群监听聊天</title><summary>请注意聊天言辞</summary></item><source name="" icon="" action="" appid="0" /></msg>,resid=1]"""
    print(repys)
    await echo.send(message=Message(repys))