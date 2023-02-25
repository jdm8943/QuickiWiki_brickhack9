# Pywikibot needs a config file:
pywikibot_config = r"""# -*- coding: utf-8  -*-


mylang = 'en'
family = 'wikipedia'
usernames['wikipedia']['en'] = 'SolKr'"""

with open('user-config.py', 'w', encoding="utf-8") as f:
    f.write(pywikibot_config)

import pywikibot
from heapq import *

site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
site.login()

def a_star(start, end):    # start/end are nodes for a*
    self = set();
    start.totalPathWeight = 0      # distance from start    
    open = [start]
    closed = set()
    while open:
        curr = heappop(open)    # gets current node by getting max f(n)
        if curr in closed:      # if curr has already been visited go next
            continue
        closed.add(curr)        # add curr to closed
        if curr == end:         # if curr = goal return the path
            return path         # TODO create func that gets 
        for weight, neighbor in getNeighbors(curr):
            g = curr.g + weight
            if g < neighbor.g:
                neighbor.g = g
                neighbor.f = g + self.heuristic(neighbor.location, end.location)
                neighbor.parent = curr
                heappush(open, neighbor)
                
    def getNeighbors(root):
        return 0;