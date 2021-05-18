#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import datetime

AUTHOR = 'Essa Alshammari'
SITENAME = 'بايثون - Python Language'
SITEURL = 'https://pythonarabic.github.io/blog'
# SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Riyadh'

DEFAULT_LANG = 'ar'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('الرئيسية', SITEURL),
    ('الاقسام', SITEURL + "/categories.html"),
    ('الوسوم', SITEURL + "/tags.html"),
    ('الكُتاب', SITEURL + "/authors.html"),
)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


THEME = "pelican-themes/Flex"

SITELOGO = "https://avatars.githubusercontent.com/u/83315320?v=4"

ARTICLE_ORDER_BY = 'reversed-date'

PYGMENTS_STYLE = "tango"

COPYRIGHT_NAME = "Essa Alshammari"
COPYRIGHT_YEAR = datetime.date.today().year

FAVICON = "https://avatars.githubusercontent.com/u/83315320?v=4"

SOCIAL = (
    ("github", "https://github.com/pythonarabic"),
    ("telegram", "https://t.me/arabipython"),
)

# DISQUS_SITENAME = "pythonarabic-github-io-blog"

ARTICLE_URL = 'posts/{date:%Y}/{slug}.html'

ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}.html'

STATIC_PATHS = ['images']
