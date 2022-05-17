from nonebot import on_command, on_keyword
import requests
from nonebot.internal.matcher import Matcher
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
chengyu = on_command("成语查询", to_me(),priority=0)


@chengyu.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("chenyu", args)


@chengyu.got("chenyu", prompt="你想查询什么成语呢？")
async def handle_city(chenyu: Message = Arg(), chenyu_name: str = ArgPlainText("chenyu")):
    chenyu = await xin(chenyu_name)
    await chengyu.finish(chenyu)


async def xin(city: str):
    cityname = city
    url = 'http://apis.juhe.cn/idioms/query?key=3da85cf3b46175276926ceea5238ee0c&wd=' + cityname
    proxies = {"http": None, "https": None}
    d = requests.get(url=url, verify=False, proxies=proxies).json()
    print(d)
    jie = d['result']['xxsy'][0]
    chu = d['result']['xxsy'][1]
    shi = d['result']['xxsy'][2]
    # yu=d['result']['xxsy'][3]
    # j='近义词：'+d['result']['jyc']
    # fyc='反义词：'+d['result']['fyc']
    return str(jie + '\n' + chu + '\n' + shi)
