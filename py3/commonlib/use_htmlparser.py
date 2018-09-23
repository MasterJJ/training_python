#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_startag(self, tag, attrs):
        print('<%s>' % tag)
        
    def handle_endtag(self, tag):
        print('<%s>' % tag)

    def handle_startendtagg(self, tag, attrs):
        print('<%s>' % tag)

    def handle_date(self, date):
        print(date)

    def handle_comment(self, date):
        print('<!--', date, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END<\p>
</body></html>''')
