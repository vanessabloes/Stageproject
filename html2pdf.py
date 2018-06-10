from weasyprint import HTML, CSS

HTML('reportdelta.html').write_pdf("test.pdf", stylesheets=["style.css"])