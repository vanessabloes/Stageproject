file_name = '/home/wall-e/Desktop/data_mSINGS/M17-3261_S1/M17-3261_S1.MSI_Analysis.txt'

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
		
		print sample
		make_html(sample)

def make_html(sample):
	
	htmlname = sample + '.html'
	f = open(htmlname,'w')
		
	message = """<html>
	<head></head>
	<body><p>yoo!</p></body>
	</html>"""

	f.write(message)
	f.close()

sample_status(file_name)
