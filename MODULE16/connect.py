import smtplib


def send_mail(user,passw,msg,to):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(user,passw)
    server.sendmail(user,to,msg)
    #print(user,passw,msg,to)
