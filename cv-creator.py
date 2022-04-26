import argparse
import os
from os.path import exists

import markdown
from pdf2docx import parse
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

MARKDOWN_FILE = 'cv.md'

WEB_CSS_FILE = 'static/web.css'
PDF_CSS_FILE = 'static/pdf.css'
WORD_CSS_FILE = 'static/word.css'

OUTPUT_DIR = 'generated'
HTML_TITLE = '''Richard Kasperowski - Curriculum Vitae'''
HTML_FILE = 'cv.html'
PDF_FILE = 'cv.pdf'
TMP_PDF_FILE = 'tmp-cv.pdf'
DOCX_FILE = 'cv.docx'

if __name__ == '__main__':
    # Handle command-line arg's
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--markdownfile', default=MARKDOWN_FILE,
                        help='the MarkDown file to use as input. default:' + MARKDOWN_FILE)
    parser.add_argument('-o', '--output', default=OUTPUT_DIR,
                        help='output generated files to this directory. default:' + OUTPUT_DIR)
    parser.add_argument('-t', '--title', default=HTML_TITLE,
                        help='<title> of the generated HTML file. default:' + HTML_TITLE)
    args = parser.parse_args()
    markdown_file = args.markdownfile
    output_dir = args.output
    html_title = args.title

    # Create output directory, if necessary
    if not exists(output_dir):
        os.mkdir(output_dir)

    # Convert Markdown file to simple HTML
    with open(markdown_file, 'r') as f:
        text = f.read()
        simple_html = markdown.markdown(text, extensions=['smarty'])

    # Convert simple HTML to PDF and output PDF file
    font_config = FontConfiguration()
    css = CSS(PDF_CSS_FILE, font_config=font_config)
    parsed_html = HTML(string=simple_html)
    parsed_html.write_pdf(output_dir + '/' + PDF_FILE, stylesheets=[css], font_config=font_config)

    # Enhance simple HTML and output HTML file
    full_html = '''<!DOCTYPE html>
<head>
  <title>''' + html_title + '''</title>
  <link rel="stylesheet" href="../''' + WEB_CSS_FILE + '''">
</head>
<body>''' + simple_html + '''</body></html>'''
    with open(output_dir + '/' + HTML_FILE, 'w') as f:
        f.write(full_html)

    # Generate a one-page version of the PDF and output Word file
    font_config = FontConfiguration()
    css = CSS(WORD_CSS_FILE, font_config=font_config)
    parsed_html = HTML(string=simple_html)
    parsed_html.write_pdf(output_dir + '/' + TMP_PDF_FILE, stylesheets=[css], font_config=font_config)
    parse(pdf_file=output_dir + '/' + TMP_PDF_FILE, docx_file=output_dir + '/' + DOCX_FILE)
    os.remove(output_dir + '/' + TMP_PDF_FILE)
