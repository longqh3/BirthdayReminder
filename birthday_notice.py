# -*- coding: UTF-8 -*-

import time
import sxtwl
lunar = sxtwl.Lunar()
from One2TwoDigit import One2TwoDigit
from differ_days import date_part
import datetime

def birthdayNotice_job(bri_name, bri_mon, bri_day, futureDays):
    solarDayMsg = str(bri_mon) + '月' + str(bri_day) + '日'
    solarDay = (str(int(time.strftime("%Y"))) + One2TwoDigit(str(bri_mon)) + One2TwoDigit(str(bri_day)))
    d2 = date_part(solarDay)
    d1 = date_part(date=datetime.datetime.now().strftime('%Y%m%d'))
    differ_day = (d2 - d1).days
    # 提前futureDays = 3提醒准备礼物或是其他
    if differ_day == futureDays:
        msg = solarDayMsg + '是【' + bri_name + '】的生日🎂。再过' + str(differ_day) + '天就到了~，记得准备礼物哦'
        print(bri_name + '生日是:' + solarDayMsg)
        print(time.strftime("%Y-%m-%d：") + bri_name + '的生日礼物提醒发送完毕~')
        return msg
    # 提前一天告知生日要到了，提醒发送生日祝福
    if differ_day == 1:
        msg = "明天是【" + bri_name + '】的生日🎂，记得发生日祝福哦'
        print(bri_name + '生日是:' + solarDayMsg)
        print(time.strftime("%Y-%m-%d：") + bri_name + '的生日祝福提醒发送完毕~')
        return msg


# 备用函数，可用于查找农历生日
def lunar_birthdayNotice_job(bri_name,bri_mon,bri_day,futureDays):
    print("lunar_birthdayNotice_job is working...")
    dayYinli2Yangli = lunar.getDayByLunar(int(time.strftime("%Y")), bri_mon, bri_day, False)  #查询阴历2018年10月20日的信息，最后一个False表示是否是闰月，填True的时候只有当年有闰月的时候才生效
    yangliDay = (str(dayYinli2Yangli.y) + One2TwoDigit(str(dayYinli2Yangli.m)) + One2TwoDigit(str(dayYinli2Yangli.d)))
    yangliDayMsg ='农历:' + (str(bri_mon) + '月' + (str(bri_day)) + '日' )
    print(bri_name+'阳历生日是:'+yangliDay)
    d2 = date_part(yangliDay) 
    d1 = date_part(date=datetime.datetime.now().strftime('%Y%m%d'))
    differ_day = (d2 - d1).days
    
    if 0<differ_day<=futureDays:
        name = bri_name
        # xiaoding.send_text(msg= yangliDayMsg + '是【' + name + '】的生日🎂\n再过' + str(differ_day) + '天就到了~\n', is_at_all=True)     # Text消息@所有人
        print(time.strftime("%Y-%m-%d") + name + '的生日提前提醒发送完毕~\n')
    elif differ_day==0 :
        name = bri_name
        # xiaoding.send_text(msg='今天是【' + name + '】的生日🎂\n祝寿星生日快乐！\n', is_at_all=True)     # Text消息@所有人
        print(time.strftime("%Y-%m-%d") + name + '的当天生日提醒发送完毕~\n')
