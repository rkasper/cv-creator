import markdown
from pdf2docx import parse
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


OUTPUT_DIR = 'generated'

if __name__ == '__main__':
    # Convert Markdown file to simple HTML
    with open('cv.md', 'r') as f:
        text = f.read()
        simple_html = markdown.markdown(text, extensions=['smarty'])

    # Convert to PDF and output PDF file
    font_config = FontConfiguration()
    css = CSS('static/print.css', font_config=font_config)
    parsed_html = HTML(string=simple_html)
    parsed_html.write_pdf(OUTPUT_DIR + '/cv.pdf', stylesheets=[css], font_config=font_config)

    # Enhance simple HTML and output HTML file
    full_html = '''<!DOCTYPE html>
<head>
  <title>Richard Kasperowski - Curriculum Vitae</title>
  <link rel="stylesheet" href="../static/web.css">
</head>
<body>''' + simple_html + '''</body></html>'''
    with open(OUTPUT_DIR + '/cv.html', 'w') as f:
        f.write(full_html)

    # Convert PDF to Word file
    parse(pdf_file=OUTPUT_DIR + '/cv.pdf', docx_with_path=OUTPUT_DIR + '/cv.docx')
