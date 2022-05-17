
import urllib, requests
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.params import CommandArg
from nonebot.rule import to_me

translate = on_command("翻译", rule=to_me())


@translate.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值


@translate.got("city", prompt="你想翻译什么")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    city_weather = await translate_tome(city_name)
    await translate.finish(city_weather)


async def translate_tome(city: str):
    cityname = city
    print(cityname)
    url = 'http://hm.suol.cc/API/fy.php?msg=' + cityname
    print(url)
    proxies = {"http": None, "https": None}
    data = requests.get(url=url, verify=False, proxies=proxies).text
    print(data)
    # to=resp['result']['future'][0]
    return data
