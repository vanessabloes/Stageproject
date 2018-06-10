from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

template_vars = {"title" : "Sales Funnel Report - National",
                 "national_pivot_table": sales_report.to_html()}

html_out = template.render(template_vars)

HTML('/home/wall-e/Documents/Thomas/M17-3261.html').write_pdf("staal1.pdf")