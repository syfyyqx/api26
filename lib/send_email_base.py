#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 8:47
# Author    : zhangqi
# @File     : send_email_base.py
# @Software : PyCharm
#用于建立smtp连接
import  smtplib
#邮件需要专门的MIME格式
from email.mime.text import MIMEText
#plain指普通文本格式邮件内容
msg = MIMEText('恭喜你！已被我店录取----按摩师','plain','utf-8')
#发件人
msg['From']='3194551377@qq.com'
#收件人
msg['To']='2591882334@qq.com'
#邮件标题
msg['Subject']='入职通知-2024/4/27 9:55来J8-505 4-2位置报道'

smtp = smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('3194551377@qq.com','wyzzqdsyqeopdeea')
smtp.sendmail('3194551377@qq.com','2591882334@qq.com',msg.as_string())
smtp.quit()

























