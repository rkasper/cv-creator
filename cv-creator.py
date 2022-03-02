import os

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

if __name__ == '__main__':
    with open('cv.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text, extensions=['smarty'])

    if not os.path.exists('generated'):
        os.mkdir('generated')

    with open('generated/cv.html', 'w') as f:
        f.write(html)

    font_config = FontConfiguration()
    html = HTML('generated/cv.html')
    css = CSS('cv.css')
    html.write_pdf('generated/cv.pdf', stylesheets=[css], font_config=font_config)
