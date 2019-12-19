# -*- coding: UTF-8 -*-
 
from birthday_notice import birthdayNotice_job
import schedule
import time
import requests
import datetime

def run_birthday():
    print(time.strftime("\n%Y-%m-%d: ") + "生日定时任务开始\n")
    # 创建保存生日推送信息的list
    bir_msg_list = []
    # 分析保存于csv数据文件中的阳历生日信息
    # 获取当前Python程序的绝对路径
    dirname, filename = os.path.split(os.path.abspath(__file__))
    with open(os.path.join(dirname, "data.csv"), "r", encoding='UTF-8') as f_birth:
        all_line_birth = f_birth.readlines()
        # 逐行读取生日信息
        for i in range(len(all_line_birth)):
            line_birth = all_line_birth[i].split(",")
            bir_name, bir_mon, bir_day = line_birth[0], line_birth[1], line_birth[2]
            # 判断生日是否位于3天后，是，则返回提示信息并存入list中；否，则返回None
            msg = birthdayNotice_job(bir_name,int(bir_mon),int(bir_day),futureDays=3)
            if msg:
                bir_msg_list.append(msg)
    # 判断此次是否有生日提示信息需要推送
    if len(bir_msg_list) > 0:
        # 直接调用Server酱服务进行微信推送
        # Server酱URL
        url = 'your own Server酱 URL'
        d = {'text':datetime.datetime.now().strftime('%Y年%m月%d日')+"生日提醒信息",
             'desp':"\n\n".join(bir_msg_list)}
        requests.post(url, data = d)

if __name__ == '__main__':
    schedule.every().day.at("10:00").do(run_birthday)

    while True:
        schedule.run_pending()
        time.sleep(1)
 
