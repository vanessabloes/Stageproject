from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import matplotlib.pyplot as plt
import numpy as np

class ReportCreator(object):
	"""Takes text files, outputs a pdf report"""
	def __init__(self, textfile1, textfile2, peaksfile):
		self.textfile1 = textfile1
		self.textfile2 = textfile2
		self.peaksfile = peaksfile

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

		with open(self.textfile2) as file:
			for x, line in enumerate(file):
				line = line.strip().split('\t')
				self.regio = []
				self.peaks = []
				self.peaks_base = []
				if x != 0:
					self.regio.append(line[0])
					self.peaks.append(float(line[3]))

		with open(self.peaksfile) as file:
			for x, line in enumerate(file):
				line = line.strip().split('\t')
				if x !=0:
					self.peaks_base.append(float(line[2]))

		return [self.regio,  self.peaks, self.peaks_base], [self.sample, self.score, self.status]

	def create_images(self):
		"""Create graphs from values"""
		xpos = np.arange(len(self.regio))

		plt.bar(xpos-0.2,self.peaks, width =0.4,label="Patient")
		plt.bar(xpos+0.2,self.peaks_base, width =0.4,label="Baseline")

		plt.xticks(xpos,self.regio, rotation=10,fontsize=4)
		plt.ylabel("Aantal pieken")
		plt.xlabel("Loci")
		plt.title('Pieken per loci: Patient vs Baseline', fontsize = 20)
		plt.legend()
		fig1 = plt.gcf()
		plt.draw()
		fig1.savefig('tessstttyyy.png', dpi=100)
	
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
	style = 'template/img/style.css'
	
 
	#script
	peaksfile = 'example_input/MSI_BASELINE.txt'
	report = ReportCreator(args.file1, args.file2, peaksfile)
	list2, list1 = report.get_values()
	print list2
	print list1
	report.create_images()
	#report.create_pdf(template, style, args.out)