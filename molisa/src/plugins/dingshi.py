from nonebot import require
import nonebot
import time
import requests
scheduler = require('nonebot_plugin_apscheduler').scheduler


@scheduler.scheduled_job('cron', minute='*/20', id='sleep1')
async def co():
    # d = time.strftime("%m-%d %H:%M:%S", time.localtime())
    url = 'http://api.ymong.top/api/cos.php'
    da = requests.get(url).text
    tu = f"[CQ:image,file={da}]"

    bot = nonebot.get_bots()['328170849']
    return await bot.call_api('send_group_msg', **{
        'message': '{}'.format(tu),
        'group_id': '695392621'
    })

@scheduler.scheduled_job('cron', minute='*/50', id='sleep')
async def w():

    url = 'https://api.muxiuge.cn/API/wbrs.php'
    resp = requests.get(url).json()

    da1=resp['data'][0]
    te1='标题：'+da1.get('text')
    wang1='网址'+da1.get('url')

    da2 = resp['data'][1]
    te2 = '标题：' + da2.get('text')
    wang2 = '网址' + da2.get('url')

    da3 = resp['data'][2]
    te3 = '标题：' + da3.get('text')
    wang3 = '网址' + da3.get('url')

    da4 = resp['data'][3]
    te4 = '标题：' + da4.get('text')
    wang4 = '网址' + da4.get('url')

    da5 = resp['data'][4]
    te5 = '标题：' + da5.get('text')
    wang5 = '网址' + da5.get('url')
    t=te1+wang1+'\n'+te2+wang2+'\n'+te3+wang3+'\n'+te4+wang4+'\n'+te5+wang5
    # print(te5)
    rl = 'http://api.52guleng.cn/api/wzztp/api.php?s=325&ss=00A8FF&nr='+ t
    png = requests.get(url=rl).text
    tu = f"[CQ:image,file={png}]"

    bot = nonebot.get_bots()['328170849']
    return await bot.call_api('send_group_msg', **{
        'message': '今日微博热搜：{}'.format(tu),
        'group_id': '695392621'
    })


@scheduler.scheduled_job('cron',minute='*/30', id='sleep2')
async def f():
    url = 'https://api.muxiuge.cn/API/bilirand.php'
    resp = requests.get(url).json()
    t='网址：'+resp['data']['url']
    zuo='作者：'+resp['data']['author']
    biao='标题：'+resp['data']['title']
    z=str(zuo+'\n'+biao+'\n'+t)
    # return z
    bot = nonebot.get_bots()['328170849']
    return await bot.call_api('send_group_msg', **{
        'message': '哔哩热搜\n{}'.format(z),
        'group_id': '695392621'
    })