#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ka2n'
AUTHOR_EMAIL = u'katsumai@gmail.com'
SITENAME = u'ktmtt'
SITESUBTITLE = u''
SITEURL = 'http://d.ktmtt.com'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_RSS = 'feeds/atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_MAX_ITEMS = 20

DEFAULT_PAGINATION = 12

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

THEME = "./themes/pure"

# URL
ARTICLE_URL = '-/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '-/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Format
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

STATIC_PATHS = [
    "content/images",
    "content/files",
    "content/extra/CNAME",
    "content/extra/favicon.ico"
]

EXTRA_PATH_METADATA = {
    "content/extra/CNAME": {'path': 'CNAME'},
    "content/extra/favicon.ico": {'path': 'favicon.ico'}
}

READERS = {
    "html": None
}

MENUITEMS = (
    ('@ka2n', 'https://twitter.com/ka2n'),
    ('GitHub', 'https://github.com/ka2n'),
)

# Plugin
PLUGIN_PATH = './plugins'
PLUGINS = ["gravatar"]

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

TWITTER_USERNAME = 'ka2n'

GOOGLE_ANALYTICS = "UA-62172-11"

MESSAGE_LEAF = True

USE_OPEN_GRAPH = True

GOOGLE_PLUS_ID = "+KatsumaIto"
