# WeixinBirthdayNotice
#### 介绍
这是一个python写的按照阳历生日推送消息提醒的程序，
当前使用的是微信服务号(Server酱)进行消息推送。

#### 环境：python3.6+

#### 安装
1.下载源代码到本地

2.安装依赖包，命令：pip install -r requestments.txt

#### 快速使用-进入
1.打开run.py修改“schedule.every().day.at("10:00").do(run_birthday)”自定义每天推送消息时间；
  
2.运行‘python run.py’即可(若需要云服务器后台运行可应用nohup)

#### 详细/自定义使用步骤：
1.进入run.py修改第28行url为自己的Server酱url(申请地址见http://sc.ftqq.com/3.version)

2.打开data.csv添加寿星的阳历生日列表：姓名,月,日。以英文逗号隔开，多个寿星换行。注意“月日”格式为“1”型，不是“01”型。

3.打开run.py

a.修改第14行中的data.csv存放位置(目前暂时使用绝对路径，未来将打包以便于使用)

b. 第21行中"msg=birthdayNotice_job(bir_name,int(bir_mon),int(bir_day),futureDays=3)"
中的futureDays参数值为自定义提醒时间（默认为提前3天提醒准备生日礼物，提前1天提醒准备生日祝福。需要修改的话可自行于birthday_notice.py的函数中修改）

c. 可修改第34行“schedule.every().day.at("10:00").do(run)”，自定义每天消息时间；

4.运行‘python run.py’
 
#### 其他
Server酱发送的消息内容为Markdown格式，可进行消息内容的个性化定制发送

#### 待完善功能
1.添加农历生日提醒功能

2.在云服务器建立相应服务，以SaaS的形式提供多用户生日提醒

#### 参考代码与资料
DingtalkNotice：https://github.com/yuzg667/DingtalkNotice
