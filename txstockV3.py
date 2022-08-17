import random
import requests,json,time
import sys
headers={'Host': 'wzq.tenpay.com',
         'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; MI CC 9e Build/NZH54D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 qqstock/9.10.0', 'accept': '*/*', 'x-requested-with': 'com.tencent.portfolio', 'sec-fetch-site': 'same-origin',
         'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty',
         'referer': 'https', 'accept-encoding': 'gzip, deflate',
         'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
         }
#获取每日任物
def tadyrw():
    api='https://wzq.tenpay.com/cgi-bin/activity_task_daily.fcgi'
    parmg={'action': 'home', 'type': 'routine', 'actid': '1111', '_': '1652179491542',
           'openid': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo',#cookie数据
           'fskey': 'v0ba82b0820627a35b80ec30ad916a0b', #cookie数据
           'channel': '1', '_appName': 'android', '_appver': '9.10.0', '_osVer': '7.1.2',
           '_devId': '4eb584fe699dc90244b49fca0d0d6eee06bca114'}#cookie数据
    repose=requests.get(url=api,params=parmg,headers=headers)
    #获取任务id
    it_t=repose.json()['task_pkg']
    id_tid = it_t[0]["tasks"]
    #提取id tid
    rwmas=len(id_tid)
    print(f'总共获取到每日{rwmas}个任务')
    tid={}
    for x in id_tid:
        tid[x["id"]]=x["tid"]
    return tid
# #成长任务
# def czrw():
#     api='https://wzq.tenpay.com/cgi-bin/activity_task_continue.fcgi?action=home&type=app_new_user&actid=1030&invite_code=&_=1652176850640&openid=oA0GbjvDTCVa3l5o0ejUD9AdhUEo&fskey=v0ba82b0820627a35b80ec30ad916a0b&channel=1&access_token=&_appName=android&_appver=9.10.0&_osVer=7.1.2&_devId=4eb584fe699dc90244b49fca0d0d6eee06bca114'
#     re_2=requests.get(url=api,headers=headers)
#     idd=re_2.json()['task_pkg'][0]['tasks']
#     tid_1={}
#     rwmas = len(idd)
#     print(f'总共获取到成长{rwmas}个任务')
#     for i in idd:
#         tid_1[i["id"]]=i["tid"]
#     return tid_1
def shujupiao():
    api='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?action=taskticket&channel=1&actid=1111&uin=oA0GbjvDTCVa3l5o0ejUD9AdhUEo&check=11&appid=&logintype=phone&openid=oA0GbjvDTCVa3l5o0ejUD9AdhUEo&fskey=v0ba82b0820627a35b80ec30ad916a0b&access_token=&g_openid=oA0GbjvDTCVa3l5o0ejUD9AdhUEo&uin=oA0GbjvDTCVa3l5o0ejUD9AdhUEo&_appName=android&_dev=MI+CC+9e&_devId=ffffffffed17b49f000000002bc635640000b49f&_mid=ffffffffed17b49f000000002bc635640000b49f&_md5mid=27CCB4B6D6BD8347ED127AC5081C89D2&_appver=9.10.0&_ifChId=17&_screenW=720&_screenH=1464&_osVer=7.1.2&_ui=7B1C44F9F1149A47&_uin=oA0GbjvDTCVa3l5o0ejUD9AdhUEo&_wxuin=oA0GbjvDTCVa3l5o0ejUD9AdhUEo&_net=WIFI&__random_suffix=4481&_buildtype=store&buildtime=2022-04-26+17%3A06%3A43&lang=zh_CN'
    re=requests.get(url=api,headers=headers)
    return re.json()['task_ticket']
def zuorenwu(id,tid):
    api='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi'
    # parmg={'action': 'taskdone', 'channel': '1', 'actid': '1033',
    #        'tid': tid, 'id': id,
    #        'task_ticket': shujupiao(),
    #        'check': '11', 'logintype': 'phone', 'openid': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo', 'fskey': 'v0ba82b0820627a35b80ec30ad916a0b', 'g_openid': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo', 'uin': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo', '_appName': 'android', '_dev': 'MI%20CC%209e', '_devId': 'ffffffffed17b49f000000002bc635640000b49f', '_mid': 'ffffffffed17b49f000000002bc635640000b49f', '_md5mid': '27CCB4B6D6BD8347ED127AC5081C89D2', '_appver': '9.10.0', '_ifChId': '17', '_screenW': '720', '_screenH': '1464', '_osVer': '7.1.2', '_ui': '7B1C44F9F1149A47', '_uin': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo', '_wxuin': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo', '_net': 'WIFI', '__random_suffix': '52227', '_buildtype': 'store', 'buildtime': '2022-04-26%2017%3A06%3A43', 'lang': 'zh_CN', 'hunheshiType': 'hippy'
    #        }
    parmg={'action': 'taskdone', 'channel': '1', 'actid': '1111',
           'id': id, 'tid': tid,
           'task_ticket': shujupiao(),
           'uin': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo',
           'check': '11','logintype': 'phone', 'openid': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo', 'fskey': 'v0ba82b0820627a35b80ec30ad916a0b', 'g_openid': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo', '_appName': 'android', '_dev': 'MI+CC+9e', '_devId': 'ffffffffed17b49f000000002bc635640000b49f', '_mid': 'ffffffffed17b49f000000002bc635640000b49f', '_md5mid': '27CCB4B6D6BD8347ED127AC5081C89D2', '_appver': '9.10.0', '_ifChId': '17', '_screenW': '720', '_screenH': '1464', '_osVer': '7.1.2', '_ui': '7B1C44F9F1149A47', '_uin': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo', '_wxuin': 'oA0GbjvDTCVa3l5o0ejUD9AdhUEo', '_net': 'WIFI', '__random_suffix': '6253', '_buildtype': 'store', 'buildtime': '2022-04-26+17%3A06%3A43', 'lang': 'zh_CN'}
    repo=requests.get(url=api,params=parmg,headers=headers)
    try:
        jb = repo.json()
        print(f"完成任务获得{jb}")
    except:
        print(repo.text)
if  __name__ == "__main__":
     #获取任务参数
     cz_id=tadyrw()
     for i in cz_id.items():
         zuorenwu(i[0],i[1])
         a=random.randint(60,200)
         time.sleep(a)
