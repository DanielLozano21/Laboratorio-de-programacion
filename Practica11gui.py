import tkinter
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main():
	
	send = email()
	
	window = tkinter.Tk()
	window.geometry('500x400')

	button = tkinter.Button(window, text = 'Mandar correo', command = send.crearemail)
	button.pack()

	window.mainloop()


class email:

    def __init__(self):
        self.user = 'testdelaboratorio@gmail.com'
        self.pasw = 'fcfm1234'
        self.email = 'dany_z00@hotmail.com'
        self.subj = 'Prueba para la practica'
        self.body = 'Que onda'


    def enviaremail(self,x):
        conex = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=conex) as ser:
            ser.login(self.user, self.pasw)
            ser.sendmail(self.user, self.email, x)


    def crearemail(self):
        mail = MIMEMultipart("alternative")
        mail["Subject"] = self.subj
        mail["From"] = self.user
        mail["To"] = self.email
        html = """\
        <html>
          <body> 
		    <p>
		      """+self.body+"""
		    </p>
		  </body>
		</html>
		"""
        mailhtml = MIMEText(html, "html")
        mail.attach(mailhtml)
        creado = mail.as_string()
        self.enviaremail(creado)
        print('Correo enviado satisfactoriamente')
        exit()

main()

