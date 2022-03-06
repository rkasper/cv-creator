# cv-creator

I want a version-controlled resume that's always ready for people to read, always in a format that looks good on screen and in print.

I want to edit my resume once, and have it look the same in all output formats...

This little script seamlessly converts my CV from Markdown to elegant PDF. Along the way, it generates a great looking HTML file and a good-enough Word file. (The vertical line spacing in the Word file is wonky; to fix it, you'll have to manually reformat everything to be single-spaced.)

## How does it work?

_cv-creator_ takes an enhanced markdown file, converts it to HTML (using [Python-Markdown](https://python-markdown.github.io)), and converts the HTML to PDF thanks to [WeasyPrint](https://weasyprint.org/).

What's that - an enhanced markdown file? Yep, we use [SmartyPants](https://python-markdown.github.io/extensions/smarty/) to do things like convert -- to &endash. How cool is that?!?  

Hey, what?!? Customizing the PDF file?!? Yep, that's right! Take a look at [CSS Paged Media Module Level 3](https://www.w3.org/TR/css-page-3/).

Finally, we use [pdf2docx](https://pypi.org/project/pdf2docx/) to convert the PDF file to Word.

## How to use it?

1. Create your CV in Markdown as `cv.md`.
2. Adjust the CSS file `cv.css`.
3. Run the script: `python3 cv-creator`
4. Enjoy the generated output files, `cv.html`, `cv.pdf`, and `cv.docx`.

## Credit
[Richard Kasperowski](https://kasperowski.com) created this. I was inpired by, and got started by forking, [Romain Ginestou](https://github.com/rginestou) 's [MarkReport](https://github.com/rginestou/MarkReport). Thanks, Romain!

## TODO
Here are some things left to do:

* ~~Replace the LICENSE file.~~
* ~~Remove setup.py.~~
* ~~Clean up my pip database. Start over with the minimum 'pip install's. Create a requirements.txt file.~~
* ~~Rename main.py.~~
* ~~Clean up the original repo and make my first big commit+push.~~
* ~~Move generated files to their own subdir.~~
* ~~Add the rest of my CV to the .md file.~~
* ~~Add a page on my website that embeds the .pdf file from github.com.~~
* ~~Add this project to my CV.~~
* ~~Tweak the style of hyperlinks.~~
* ~~Tweak the fonts so they look more like the ones in the Pages version of my CV.~~
  * ~~H1~~
  * ~~H2~~
  * ~~H3~~
  * ~~body~~
  * ~~footer~~
* ~~Student reviews: italicize so they look like quotes.~~
* ~~Tweak the layout of lists so top-level lists are left-justified.~~
* ~~Tweak the layout of H2 and H3 so they display in caps.~~
* ~~Tweak the page layout so it looks more like the Pages version of my CV.~~
* ~~Italicize book titles and cum laude.~~
* ~~Generate a styled HTML file.~~
* ~~Improve web view.~~
* ~~Refactor: factor-out the common parts of the CSS files.~~
* ~~Generate a Word file.~~
* Generalize it as a web app?
