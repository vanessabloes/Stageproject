from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('/home/wall-e/Stageproject/template.html')

template_vars = {"title" : "Sales Funnel Report - National",
                 "national_pivot_table": sales_report.to_html()}

html_out = template.render(template_vars)