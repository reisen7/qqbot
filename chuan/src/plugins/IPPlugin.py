import urllib, requests
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.params import CommandArg
from nonebot.rule import to_me

ipname = on_command("ip", rule=to_me())


@ipname.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值


@ipname.got("city", prompt="你想查什么ip，快说喵~")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    city_weather = await get_ipinfo(city_name)
    await ipname.finish(city_weather)


async def get_ipinfo(ipinfo: str):
    ipin=ipinfo
    url = 'http://opendata.baidu.com/api.php?query='+ipin+'&co=&resource_id=6006&oe=utf8'
    print(url)
    proxies = {"http": None, "https": None}
    data = requests.get(url=url).json()
    ip = data['data']
    for info in ip:
        if (info['location']):
            return info['location']
    return '查找失败，ip地址错的吧'
