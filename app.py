import sys
import markdown
from pygments.formatters import HtmlFormatter
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

# Variable
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

# Function names

# Indexes the last 4 pages
@app.route('/')
def index():
    a = []
    for page in pages:
        if len(a)>=4:
            break
        a.append(page)
    return render_template('index.html', pages=a,len=len(a))

# Render the about me page
@app.route('/about.html')
def about():
    return render_template('about.html')

# Helper function for day
def day(i):
  if i=="1":
      return "1st"
  elif i=="2":
      return "2nd"
  elif i=="3":
      return "3rd"
  else:
      return i+"th"

# Lists all the blog posts by their year
@app.route('/blog.html')
def blog():
    # TODO : Very redundant, could do some metaprogramming stuff?
    a_2023 = []
    a_2022 = []
    a_2021 = []
    for page in pages:
        date = int(str(page.meta['date'])[:4])
        mon = str(page.meta['date'].strftime('%B'))
        day1 = day(str(int(page.meta['date'].strftime('%d'))))
        str1 = day1+" " + mon
        if date ==2022:
            a_2022.append( (page,str1))
        elif date ==2021:
            a_2021.append((page,str1))
        elif date ==2023:
            a_2023.append((page,str1))
    return render_template('blog.html',a_2023=a_2023,a_2022=a_2022,a_2021=a_2021)

# List all the pages for freezer
@freezer.register_generator
def pagelist():
    for page in pages:
        yield url_for('page', path=page.path)

# Rendering a blog post
@app.route('/<path:path>.html')
def page(path):
    formatter = HtmlFormatter(style="stata-dark",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    page = pages.get_or_404(path)
    # Look for the markdown and render it
    f =  open("./pages/"+path+".md", "r")
    md_template_string = markdown.markdown(
        f.read()[3:].split("---")[1], extensions=["fenced_code", "codehilite",'mdx_math']
    )
    
    md_css_string = "<style>" + css_string + "</style>"
    f.close()
    return render_template("page.html",page=md_css_string+md_template_string)

# Main function, choose if you would like to build or test dynamically.
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=5001)
