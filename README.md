# Python寄信程式撰寫筆記

#### Mail參數設置
---
預設使用*Google Gmail SMTP SERVER*
<br/>

> SMTP_Server =  *"smtp.gmail.com"*
<br/>

寄件人信箱帳號(輸入自己的信箱)
> mail_user = "Your mail address"
<br/>

寄件人信箱密碼(輸入自己的信箱密碼)
> mail_password = "Your mail password"
<br/>

針對mail port使用SSL加密，必須要使用*465* Port
> mail_port = 465
<br/>

信件寄送來源位址(寄送信件的來源位址，跟*mail_user* 一樣的參數，只需要取它的值即可)
> sent_from = mail_user
<br/>

信件寄送目的位址(輸入要寄送的對方信箱)
> mail_to = "Send to mail address"
<br/>

<p><p/>

#### Mail內容設置
---

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
