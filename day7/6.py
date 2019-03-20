# -*- coding: utf-8 -*-

# XML
'''
    DOM vs SAX
    操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
    SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

    正常情况下，优先考虑SAX，因为DOM实在太占内存。

    在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

'''
import io ,sys
from xml.parsers.expat import ParserCreate
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self,name):
        print('sax:end_element: %s' % name)

    def char_data(self,text):
        print('sax:char_data: %s' % text)
        


#解析xml
def parser_xml():
    xml = r'''<?xml version="1.0"?>
    <ol>
        <li><a href = "/python">python</a></li>
        <li><a href = "/java">java</a></li>
    </ol>
    '''
    handler = DefaultSaxHandler()

    parser = ParserCreate()

    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)


# HTMLParser

'''
    如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。

    假设第一步已经完成了，第二步应该如何解析HTML呢？

    HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
'''
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHtmlParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(" <%s> " % tag )

    def handle_endtag(self, tag):
        print(" </%s> " % tag )

    def handle_startendtag(self, tag, attrs):
        print(" <%s> " % tag )

    def handle_data(self,data):
        print(data)

    def handle_comment(self,data):
        print("<!--",data,'-->')

    def handle_entityref(self,name):
        print("&%s;" % name)

    def handle_charref(self, name):
         print("&%s;" % name)

parser = MyHtmlParser()

parser.feed('''
    <html>
    <head></head>
    <body>
        <!-- test html parser -->
        <p> Some <a href=\"#\">html</a>Html&nbsp;tutorial...<br>END </p>
        <!-- test html END -->
    </body>
    </html>
''')

'''
    feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

    特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
'''
