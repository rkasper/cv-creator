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

1. Set up your dev environment.
   2. Install Python 3.11. 
   3. Install packages. 
   4. Install weasyprint: `brew install weasyprint`.
1. Create your CV in Markdown as `cv.md`.
1. Create your resume in Markdown as `resume.md`.
1. Adjust the CSS files.
1. Run the script: `./generate-cv-and-resume.sh`
1. Enjoy the generated output files, `cv.html`, `cv.pdf`, `cv.docx`, `resume.html`, `resume.pdf`, and `resume.docx`. (You might want to manually add some footers or other formatting to the generated Word file.)

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
* ~~Improve the Word file. Here's an idea for a hack: generate a 1-page PDF, on a page that's like 1000 inches long. Convert that PDF to Word.~~
* ~~Refactor: main has duplicated code, and it's a little too long.~~
* Automatically generate resume from cv.md. Heuristic: use the first sentence of each section in the CV as the one and only one sentence in the resume.
* Tweak speaking sessions: highlight freshness. First date should be most recent presentation. "Also at" dates should be reverse-chronological order.
* Add private keynotes & sessions.
* Generalize it as a web app?
