# -*- coding: utf-8 -*-

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
   

'''
How to send an email with Gmail as provider using Python?
https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python

How to Send Emails with Gmail using Python
https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

python学习通过smtp发送电子邮件
https://blog.csdn.net/pengzhi5966885/article/details/74701442

飄逸的python - 發送帶各種類型附件的郵件
https://blog.csdn.net/handsomekang/article/details/9811355

'''


''' ------------------------------------- Mail參數設定 ------------------------------------- '''
SMTP_Server =  "smtp.gmail.com" # 設定SMTP伺服器位址(Gmail: "smtp.gmail.com")

mail_user = "Your mail address"  # 寄件人信箱帳號
mail_password = "Your mail password"  # 寄件人信箱密碼
mail_port = 465  # 465 Port 必須要用SSL加密來進行
sent_from = mail_user  # 信件寄送來源位址
mail_to = "Send to mail address"  # 信件寄送目的位址

''' ---------------------------------------------------------------------------------------- '''


''' ------------------------------------- Mail內容設定 ------------------------------------- '''
# -- 建立一個訊息主體 --
msg = MIMEMultipart()

msg['Subject'] = "Python SMTP GMAIL 寄送信件測試"  # 信箱主題
msg['From'] = sent_from  # 來源位址
msg['To'] = mail_to  # 目的位址

# 信件內容(主要內容請打在這)
content = MIMEText("Python 寄送信件測試.")

# 信件附件清單
file_list = {'test.txt', 'test2.txt'}

''' ---------------------------------------------------------------------------------------- '''


# 取得當前所在位置
currentPath = os.getcwd()
# print('currentPath: ' + currentPath)


# 檢查確認是否有附件，如果有就串接到訊息主體去
def check_filelist():

    if len(file_list) != 0:

        for read_item in file_list:

            print("附件檔名： {}".format(read_item))

            # https://www.w3schools.com/python/python_file_handling.asp
            # http://www.runoob.com/python/python-func-open.html
            # open('檔名','模式') 'r' 代表指讀取檔案內容，'b'代表為二元數值(binary)) , 't' 代表為文字
            part = MIMEApplication(
                open(os.path.join(currentPath , read_item), 'rt').read())
            part.add_header('Content-Disposition',
                            'attachment', filename=read_item)

            msg.attach(part)  # 訊息主題串接附件


if __name__ == '__main__':

    try:

        # 訊息主體串接信件內容
        msg.attach(content)
        
        # 檢查是否有帶附件
        check_filelist()        

        # using a Secure Connection , for 465 port (Google)
        server = smtplib.SMTP_SSL(host = SMTP_Server,port = mail_port)

        server.ehlo()  # 詢問信箱SMTP伺服器連接

        server.login(mail_user, mail_password)  # 登入信箱服務伺服器

        server.sendmail(sent_from, mail_to, msg.as_string())  # 傳送信件

        server.close()  # 關閉信箱服務伺服器

        print('已傳送信件至 {} !!'.format(mail_to))

    except Exception as exception:

        print('傳送信件至 {} 失敗...!'.format(mail_to))

        print("{}".format(exception))
