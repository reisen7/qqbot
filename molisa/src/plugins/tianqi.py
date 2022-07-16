import urllib, requests
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.params import CommandArg
from nonebot.rule import to_me


weather = on_command("天气", rule=to_me())


@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    print(plain_text)
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="告诉我你想查哪个城市的天气")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    city_weather = await get_weather(city_name)
    await weather.finish(city_weather)


async def get_weather(city: str):
    cityname = city
    # print(cityname)
    url = 'http://hm.suol.cc/API/tq.php?msg='+cityname+'&n=1'
    # print(url)
    proxies = {"http": None, "https": None}
    data = requests.get(url=url, verify=False, proxies=proxies).text
    # to=resp['result']['future'][0]

    return str(data)
