from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

class ReportCreator(object):
    """takes txt files, outputs pdf"""
    def __init__(self, textfile1):
        self.textfile1 = textfile1

    def get_values(self):
        """txt parsing"""
        with open(self.textfile1) as file:
            for x, line in enumerate(file):
                line = line.strip().split('\t')
                if x == 0:
                    self.sample = line[1][0:8]
                elif x ==3:
                    self.score = line[1]

        return self.sample, self.score

    def create_pdf(self, html_template, stylesheet, output):
        """combines html, jinja vars and css into pdf"""
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(html_template)

        html_out = template.render(sample=self.sample, score=self.score)

        HTML(string=html_out).write_pdf(output, stylesheets=[stylesheet])

if __name__ == '__main__':
    """vars in bash for argparse"""
    parser = ArgumentParser(description='description', formatter_class= ArgumentDefaultsHelpFormatter)
    parser.add_argument('textfile1', type= str)
    parser.add_argument('output', type = str)

    args = parser.parse_args()

    template = 'template/template.html'
    style = 'template/style.css'

    """outputting pdf"""
    report = ReportCreator(args.textfile1)
    sample, score = report.get_values()
    report.create_pdf(template, style, args.output)
