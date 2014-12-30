#!/usr/bin/env python
"""

    dzmerge.py
    ------

    :copyright: (c) 2014 by Philipp Jovanovic <philipp@jovanovic.io>.
    :license: BSD (3-Clause), see LICENSE for more details.
"""

import base64
import imghdr
import lxml.html
import lxml.etree
import sys
import os.path

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print "Usage: ./dzmerge.py in.html out.html"
        sys.exit(-1)

    s = ''

    with open(sys.argv[1], 'rb') as f:
        x = f.read()
        html = lxml.html.document_fromstring(x)
        for element, attributes, link, pos in html.iterlinks():

            if os.path.isfile(link):

                if element.tag == 'img':
                    """ include images """
                    img_b64 = ''
                    with open(link, 'rb') as g:
                        img_b64 = base64.b64encode(g.read())
                    img_type = imghdr.what(link)
                    if img_type == None: # hack
                        img_type = 'svg+xml'
                    element.set('src','data:image/'+img_type+';charset=utf-8;base64,'+img_b64)

                elif element.tag == 'a' or element.tag == 'link':
                    """ include stylesheets """
                    css = ''
                    with open(link, 'rb') as g:
                        css = g.read()
                    style = lxml.etree.Element("style")
                    style.text = '\n'+css+'\n'
                    html.insert(1,style)
                    element.getparent().remove(element)

        """ remove redundant tags (added by default through lxml) """
        lxml.etree.strip_tags(html,'body')
        lxml.etree.strip_tags(html,'head')

        """ generate final html string """
        s = lxml.html.tostring(html, encoding="utf-8", doctype="<!DOCTYPE html>")

    with open(sys.argv[2], 'w') as f:
        f.write(s)

    sys.exit(0)
