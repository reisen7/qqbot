# import logging
#
# from nonebot.internal.matcher import Matcher
# from nonebot.params import Arg, CommandArg, ArgPlainText
# from nonebot import on_keyword,on_command
# from nonebot.internal.params import ArgPlainText
# from nonebot.permission import *
# from nonebot.rule import to_me
# import requests
# from nonebot .adapters.onebot.v11 import Bot,Event,Message
# import json
#
# from nonebot.typing import T_State
#
# liaotian=on_command('', rule=to_me(), priority=90)
#
#
# @liaotian.handle()
# async def handle_first_receive(matcher: Matcher,event: Event):
#       # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
#
#     message=str(event.get_message()).strip()
#     print(message)
#
#
#
# # @liaotian.got("city", prompt="你想跟我聊什么呢😊")
# # async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
# #     if city_name == '关闭聊天':
# #         await liaotian.finish('下次继续聊哦')
# #     city1=await chat(city)
# #     # await liaotian.send(message=city)
# #     await liaotian.send(message=city1)
# #     await liaotian.reject()
#
# # async def chat(city: str):
# #     cityname = city
# #     url_api = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + cityname
# #     r = requests.get(url_api).json()
# #     print(r)
# #     data = r['content']
# #     return str(data)
#
#
# async def chat(city:str):
#     cityname = city
#     url='http://api.qingyunke.com/api.php?key=free&appid=0&msg='+cityname
#     proxies = {"http": None, "https": None}
#     answer = requests.get(url, verify=False, proxies=proxies).json()
#     a = answer['content']
#     return str(a)
#
#
# async def ch(city:str):
#     cityname = city
#     url='https://api.ownthink.com/bot?appid=65b18965ecfe378cd868f114690a95e2&userid=7PmXS0bj&spoken=%E7%8C%AA%E5%90%97'+cityname
#     answer = requests.get(url=url).json()
#     a = answer['data']['info']['text']
#     return str(a)
#
# # liaotian=on_keyword({'ai'})
# # @liaotian.handle()
# # async def handle_first_receive(bot: Bot, event: Event, state: dict):
# #     args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
# #     if args:
# #         state["city"] = args  # 如果用户发送了参数则直接赋值
# #
# # @liaotian.got("city", prompt="你想问我什么？我是万能的哦！")
# # async def handle_city(bot: Bot, event: Event, state:dict):
# #     city = state["city"]
# #     city_weather = await ch(city)
# #     await liaotian.finish(city_weather)
# #
#
# # async def ch(city:str):
# #     cityname = city
# #     url_api = "http://api.brhsm.cn/lt.php?msg=" + cityname
# #     r = requests.get(url_api).json()
# #     data=r['text']
# #     return data
#
# # url='http://i.itpk.cn/api.php?question=%s&api_key=dea0ce8aeacfa5bb27a7be5b81655514&api_secret=xrvp7byekab9'%s