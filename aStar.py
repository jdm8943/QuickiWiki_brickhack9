import pywikibot as pw
import node
from heapq import *

site = pw.Site('en', 'wikipedia')  # The site we want to run our bot on
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
        neighbors = []
        links = pw.linkedPages()
        for aLink in links:
            neighbors.add(node.Node(aLink, root))
        return neighbors;
    
    # TODO Sol return the cost of a page
    def calculateCost(node):
        return 0;
    
    def getPath():
        return 0;