import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email_attach(recipients_addrs, sender_addr, sender_pwd, content, csv_list, image_list=[]):
    if image_list is None:
        image_list = []
    global imageApart, xlsxApart
    toaddrs = [_ for _ in recipients_addrs if _ != '']
    xlsxApart_list = []

    content = content
    textApart = MIMEText(content)

    if image_list != []:
        for image in image_list:
            imageFile = image
            imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
            imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

    if csv_list != [''] and csv_list!=[]:
        for xlsx in csv_list:
            if xlsx == '':
                continue
            xlsxFile = xlsx
            xlsx_name = xlsx.split('/')[-1]
            xlsxApart = MIMEApplication(open(xlsxFile, 'rb').read())
            xlsxApart.add_header('Content-Disposition', 'attachment', filename=xlsx_name)
            xlsxApart_list.append(xlsxApart)

    m = MIMEMultipart()
    m.attach(textApart)
    for item in xlsxApart_list:
        m.attach(item)
    m['Subject'] = '日常通知'

    server = smtplib.SMTP('smtp.exmail.qq.com')
    server.login(sender_addr, sender_pwd)
    try :
        server.sendmail(sender_addr, toaddrs, m.as_string())
    except Exception as e:
        print(e)
    print('success')
    server.quit()