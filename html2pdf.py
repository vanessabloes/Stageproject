from weasyprint import HTML, CSS

HTML('reportdelta.html').write_pdf("testrapport.pdf", stylesheets=["style.css"])