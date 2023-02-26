import pywikibot as pw
import node

site = pw.Site('en', 'wikipedia')  # The site we want to run our bot on
site.login()

class nodeB:
    def __init__(self, page, parent):
        self.page = page
        self.name = page.title()
        self.parent = parent
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.name == other.name:
            return True
        else:
            return False

    def __str__(self) -> str:
      if self.parent is not None:
         stri =  "[" + self.page.title() + "=> parent: " + self.parent.page.title()
      else:
         stri =  "[" + self.page.title() + "=> parent: NONE";
      return stri
    
    def __hash__(self):
      return hash(self.name)
      

def runBFS(start, end):
    start = nodeB(start, None)
    que = [start]
    visited = set()

    visited.add(start)
    
    while que:
        vert = que.pop()
        print("Curr: ", vert)
        for neighbor in getNeighbors(vert, visited):
            if neighbor.page == end:
                return getPath(neighbor)
            if neighbor.page not in visited:
                visited.add(neighbor)
                que.append(neighbor)

    return False


def getNeighbors(root, visited):
    neighbors = []
    links = root.page.linkedPages()
    for aLink in links:
        neigh = nodeB(aLink, root)
        nam = neigh.name.lower()
        if neigh in visited:
            continue
        # else:
        #     neighbors.append(neigh)
        elif not nam.startswith("list") and not nam.startswith("category:") and not nam.startswith("help:") and not nam.startswith("template:")and not nam.startswith("help:") and not nam.startswith("portal:") and not nam.startswith("draft:") and not nam.startswith("template talk:") and not nam.startswith("user talk:"):
            neighbors.append(neigh)
    return neighbors;

def getPath(node):
    totPath = []
    totPath.append(node)
    while(node.parent is not None):
        totPath.append(node.parent)
        node = node.parent
    return totPath