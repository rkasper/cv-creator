# cv-creator

I want the HTML and PDF versions of my resume to look the same. I want to edit my resume once, and have it look the same in both file formats...

This little script seamlessly converts your CV from Markdown to elegant PDF.

## How does it work?

_cv-creator_ takes an enhanced markdown file, converts it to HTML (using [Python-Markdown](https://python-markdown.github.io)), and converts the HTML to PDF thanks to [WeasyPrint](https://weasyprint.org/).

What's that - an enhanced markdown file? Yep, we use [SmartyPants](https://python-markdown.github.io/extensions/smarty/) to do things like convert -- to &endash. How cool is that?!?  

Hey, what?!? Customizing the PDF file?!? Yep, that's right! Take a look at [CSS Paged Media Module Level 3](https://www.w3.org/TR/css-page-3/).

## How to use it?

1. Create your CV in Markdown as `cv.md`.
2. Adjust the CSS file `cv.css`.
3. Run the script: `python3 cv-creator`
4. Enjoy the generated output files, `cv.html` and `cv.pdf`.

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
* Tweak the fonts so they look more like the ones in the Pages version of my CV.
  * ~~H1~~
  * ~~H2~~
  * ~~H3~~
  * ~~body~~
  * ~~footer~~
* Student reviews: italicize so they look like quotes.
* Tweak the layout of lists so top-level lists are left-justified.
* Tweak the layout of H2 and H3 so they display in caps.
* Tweak the page layout so it looks more like the Pages version of my CV.* Add CSS to the generated HTML file.
* Generate a .doc file.
* Generalize it as a web app?
