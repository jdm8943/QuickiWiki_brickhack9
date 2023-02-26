import pywikibot as pw
import node

site = pw.Site('en', 'wikipedia')  # The site we want to run our bot on
site.login()

class nodeB:
    def __init__(self, page, parent):
        self.page = page
        self.parent = parent
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.name == other.name:
            return True
        else:
            return False
      

def runBFS(start, end):
    que = []
    visited = {}

    que.append(nodeB(start, None))
    visited.add(start.title())
    
    while que:
        vert = que.pop()

        for neighbor in getNeighbors(vert):
            if vert == end:
                return getPath(vert)
            if neighbor not in visited:
                visited.add(neighbor)
                que.append(neighbor)

    return False


def getNeighbors(root, visited):
    neighbors = []
    links = root.page.linkedPages()
    for aLink in links:
        neigh = node.Node(aLink, root, qw)
        nam = neigh.name.lower()
        if not nam.startswith("list") and not nam.startswith("category:") and not nam.startswith("help:") and not nam.startswith("template:"):
            neighbors.append(neigh)
    return neighbors;

def getPath(node):
    totPath = []
    totPath.append(node)
    while(node.parent is not None):
        totPath.append(node.parent)
        node = node.parent
    return totPath