#!/usr/bin/env python


from run_html_render import *


def test_step1():

	page = hr.Element()
	page.append("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text")
	page.append("And here is another piece of text -- you should be able to add any number")
	render(page, "test_html_output1.html")

	test_output = open("test_html_output1.html")
	expected_output = open("expected_output1.html")
	
	assert test_output.read() == expected_output.read()


def test_step2():

	page = hr.Html()
	body = hr.Body()
	body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))
	body.append(hr.P(u"And here is another piece of text -- you should be able to add any number"))
	page.append(body)
	render(page, u"test_html_output2.html")

	test_output = open("test_html_output2.html")
	expected_output = open("expected_output2.html")
	
	assert test_output.read() == expected_output.read()
	

def test_step3():

	page = hr.Html()
	head = hr.Head()
	head.append(hr.Title(u"PythonClass = Revision 1087:"))
	page.append(head)
	body = hr.Body()
	body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))
	body.append(hr.P(u"And here is another piece of text -- you should be able to add any number"))
	page.append(body)
	render(page, u"test_html_output3.html")

	test_output = open("test_html_output3.html")
	expected_output = open("expected_output3.html")

	assert test_output.read() == expected_output.read()


def test_step4():

	page = hr.Html()
	head = hr.Head()
	head.append(hr.Title(u"PythonClass = Revision 1087:"))
	page.append(head)
	body = hr.Body()
	body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text", style=u"text-align: center; font-style: oblique;"))
	page.append(body)
	render(page, u"test_html_output4.html")

	test_output = open("test_html_output4.html")
	expected_output = open("expected_output4.html")

	assert test_output.read() == expected_output.read()


def test_step5():

	page = hr.Html()
	head = hr.Head()
	head.append(hr.Title(u"PythonClass = Revision 1087:"))
	page.append(head)
	body = hr.Body()
	body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text", style=u"text-align: center; font-style: oblique;"))
	body.append(hr.Hr())
	page.append(body)
	render(page, u"test_html_output5.html")

	test_output = open("test_html_output5.html")
	expected_output = open("expected_output5.html")

	assert test_output.read() == expected_output.read()


def test_step6():

	page = hr.Html()
	head = hr.Head()
	head.append(hr.Title(u"PythonClass = Revision 1087:"))
	page.append(head)
	body = hr.Body()
	body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text", style=u"text-align: center; font-style: oblique;"))
	body.append(hr.Hr())
	body.append(u"And this is a ")
	body.append(hr.A(u"http://google.com", 'link'))
	body.append(u"to google")
	page.append(body)
	render(page, u"test_html_output6.html")

	test_output = open("test_html_output6.html")
	expected_output = open("expected_output6.html")

	assert test_output.read() == expected_output.read()


def test_step7():

	page = hr.Html()
	head = hr.Head()
	head.append(hr.Title(u"PythonClass = Revision 1087:"))
	page.append(head)
	body = hr.Body()
	body.append(hr. H(2, u"PythonClass - Class 6 example") )
	body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
	               style=u"text-align: center; font-style: oblique;"))
	body.append(hr.Hr())
	list = hr.Ul(id=u"TheList", style=u"line-height:200%")
	list.append( hr.Li(u"The first item in a list") )
	list.append( hr.Li(u"This is the second item", style="color: red") )
	item = hr.Li()
	item.append(u"And this is a ")
	item.append( hr.A(u"http://google.com", u"link") )
	item.append(u"to google")
	list.append(item)
	body.append(list)
	page.append(body)
	render(page, u"test_html_output7.html")

	test_output = open("test_html_output7.html")
	expected_output = open("expected_output7.html")

	assert test_output.read() == expected_output.read()


def test_step8():

	page = hr.Html()
	head = hr.Head()
	head.append( hr.Meta(charset=u"UTF-8") )
	head.append(hr.Title(u"PythonClass = Revision 1087:"))
	page.append(head)
	body = hr.Body()
	body.append( hr.H(2, u"PythonClass - Class 6 example") )
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
	render(page, u"test_html_output8.html")

	test_output = open("test_html_output8.html")
	expected_output = open("expected_output8.html")

	assert test_output.read() == expected_output.read()








