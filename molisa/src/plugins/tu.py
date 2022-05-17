import random

from nonebot.adapters.onebot.v11 import Message
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.plugin import on_command
import requests
import re
from nonebot.rule import to_me
import os

os.environ['NO_PROXY'] = 'stackoverflow.com'


yulu = on_command('美女', rule=to_me())


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await qian()
    print(msg)
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass


async def qian():
    url = 'https://imgapi.cn/api.php?zd=mobile&fl=meizi&gs=json'
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).text
    x = resp.split(',')
    y = x[1].split('"')
    # test = resp['imgurl']
    test = y[3].replace("\\", "")
    tu = f"[CQ:image,file={test}]"
    return tu


yulu = on_command('cos1',aliases={"烧鸡"}, rule=to_me())


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await mei()
    print(msg)
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass


async def mei():
    url = 'https://imgapi.cn/cos.php?return=url'
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).url
    # x = resp.split(',')
    # y = x[1].split('"')
    # # test = resp['imgurl']
    # test = y[3].replace("\\", "")
    tu = f"[CQ:image,file={resp}]"
    return tu


yulu = on_command('cos2', rule=to_me())


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await heisi()
    print(msg)
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass


async def heisi():
    url = 'https://imgapi.cn/cos2.php?return=json'
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, verify=False, proxies=proxies).text
    x = resp.split(',')
    y = x[1].split('"')
    # test = resp['imgurl']
    test = y[3].replace("\\", "")
    tu = f"[CQ:image,file={test}]"
    return tu


yulu = on_command('肉丝', rule=to_me())


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await rousi()
    print(msg)
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass


async def rousi():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'}
    wz = 'https://www.siwashi.com/rosi'
    # 设置页数
    a = 20
    y = 1
    tmp = random.randint(2, 19)
    print(tmp)
    for itme in range(1, a + 1):
        url = wz
        # print('正在下载第%s页图片' % y)
        # print(url)
        y += 1
        # 开始解析网页
        proxies = {"http": None, "https": None}
        res = requests.get(url, headers=headers, verify=False, proxies=proxies)
        img = re.findall('src=".*?"', res.text)
        # 开始下载图片
        # print(img)
        x = 1
        i = 0
        if y == tmp:
            while (1 > 0):  # 对查找出来的大量结果进行循环，一个一个处理
                i=i+1
                if(i==20):
                    imgtu = '查找失败'
                    break
                x = random.randint(1, len(img) - 1)
                imgurl = re.findall("https.*webp", img[x])  # 把“img” 标签里图片的 地址给提取出来
                # imgtu=str(imgurl)
                # print(imgtu)
                print(x)
                imgtu = str(imgurl)
                imgtu = imgtu.replace("['", "")
                imgtu = imgtu.replace("']", "")
                if (imgtu != '[]' and int(len(imgtu)) > 71):
                    break

    test = imgtu
    test = test.replace(".webp", ".jpg")
    if (test == "查找失败"):
        return test;
    tu = f"[CQ:image,file={test}]"
    return tu


yulu = on_command('白丝',priority=0)


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await baisi()
    print(msg)
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass


async def baisi():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'}

    wz = 'https://www.siwashi.com/baisi'
    # 设置页数
    a = 20
    y = 1
    tmp = random.randint(2,19)
    print(tmp)
    for itme in range(1, a + 1):
        url = wz
        # print('正在下载第%s页图片' % y)
        # print(url)
        y += 1
        # 开始解析网页
        proxies = {"http": None, "https": None}
        res = requests.get(url, headers=headers, verify=False, proxies=proxies)
        img = re.findall('src=".*?"', res.text)
        # 开始下载图片
        # print(img)
        x = 1
        i = 0
        if y == tmp:
            while (1 > 0):  # 对查找出来的大量结果进行循环，一个一个处理
                i=i+1
                if(i==20):
                    imgtu = '查找失败'
                    break
                x = random.randint(1, len(img) - 1)
                imgurl = re.findall("https.*webp", img[x])  # 把“img” 标签里图片的 地址给提取出来
                # imgtu=str(imgurl)
                # print(imgtu)
                print(x)
                imgtu = str(imgurl)
                imgtu = imgtu.replace("['", "")
                imgtu = imgtu.replace("']", "")
                if (imgtu != '[]' and int(len(imgtu)) > 71):
                    break

    test = imgtu
    test = test.replace(".webp", ".jpg")
    if (test == "查找失败"):
        return test;
    tu = f"[CQ:image,file={test}]"
    return tu


yulu = on_command('其他丝袜',priority=0)


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await qitas()
    print(msg)
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass


async def qitas():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'}
    wz = 'https://www.siwashi.com/other'
    # 设置页数
    a = 20
    y = 1
    tmp = random.randint(2, 19)
    print("tmp: "+str(tmp))
    for itme in range(1, a + 1):
        url = wz
        # print('正在下载第%s页图片' % y)
        # print(url)
        y += 1
        # 开始解析网页
        proxies = {"http": None, "https": None}
        res = requests.get(url, headers=headers, verify=False, proxies=proxies)
        img = re.findall('src=".*?"', res.text)
        # 开始下载图片
        # print(img)
        i = 0
        if y == tmp:
            while (1 > 0):  # 对查找出来的大量结果进行循环，一个一个处理
                i = i+1
                if(i==20):
                    imgtu='查找失败'
                    break
                x = random.randint(1, len(img) - 1)
                print(img[i])
                imgurl = re.findall("https.*webp", img[x])  # 把“img” 标签里图片的 地址给提取出来
                # imgtu=str(imgurl)
                # print(imgtu)
                print("x: "+str(x))
                imgtu = str(imgurl)
                imgtu = imgtu.replace("['", "")
                imgtu = imgtu.replace("']", "")
                print("img"+ imgtu)
                if ((imgtu != '[]' )and int(len(imgtu)) > 71):
                    break

    test = imgtu
    test = test.replace(".webp", ".jpg")
    if(test =="查找失败"):
        return test;
    tu = f"[CQ:image,file={test}]"
    return tu