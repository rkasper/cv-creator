import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


if __name__ == '__main__':
    with open('cv.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text, extensions=['smarty'])

    with open('cv.html', 'w') as f:
        f.write(html)

    font_config = FontConfiguration()
    html = HTML('cv.html')
    css = CSS('cv.css')
    html.write_pdf('cv.pdf', stylesheets=[css], font_config=font_config)
