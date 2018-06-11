file_name = '/home/wall-e/Desktop/data_mSINGS/M17-3261_S1/M17-3261_S1.MSI_Analysis.txt'
path = '/home/wall-e/Desktop/data_mSINGS/'

from reportlab.pdfgen import canvas
from reportlab.platypus import Image

def sample_status(file_name):
    with open(file_name) as file:
		for x, line in enumerate(file):
			
			line = line.strip().split('\t')
			if x == 0:
				sample = line[1][0:8]
			elif x == 3:
				score = line[1]
			elif x == 4:
				status = line[1]
		
		pdf_filename = sample + '.pdf'
		generate_report(sample, pdf_filename)
		send_mail(pdf_filename)

def generate_report(sample, pdf_filename):
	c = canvas.Canvas(pdf_filename)

	#header text
	c.setFont('Helvetica', 48, leading=None)
	c.drawCentredString(300, 720, sample)
	c.save()


def send_mail(pdf_filename):

	import smtplib
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	from email.mime.base import MIMEBase
	from email import encoders

	email = 'trouwvanessajannes@gmail.com'
	password = 'testwachtwoord'

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