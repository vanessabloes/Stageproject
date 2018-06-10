from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

template_vars = {"test": "vans ook hoor"}

html_out = template.render(template_vars)

html_out = template.render(template_vars)

HTML(string=html_out).write_pdf("outputfile.pdf")