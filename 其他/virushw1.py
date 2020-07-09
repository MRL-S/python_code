import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = input("请输入发件人qq邮箱：")
password = input("请输入发件人qq邮箱授权码：")
receiver = []
while True:
    a = input("请输入收件人邮箱：")
    receiver.append(a)
    b = input("是否继续输入，输入n退出，任意键继续：")
    if b == 'n':
        break

smtp_server = 'smtp.qq.com'

message = MIMEMultipart()
message['From'] = Header('MRLiu','utf-8')
message['To'] = Header(','.join(receiver),'utf-8')
message['Subject'] = Header("这是一个测试",'utf-8')
message.attach(MIMEText('这是一个测试','plain','utf-8'))
while True:
    filename = input("请输入文件路径：")
    att = MIMEText(open(filename,'rb').read(),'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    message.attach(att)
    c = input("是否继续发送附件，输入n结束，任意键继续：")
    if c == 'n':
        break
try:
    server = smtplib.SMTP_SSL()
    server.connect('smtp.qq.com',465)
    server.login(sender,password)
    server.sendmail(sender,receiver,message.as_string())
    server.quit()
    print("成功")
except smtplib.SMTPException:
    print("Error:出错")