#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ka2n'
SITENAME = u'ktmtt'
SITESUBTITLE = u'シンプルになりました'
SITEURL = ''

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME="ktmtt"

# URL
ARTICLE_URL = '-/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '-/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Format
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

FILES_TO_COPY = (
        ('extra/CNAME', 'CNAME'),
)
