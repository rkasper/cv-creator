import argparse
import os
import pathlib
from os.path import exists

import markdown
from pdf2docx import parse
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


WEB_CSS_FILE = 'static/web.css'
PDF_CSS_FILE = 'static/pdf.css'
WORD_CSS_FILE = 'static/word.css'

TMP_PDF_FILE = 'tmp-cv.pdf'

DEFAULT_MARKDOWN_FILE = 'cv.md'
DEFAULT_OUTPUT_DIR = 'generated'
DEFAULT_HTML_TITLE = '''Richard Kasperowski - Curriculum Vitae'''
DEFAULT_HTML_FILE = 'cv.html'
DEFAULT_PDF_FILE = 'cv.pdf'
DEFAULT_DOCX_FILE = 'cv.docx'


# Convert Markdown file to simple HTML
def generate_simple_html(markdown_file):
    with open(markdown_file, 'r') as f:
        text = f.read()
        simple_html = markdown.markdown(text, extensions=['markdown.extensions.smarty'])
    return simple_html


# Convert simple HTML to PDF and output PDF file
def generate_pdf(simple_html, output_file):
    font_config = FontConfiguration()
    css = CSS(PDF_CSS_FILE, font_config=font_config)
    parsed_html = HTML(string=simple_html)
    parsed_html.write_pdf(output_file, stylesheets=[css], font_config=font_config)


# Enhance simple HTML and output HTML file
def generate_enhanced_html(simple_html, html_title, output_file):
    full_html = '''<!DOCTYPE html>
<head>
  <title>''' + html_title + '''</title>
  <link rel="stylesheet" href="../''' + WEB_CSS_FILE + '''">
</head>
<body>''' + simple_html + '''</body></html>'''
    with open(output_file, 'w') as f:
        f.write(full_html)


# Generate a one-page version of the PDF and output Word file
def generate_word(simple_html, output_file):
    font_config = FontConfiguration()
    css = CSS(WORD_CSS_FILE, font_config=font_config)
    parsed_html = HTML(string=simple_html)
    parsed_html.write_pdf(TMP_PDF_FILE, stylesheets=[css], font_config=font_config)
    parse(pdf_file=TMP_PDF_FILE, docx_file=output_file)
    os.remove(TMP_PDF_FILE)


if __name__ == '__main__':
    # Handle command-line arg's
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--markdownfile', default=DEFAULT_MARKDOWN_FILE,
                        help='the MarkDown file to use as input. default: ' + DEFAULT_MARKDOWN_FILE)
    parser.add_argument('-o', '--output', default=DEFAULT_OUTPUT_DIR,
                        help='output generated files to this directory. default: ' + DEFAULT_OUTPUT_DIR)
    parser.add_argument('-t', '--title', default=DEFAULT_HTML_TITLE,
                        help='<title>Title Text</title> of the generated HTML file. default: ' + DEFAULT_HTML_TITLE)
    args = parser.parse_args()

    # Create output directory, if necessary
    if not exists(args.output):
        os.mkdir(args.output)

    # Generate the awesome looking outpu documents
    filename_root = filename = pathlib.Path(args.markdownfile).stem
    simple_html = generate_simple_html(args.markdownfile)
    generate_pdf(simple_html, args.output + '/' + filename_root + '.pdf')
    generate_enhanced_html(simple_html, args.title, args.output + '/' + filename_root + '.html')
    generate_word(simple_html, args.output + '/' + filename_root + '.docx')
