import smtplib
from getpass import getpass
sender_mail = 'thumar2004@gmail.com'
receivers_mail = ['rajsteam0604@gmail.com','thumarbhautik2004@gmail.com']
password=getpass("Enter Your Password")
message=f'''
        From: {sender_mail}
        To: {receivers_mail}
        Subject: Sending SMTP e-mail this is a test email message.
        '''
try:
    smptobj = smtplib.SMTP('smtp.gmail.com',587)
    smptobj.ehlo()
    smptobj.starttls()
    smptobj.login(sender_mail,password)
    smptobj.sendmail(sender_mail,receivers_mail,message)
    print("Successfully Send Email...")
except Exception as e:
    print("Error:",str(e))
