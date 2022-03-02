import os

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

OUTPUT_DIR = 'generated'

if __name__ == '__main__':
    with open('cv.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text, extensions=['smarty'])

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    with open(OUTPUT_DIR + '/cv.html', 'w') as f:
        f.write(html)

    font_config = FontConfiguration()
    print(font_config)

    css = CSS('cv.css', font_config=font_config)
    html = HTML(OUTPUT_DIR + '/cv.html')
    html.write_pdf(OUTPUT_DIR + '/cv.pdf', stylesheets=[css], font_config=font_config)
