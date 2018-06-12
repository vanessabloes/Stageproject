from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os
import matplotlib.pyplot as plt
import numpy as np


class ReportCreator(object):
	"""Takes text files, outputs a pdf report"""
	def __init__(self, textfile1):
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
				elif x == 4:
					self.status = line[1]
			return self.sample, self.score, self.status

	def create_images(self):
		"""Create graphs from values"""
		regio = []
		peaks_sample = []
		peaks_base = []

		with open(self.textfile2) as f:
    		for x, line in enumerate(f):
        		line = line.strip().split('\t')
        		if x != 0:
            	regio.append(line[0]) 
            	peaks_sample.append(float(line[3]))

		with open('/home/wall-e/msings/doc/MSI_BASELINE.txt') as b:
    		for x, line in enumerate(b):
        		line = line.strip().split('\t')
       			if x !=0:
            	peaks_base.append(float(line[2]))

		xpos = np.arange(len(regio))

		plt.bar(xpos-0.2,peaks_sample, width =0.4,label="Patient")
		plt.bar(xpos+0.2,peaks_base, width =0.4,label="Baseline")

		plt.xticks(xpos,regio, rotation=10,fontsize=4)
		plt.ylabel("Aantal pieken")
		plt.xlabel("Loci")
		plt.title('Pieken per loci: Patient vs Baseline', fontsize = 20)
		plt.legend()

		plt.savefig('report.png')
		plt.close()
	
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