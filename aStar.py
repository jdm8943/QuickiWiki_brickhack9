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

        print("CURR: ", curr)

        for neighbor in getNeighbors(curr):
            if neighbor.page == end:         # if neighbor = goal, return the path
                print("WE ARE AT THE END!!!")
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
                    # neighbor.setF();
    
                
    # TODO Sol get neighbors from a node and return nodes
def getNeighbors(root):
    neighbors = []
    links = root.page.linkedPages()
    for aLink in links:
        neighbors.append(node.Node(aLink, root))
    return neighbors;

# TODO Sol return the cost of a page
def calculateCost(node):
    return 1;

def getPath(node):
    totPath = []
    totPath.append(node)
    while(node.parent is not None):
        totPath.append(node.parent)
        node = node.parent
    return totPath