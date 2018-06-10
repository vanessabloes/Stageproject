from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('reportdelta.html')

template_vars = {"test": "vans ook hoor"}

html_out = template.render(template_vars)

HTML('reportdelta.html').write_pdf("test.pdf", stylesheets= ["style.css"])

