from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

class ReportCreator(object):
	"""Takes text files, outputs a pdf report"""
	def __init__(self, textfile1):
		self.textfile1 = textfile1

	def get_values(self):
		"""txt parsers"""
		with open(self.textfile1) as file:
			for x, line in enumerate(file):
				line = line.strip().split('\t')
				if x == 0:
					self.sample = line[1][0:8]
				elif x == 3:
					self.score = line[1]
				elif x == 4:
					self.status = line[1]
			return self.sample, self.score, self.status

	def create_images(self):
		"""Create graphs from values"""
		pass
	
	def create_pdf(self, html_template, stylesheet, output):
		"""Combines html, jinja variables and css into pdf"""
		env = Environment(loader=FileSystemLoader('.'))
		template = env.get_template(html_template)
		
		html_out = template.render(sample=self.sample, score=self.score)
		
		HTML(string= html_out).write_pdf(output, stylesheets= [stylesheet])
		

if __name__ == '__main__':
	#Variabelen eventueel meegeven op commandline met argeparse
	file_name = 'example_input/M18-1605_S10.MSI_Analysis.txt'
	template = 'template/template.html'
	style = 'template/style.css'
	output = 'testpdf.pdf'

	#script
	report = ReportCreator(file_name)
	report.get_values()
	report.create_pdf(template, style, output)