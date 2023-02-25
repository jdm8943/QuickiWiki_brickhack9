from heuristic import *

class Node:
    def __init__(self, page, name, parent):
        # Self, page, name, pathweight (int), parent (node)
        self.page = page
        self.name = name
        self.h = Heuristics.calculateH(self.page)
        self.totalPathWeight = 0
        self.parent = parent
        self.f = -1
        
    def __eq__(self, other):
      if not isinstance(other, self.__class__):
         return False
      if self.name == other.name and self.h == other.h:
         return True
      else:
         return False
      
    def setF(self):
      self.f = self.totalPathWeight + self.h;