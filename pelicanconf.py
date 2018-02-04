#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from pyembed.rst import PyEmbedRst
PyEmbedRst().register()

AUTHOR = 'neuclid'
SITETITLE = 'higher abstractions'
#ABOUT_ME = "Wanderer"
SITENAME = "higher abstractions"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

LOCALE = ("en_US","en_US.utf8")

#DATE_FORMATS = {
#    'en': ((u'en_US', 'utf8'), u'%a, %d %b %Y',)
#}

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None
FAVICON = '/static/favicon.ico'
#SITELOGO = '/peijunz.jpg'
#AVATAR = '/static/site.png'
#SITELOGO = '/static/site.png'
# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
   ('Twitter', 'http://twitter.com/binaryminery'),
   ('Github', 'http://github.com/neuclid'),
   )
DISPLAY_TAGS_INLINE = True
MAIN_MENU = True
HOME_HIDE_TAGS = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU=False
DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives',
'tags'))
MENUITEMS = (('About','/pages/about.html'),
             ('Now','/pages/now.html'),
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
)
#USE_LESS = False
DEFAULT_DATE = 'fs'
PYGMENTS_STYLE = 'default'
DEFAULT_PAGINATION = 10
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = "superhero"
DISPLAY_BREADCRUMBS=True
DISPLAY_CATEGORY_IN_BREADCRUMBS=True
BOOTSTRAP_NAVBAR_INVERSE=False

STATIC_PATHS = ['static', 'code']

#OUTPUT_SOURCES = True
#OUTPUT_SOURCES_EXTENSION = '.txt'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'authors', 'archives', 'search')
MARKUP = ('md', 'ipynb', 'rst')
PLUGIN_PATHS = ['plugins','pelican-plugins']
PLUGINS = ['render_math', 'ipynb2pelican', 'liquid_tags.include_code',
           'pelican-toc', 'tag_cloud', 'tipue_search', 'neighbors','i18n_subsites']
IGNORE_FILES = ['.ipynb_checkpoints']
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
MATHJAX_CDN="/mathjax/MathJax.js"
TOC = {
    'TOC_HEADERS' : '^h[2-4]',
    'TOC_RUN'     : 'true',
    'TOC_INCLUDE_TITLE': 'false',
}


# CUSTOM_CSS="static/css/custom.css"

# the ipynb2pelican is the modified one by PeiJun: https://github.com/peijunz/ipynb2pelican#metacell

# pyembed instructions here: https://pyembed.github.io/usage/rst/

#ToDos

# Add TravisCI like PeiJun
# LINKS = (('<img alt="Build Status" src="https://travis-ci.org/peijunz/peijunz.github.io.svg?branch=src" style="max-width:100%;">', 'https://travis-ci.org/peijunz/peijunz.github.io'),
#        ('<i class="fa fa-code fa-lg"></i> Source of Contents', 'https://github.com/peijunz/peijunz.github.io/tree/src/content'))

# Inlcude pyembed