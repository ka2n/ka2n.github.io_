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
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "./themes/pure"

# URL
ARTICLE_URL = '-/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '-/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Format
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

STATIC_PATHS = [
    "images",
    "files",
    "extra/CNAME",
    "extra/favicon.ico"
]

EXTRA_PATH_METADATA = {
    "extra/CNAME": {'path': 'CNAME'},
    "extra/favicon.ico": {'path': 'favicon.ico'}
}

READERS = {
    "html": None
}

MENUITEMS = (
        ('GitHub', 'http://github.com/ka2n'),
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
