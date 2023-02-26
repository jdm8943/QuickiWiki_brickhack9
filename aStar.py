import pywikibot as pw
import node
from heapq import *

site = pw.Site('en', 'wikipedia')  # The site we want to run our bot on
site.login()

def runAStar(start, end):    # start/end are nodes for a*
    self = set();
    start = node.Node(start, None)
    start.totalPathWeight = 0      # distance from start    
    open = [start]
    closed = set()

    while open:
        curr = heappop(open)    # gets current node by getting max f(n)

        closed.add(curr)        # add curr to closed

        # print("CURR: ", curr)

        for neighbor in getNeighbors(curr):
            if neighbor.page == end:         # if neighbor = goal, return the path
                return getPath(neighbor)
            if neighbor in closed:      # if curr has already been visited go next
                continue
            else:
                # neighbor.totalPathWeight = neighbor.parent.totalPathWeight + calculateCost(neighbor)
                try:
                    #if in heap and neigh f val is less, change neighbor.
                    ind = open.index(neighbor)
                    if neighbor.f < open[ind].f:
                        open[ind] = neighbor
                except:
                    #if not in heap, add it to heap.
                    heappush(open, neighbor)
    
                

def getNeighbors(root):
    neighbors = []
    links = root.page.linkedPages()
    for aLink in links:
        neigh = node.Node(aLink, root)
        nam = neigh.name.lower()
        if not nam.startswith("list") and not nam.startswith("category:") and not nam.startswith("help:") and not nam.startswith("template:"):
            neighbors.append(node.Node(aLink, root))
    return neighbors;

def getPath(node):
    totPath = []
    totPath.append(node)
    while(node.parent is not None):
        totPath.append(node.parent)
        node = node.parent
    return totPath