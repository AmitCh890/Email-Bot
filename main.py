import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('viber.ac.7@gmail.com','thinkpad890')
    email = EmailMessage()
    email['From'] = 'viber.ac.7@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {'amit' : 'akchaudhary8900@gmail.com',
              'puja' : 'chaudhary12pooja@gmail.com',
              'bhola': 'bctharu@gmail.com',
              'jyoti': 'drubajyoti01@gmail.com'}


def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of the email')
    subject = get_info()
    talk('Tell your content of the email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Your email is sent successfully')
    talk('Do you want to send more email')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
