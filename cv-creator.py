import os

import markdown
from pdf2docx import parse
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

MARKDOWN_FILE = 'cv.md'

WEB_CSS_FILE = 'static/web.css'
PDF_CSS_FILE = 'static/pdf.css'
WORD_CSS_FILE = 'static/word.css'

OUTPUT_DIR = 'generated'
HTML_FILE = OUTPUT_DIR + '/cv.html'
PDF_FILE = OUTPUT_DIR + '/cv.pdf'
TMP_PDF_FILE = OUTPUT_DIR + '/tmp-cv.pdf'
DOCX_FILE = OUTPUT_DIR + '/cv.docx'

if __name__ == '__main__':
    # Convert Markdown file to simple HTML
    with open(MARKDOWN_FILE, 'r') as f:
        text = f.read()
        simple_html = markdown.markdown(text, extensions=['smarty'])

    # Convert simple HTML to PDF and output PDF file
    font_config = FontConfiguration()
    css = CSS(PDF_CSS_FILE, font_config=font_config)
    parsed_html = HTML(string=simple_html)
    parsed_html.write_pdf(PDF_FILE, stylesheets=[css], font_config=font_config)

    # Enhance simple HTML and output HTML file
    full_html = '''<!DOCTYPE html>
<head>
  <title>Richard Kasperowski - Curriculum Vitae</title>
  <link rel="stylesheet" href="../''' + WEB_CSS_FILE + '''">
</head>
<body>''' + simple_html + '''</body></html>'''
    with open(HTML_FILE, 'w') as f:
        f.write(full_html)

    # Generate a one-page version of the PDF and output Word file
    font_config = FontConfiguration()
    css = CSS(WORD_CSS_FILE, font_config=font_config)
    parsed_html = HTML(string=simple_html)
    parsed_html.write_pdf(TMP_PDF_FILE, stylesheets=[css], font_config=font_config)
    parse(pdf_file=TMP_PDF_FILE, docx_file=DOCX_FILE)
    os.remove(TMP_PDF_FILE)
