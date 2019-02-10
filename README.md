# Python寄信程式撰寫筆記

本專案程式執行前需要完成*Mail參數設置*與*Mail內容設置*內的設置，完成後即可測試執行程式，關於附件檔案類型部份，本專案原始測試是使用文字檔(txt)，在程式中會先透過*open()*開啟檔案並*read()*讀取內容，關於*Python open()* 開檔類型可參考[Python open() 函数](http://www.runoob.com/python/python-func-open.html)
<p><p/>

#### Mail參數設置
---
[1].  預設使用*Google Gmail SMTP SERVER*
  > SMTP_Server =  *"smtp.gmail.com"*
<br/>

[2].  寄件人信箱帳號(輸入自己的信箱)
  > mail_user = "Your mail address"
<br/>

[3].  寄件人信箱密碼(輸入自己的信箱密碼)
  > mail_password = "Your mail password"
<br/>

[4].  針對mail port使用SSL加密，必須要使用*465* Port
  > mail_port = 465
<br/>

[5].  信件寄送來源位址(寄送信件的來源位址，跟*mail_user* 一樣的參數，只需要取它的值即可)
  > sent_from = mail_user
<br/>

[6].  信件寄送目的位址(輸入要寄送的對方信箱)
  > mail_to = "Send to mail address"
<br/>

<p><p/>

#### Mail內容設置
---
[7].  信箱主題(標題)
  > msg['Subject'] = "Python SMTP GMAIL 寄送信件測試"
<br/>

[8].  信箱內容(主要信箱內容)
  > content = MIMEText("Python 寄送信件測試.")
<br/>

[9].  信箱附件清單(如果有附件檔案夾帶需求，請注意附件檔案路徑位置，本專案是建立在一個目錄底下，所需附件也是存在於專案相同目錄底下)
  > file_list = {'test.txt', 'test2.txt'}
<br/>

<p><p>

#### 可參考連結資源
---

1. [How to send an email with Gmail as provider using Python?]<br/>
  <https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python>

2. [How to Send Emails with Gmail using Python]<br/>
  <https://stackabuse.com/how-to-send-emails-with-gmail-using-python/>

3. [python学习通过smtp发送电子邮件]<br/>
  <https://blog.csdn.net/pengzhi5966885/article/details/74701442>

4. [飄逸的python - 發送帶各種類型附件的郵件]<br/>
  <https://blog.csdn.net/handsomekang/article/details/9811355>
