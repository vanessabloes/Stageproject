import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_mail(pdf_filename):
	"""Send automatic mails trought smtp"""
	email = '*****'
	password = '*****'

	email_to = 'vanessa.bloes@student.howest.be'
	subject = 'mSINGS Resultaten'

	body= "Zie bijlage voor mSINGS resultaten"
	filename = path + pdf_filename

	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = email_to
	msg['Subject'] = subject

	msg.attach(MIMEText(body, 'plain'))

	attachment =open(filename, 'rb')

	part = MIMEBase('application','octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment; filename= "+filename)
	msg.attach(part)

	text = msg.as_string()
	text = msg.as_string()
	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	mail.login(email, password)
	mail.sendmail( email , email_to , text)
	mail.close()

sample_status(file_name)