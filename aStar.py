# Pywikibot needs a config file:
pywikibot_config = r"""# -*- coding: utf-8  -*-


mylang = 'en'
family = 'wikipedia'
usernames['wikipedia']['en'] = 'SolKr'"""

with open('user-config.py', 'w', encoding="utf-8") as f:
    f.write(pywikibot_config)

import pywikibot

site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
site.login()

import heapq


