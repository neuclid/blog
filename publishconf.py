#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://neuclid.github.io/blog'
RELATIVE_URLS = False

MENUITEMS = (('About', '/blog/pages/about.html'),
             ('Now', '/blog/pages/now.html'),
             ('Archives', '/blog/archives.html'),
             ('Categories', '/blog/categories.html'),
             ('Tags', '/blog/tags.html'),
)

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
