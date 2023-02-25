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
        for neighbor in getNeighbors(curr):
            neighbor.totalPathWeight = neighbor.parent.totalPathWeight + calculateCost(neighbor)
            if curr.totalPathWeight < neighbor.totalPathWeight:
                neighbor.parent = curr
                neighbor.setF();
                heappush(open, neighbor)
                
    # TODO Sol get neighbors from a node and return nodes
    def getNeighbors(root):
        return 0;
    
    # TODO Sol return the cost of a page
    def calculateCost(node):
        return 0;