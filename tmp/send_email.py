import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#1.组装邮件正文
msg=MIMEMultipart()#混合格式
body=MIMEText('python发送的邮件','plain','utf-8')
msg.attach(body)#将正文添加到msg对象中

#2.组装邮件头
# body['From']='test_results@sina.com'
# body['To']='superhin@126.com'
# body["Subject"]="from python"
msg['From']='test_results@sina.com'
msg['To']='superhin@126.com'
msg["Subject"]="from python"

#4.附件
with open("../report/report.html","rb")as f:
    att_file=f.read()

att=MIMEText(att_file,'base64','utf-8')
att["Content-Type"]='application/octet-stream'
att["Content-Disposition"]="attachment;file+++++++：=me='report.html'"
msg.attach(att)

smtp = smtplib.SMTP("smtp.163.com") # 建立连接
smtp.login("ivan-me@163.com", "hanzhichao123") # 登录邮箱
smtp.sendmail("ivan-me@163.com",
              'superhin@126.com',
              msg.as_string())# 讲MIME格式邮件转成字符串发送