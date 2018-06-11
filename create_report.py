from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

class ReportCreator(object):
	"""Takes text files, outputs a pdf report"""
	def __init__(self, textfile1, textfile2):
		self.textfile1 = textfile1
		self.textfile2 = textfile2

	def get_values(self):
		"""txt parsers"""
		with open(self.textfile1) as file:
			for x, line in enumerate(file):
				line = line.strip().split('\t')
				if x == 0:
					self.sample = line[1][0:8]
				elif x == 3:
					self.score = line[1]
					self.score = float(self.score)
				elif x == 4:
					self.status = line[1]
			return self.sample, self.score, self.status

	def get_values2(self):
		with open(self.textfile2) as file:
			for x, line in enumerate(file):
				line = line.strip().split('\t')
				self.regio = []
				self.peaks = []
				if x != 0:
					regio.append(line[0])
					peaks.append(int(line[3]))	

				
		

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
	parser = ArgumentParser(description='description', 
                            formatter_class= ArgumentDefaultsHelpFormatter)

	parser.add_argument('file1', type= str)
	parser.add_argument('file2', type= str)
	parser.add_argument('out', type= str)
	args = parser.parse_args()

	#Variabelen eventueel meegeven op commandline met argeparse
	template = 'template/template.html'
	style = 'template/style.css'
	
 
	#script

	report = ReportCreator(args.file1, args.file2)
	sample, score, status = report.get_values()
	print score
	print type(score)
	report.get_values2()
	report.create_pdf(template, style, args.out)