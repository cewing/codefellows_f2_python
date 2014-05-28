
import py.test
import html_render as hr
import codecs
import cStringIO

# taking run_html_render's render function to test the file out 
def render(page, filename):
   """
   render the tree of elements

   This uses cSstringIO to renderto memory, then dump to console and
   write to file -- very handy!
   """

   f = cStringIO.StringIO()
   page.render(f)

   f.reset()

   print f.read()

   f.reset()
   codecs.open(filename, 'w', encoding="utf-8").write( f.read() )


#Using only Step 8 for testing as the steps are additive.
page = hr.Html()


head = hr.Head()

head.append(hr.Title(u"PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append( hr.Header(2, u"PythonClass - Class 6 example") )

body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
               style=u"text-align: center; font-style: oblique;"))

body.append(hr.Hr())

list = hr.Ul(id=u"TheList", style=u"line-height:200%")

list.append( hr.Li(u"The first item in a list") )
list.append( hr.Li(u"This is the second item", style="color: red") )

item = hr.Li()
item.append(u"And this is a ")
item.append( hr.A(u"http://google.com", "link") )
item.append(u"to google")

list.append(item)

body.append(list)

page.append(body)

render(page, u"test_html_render.html")
f = f = open(u"test_html_render.html", 'r')

def test_tag_html():
    
    hr...  ==  f....

    
tests...


f.close()
