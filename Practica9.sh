#Daniel Adrian Lozano Garza
#!/bin/bash

#Al script le proporcionas 2 parametros uno es la ruta donde tienes el archivo con los correos
#el siguiente es el mensaje que quieras enviar

emails=$1
mensaje=$2

function py { python3 -c "$1" "$2" ; }

for email in $(cat $emails)
do
    py "
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
    
def sendmail(a, x):


    data = {}
    with open('pass.json') as f:
         data = json.load(f)
    msg = MIMEMultipart()

    message = str(x)

    msg['From'] = data['user']

    msg['To'] = str(a)
    msg['Subject'] = 'Que rolloo'

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.office365.com:587')
    server.starttls()

    print(data['user'])
    server.login(data['user'], data['pass'])

    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print('successfully sent email to %s:' % (msg['To']))

a = '$email'
b = '$mensaje'

sendmail(a, b)
    "

done
