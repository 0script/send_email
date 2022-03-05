#import nedeed libraries
import argparse
import json
import smtplib

#MIME (Multipurpose Internet Mail Extensions) type is a 
#standard way of describing a data type
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main(sender_mail,receiver_mail,subject,server,port,password,attachementt):
    'This function will send the mail'

    print(f'Preparing to send mail to {receiver_mail} from  {sender_mail}...')

    #Setup MIME
    message=MIMEMultipart()
    message['From']=sender_mail
    message['To']=receiver_mail
    message['Subject']=attachementt

    #Body and Attachements for the mail
    message.attach(MIMEText(subject,'plain'))

    #Create SMTP session and send the mail
    session=smtplib.SMTP(server,port)
    session = smtplib.SMTP(server, port)
    session.starttls()  #enable security
    session.login(sender_mail,password)
    msg_str=message.as_string()
    session.sendmail(sender_mail,receiver_mail,msg_str)
    session.quit()
    print(f'Mail successfully Send to {receiver_mail}.')

    return

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('email',
            type=str,
            help='Receiver Mail Address')
    parser.add_argument('-c',
            '--config',
            dest='config',
            type=argparse.FileType('r'),
            help='Configuration File',
            default=None)
    parser.add_argument('-s',
            '--subject',
            dest='subject',
            type=argparse.FileType('r'),
            help='The subject',
            default=None)
    parser.add_argument('-a',
            '--attach',
            dest='attach',
            type=str,
            help='The Attachement (title/header) of the mail',
            default='A test mail sent by Python. It has an attachment.')
    
    args=parser.parse_args()
    if not args.config:
        print('Error : A configuration file in json format is nedeed')
        parser.print_help()
        exit(1)
    if not args.subject:
        print('Error : A subject file in plain text format is nedeed')
        parser.print_help()
        exit(1)
    
    config=json.load(args.config)
    thesubject=''.join(args.subject.readlines())
    
    main(sender_mail=config['email'],
            receiver_mail=args.email,
            subject=thesubject,
            server=config['server'],
            port=config['port'],
            password=config['password'],
            attachementt=args.attach)
