#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kevin W. Potter'
SITENAME = 'Kevin W. Potter'
SITESUBTITLE = ' '
SITEURL = 'localhost:8000'

PATH = 'content'
STATIC_PATHS = ['img','presentations','publications', 'misc']

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'theme/academia'
# THEME = 'notmyidea'
AVATAR = 'Professional_picture.JPG'
# Links widget
LINKS = (('cv', '/misc/CV.pdf'),
         ('email', 'mailto:kevin.w.potter@gmail.com'),
         ('github', 'https://github.com/rettopnivek'))

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 90
DIRECT_TEMPLATES = ('index', 'posts_index', 'tags', 'archives')
PAGINATED_DIRECT_TEMPLATES = ['posts_index']

POSTS_PATHS = ['posts']
POSTS_URL = 'posts/'
POSTS_INDEX_SAVE_AS = 'posts/index.html'

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
