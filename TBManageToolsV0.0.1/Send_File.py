import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from Config import getConfig


def send_email_attach(addrs, content, csv_list, image_list=[]):
    if image_list is None:
        image_list = []
    global imageApart, xlsxApart
    fromaddr = getConfig('config', 'Main', 'fromaddr')
    password = getConfig('config', 'Main', 'password')
    toaddrs = [_ for _ in addrs if _ !='']
    xlsxApart_list=[]

    content = content
    textApart = MIMEText(content)

    if image_list != []:
        for image in image_list:
            imageFile = image
            imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
            imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

    if csv_list != ['']:
        for xlsx in csv_list:
            if xlsx=='':
                continue
            xlsxFile = xlsx
            xlsx_name=xlsx.split('/')[-1]
            xlsxApart = MIMEApplication(open(xlsxFile, 'rb').read())
            xlsxApart.add_header('Content-Disposition', 'attachment', filename=xlsx_name)
            xlsxApart_list.append(xlsxApart)

    # zipFile = '算法设计与分析基础第3版PDF.zip'
    # zipApart = MIMEApplication(open(zipFile, 'rb').read())
    # zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)


    m = MIMEMultipart()
    m.attach(textApart)
    for i in range(0, len(image_list)):
        m.attach(imageApart[i])
    for item in xlsxApart_list:
        m.attach(item)
    # m.attach(zipApart)
    m['Subject'] = '日常通知'

    try:
        server = smtplib.SMTP('smtp.exmail.qq.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
        return True
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误
