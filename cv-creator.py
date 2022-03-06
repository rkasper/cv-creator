import markdown
from pdf2docx import parse
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

WEB_CSS_FILE = 'static/web.css'

PRINT_CSS_FILE = 'static/print.css'

MARKDOWN_FILE = 'cv.md'

OUTPUT_DIR = 'generated'
DOCX_FILE = OUTPUT_DIR + '/cv.docx'
HTML_FILE = OUTPUT_DIR + '/cv.html'
PDF_FILE = OUTPUT_DIR + '/cv.pdf'

if __name__ == '__main__':
    # Convert Markdown file to simple HTML
    with open(MARKDOWN_FILE, 'r') as f:
        text = f.read()
        simple_html = markdown.markdown(text, extensions=['smarty'])

    # Convert to PDF and output PDF file
    font_config = FontConfiguration()
    css = CSS(PRINT_CSS_FILE, font_config=font_config)
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

    # Convert PDF to Word file
    parse(pdf_file=PDF_FILE, docx_with_path=DOCX_FILE)
