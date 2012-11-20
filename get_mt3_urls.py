# -*- encoding:utf8 -*-
u'''
Crawl the Movable Type 3 "archives.html" page and it parse to url-title sets

@python == 2.6.6
@dependency requests v0.14.2 <http://pypi.python.org/pypi/requests>
@dependency pyquery v1.2.2 <http://pypi.python.org/pypi/pyquery>
'''
import os
import sys
import re
import getopt
import traceback
import requests
from pyquery import PyQuery

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MT_ARCHIVES_URL = 'http://kjirou.sakura.ne.jp/mt/archives.html'
WP_ARCHIVES_URL = BASE_DIR + '/data/wordpress.2012-11-20.xml'

def _main():
    mt_pages = {}
    wp_pages = {}

    # MT
    request = requests.get(MT_ARCHIVES_URL)
    content = request.content.decode('utf8')
    document = PyQuery(content);
    archive_list = document('#pagebody .archive-list a')
    for archive in archive_list:
        archive = PyQuery(archive)
        mt_pages[unicode(archive.text())] = unicode(archive.attr('href'))

    print mt_pages

    # WP

_main()
