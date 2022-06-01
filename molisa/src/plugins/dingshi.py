from nonebot import require
import nonebot
import time
from nonebot.adapters.onebot.v11 import Bot, Message
import requests
scheduler = require('nonebot_plugin_apscheduler').scheduler


# @scheduler.scheduled_job('cron', minute='*/20', id='sleep1')
# async def co():
#     # d = time.strftime("%m-%d %H:%M:%S", time.localtime())
#     url = 'http://api.ymong.top/api/cos.php'
#     da = requests.get(url).text
#     tu = f"[CQ:image,file={da}]"
#
#     bot = nonebot.get_bots()['328170849']
#     return await bot.call_api('send_group_msg', **{
#         'message': '{}'.format(tu),
#         'group_id': '695392621'
#     })

# @scheduler.scheduled_job('cron', minute='*/50', id='sleep')
# async def w():
#
#     url = 'https://api.muxiuge.cn/API/wbrs.php'
#     resp = requests.get(url).json()
#
#     da1=resp['data'][0]
#     te1='标题：'+da1.get('text')
#     wang1='网址'+da1.get('url')
#
#     da2 = resp['data'][1]
#     te2 = '标题：' + da2.get('text')
#     wang2 = '网址' + da2.get('url')
#
#     da3 = resp['data'][2]
#     te3 = '标题：' + da3.get('text')
#     wang3 = '网址' + da3.get('url')
#
#     da4 = resp['data'][3]
#     te4 = '标题：' + da4.get('text')
#     wang4 = '网址' + da4.get('url')
#
#     da5 = resp['data'][4]
#     te5 = '标题：' + da5.get('text')
#     wang5 = '网址' + da5.get('url')
#     t=te1+wang1+'\n'+te2+wang2+'\n'+te3+wang3+'\n'+te4+wang4+'\n'+te5+wang5
#     # print(te5)
#     rl = 'http://api.52guleng.cn/api/wzztp/api.php?s=325&ss=00A8FF&nr='+ t
#     png = requests.get(url=rl).text
#     tu = f"[CQ:image,file={png}]"
#
#     bot = nonebot.get_bots()['328170849']
#     return await bot.call_api('send_group_msg', **{
#         'message': '今日微博热搜：{}'.format(tu),
#         'group_id': '695392621'
#     })


@scheduler.scheduled_job('cron', hour='*/2', id='sleep2')
async def f():
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
        'pragma': 'no-cache',
        'sec-ch-ua': """Not A;Brand";v="99","Chromium";v="101","Google Chrome";v="101" """,
        "sec-ch-ua-mobile": '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'Cookie': "_uuid=66482FCD-3921-23A6-2979-92FD7B080F0E02608infoc; buvid3=10BDA524-D0DD-4920-8C70-8414CF158F0B148831infoc; rpdid=|(YYk)Yu~ul0J'uYk~Ykku)l; dy_spec_agreed=1; LIVE_BUVID=AUTO5016325481863792; fingerprint_s=d84b1b1dc981b2c61bd03a47faad2572; video_page_version=v_old_home; CURRENT_BLACKGAP=0; blackside_state=0; go_old_video=1; buvid4=D82B2EAB-FCF1-CD0F-CC7F-54BB66CC360896414-022012119-qNw/J93MbmFUJKuhPQiGbg%3D%3D; i-wanna-go-back=-1; buvid_fp_plain=undefined; fingerprint3=8f09ac291a5c46c5f4588605890e2d8b; nostalgia_conf=-1; hit-dyn-v2=1; sid=aka1y1j4; fingerprint=ad4ccdcd1be6d511f303c8843a11a691; buvid_fp=ad4ccdcd1be6d511f303c8843a11a691; DedeUserID=14211643; DedeUserID__ckMd5=896bac34e98270e4; SESSDATA=08d35968%2C1666667823%2C6b4f7*41; bili_jct=45f46e91d3e750799af9f9319dbbe17a; b_ut=5; bp_video_offset_14211643=664567196058386400; CURRENT_QUALITY=64; PVID=1; b_lsid=7BD9A139_181199B54D6; bsource=search_baidu; is-2022-channel=1; CURRENT_FNVAL=80; _dfcaptcha=5104a6cc6efb4ecb1413a76cec9fd351; innersign=0; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_10BDA524%22%3A%22181199B5B5A%22%2C%22333.337.fp.risk_10BDA524%22%3A%22181199C3471%22%2C%22333.976.fp.risk_10BDA524%22%3A%22181199C46AC%22%2C%22333.999.fp.risk_10BDA524%22%3A%2218119A659CE%22%2C%22333.788.fp.risk_10BDA524%22%3A%2218119A66C55%22%2C%22333.859.fp.risk_10BDA524%22%3A%2218119C45D1C%22%7D%7D"
    }
    url = "https://app.bilibili.com/x/topic/web/dynamic/rcmd?source=Web&;page_size=5"
    proxies = {"http": None, "https": None}
    resp = requests.get(url=url, headers=header)
    if resp.status_code == 200:
        j = resp.json()['data']['topic_items'][0]
        if 'name' in j:
            print(j['name'])
            print(j['jump_url'])
            t1 = '标题：' + j['name']
            wang5 = '网址' + j['jump_url']
            h1 = str('\n'+t1+'\n'+wang5+'\n')

        j = resp.json()['data']['topic_items'][1]
        if 'name' in j:
            print(j['name'])
            print(j['jump_url'])
            t1 = '标题：' + j['name']
            wang5 = '网址' + j['jump_url']
            h2 = str('\n' + t1 + '\n' + wang5 + '\n')

        j = resp.json()['data']['topic_items'][2]
        if 'name' in j:
            print(j['name'])
            print(j['jump_url'])
            t1 = '标题：' + j['name']
            wang5 = '网址' + j['jump_url']
            h3 = str('\n' + t1 + '\n' + wang5 + '\n')

        j = resp.json()['data']['topic_items'][3]
        if 'name' in j:
            print(j['name'])
            print(j['jump_url'])
            t1 = '标题：' + j['name']
            wang5 = '网址' + j['jump_url']
            h4 = str('\n' + t1 + '\n' + wang5 + '\n')

        j = resp.json()['data']['topic_items'][4]
        if 'name' in j:
            print(j['name'])
            print(j['jump_url'])
            t1 = '标题：' + j['name']
            wang5 = '网址' + j['jump_url']
            h5 = str('\n' + t1 + '\n' + wang5 + '\n')

        h ='哔哩哔哩热搜' +h1+h2+h3+h4+h5
        await nonebot.get_bot().send_group_msg(group_id='695392621', message="[CQ:at,qq={}]{}".format("all", h))
    # return z




