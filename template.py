from jinja2 import Template
with open('template.html') as f:
    tmpl = Template(f.read())
print tmpl.render(
    sample = 'staal1'
)