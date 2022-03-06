import os

import markdown
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
    css = CSS('cv.css', font_config=font_config)
    parsed_html = HTML(string=simple_html)
    parsed_html.write_pdf(OUTPUT_DIR + '/cv.pdf', stylesheets=[css], font_config=font_config)

    # Enhance simple HTML
    full_html = '''<!DOCTYPE html>
<head>
  <title>Richard Kasperowski - Curriculum Vitae</title>
  <link rel="stylesheet" href="../cv.css">
</head>
<body>''' + simple_html + '''</body></html>'''
    with open(OUTPUT_DIR + '/cv.html', 'w') as f:
        f.write(full_html)
