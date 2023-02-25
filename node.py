class Node:
    def __init__(self, name, h, g, totalPathWeight, parent):
        # Self, name, heuristic value (float), total paths (int), pathweight (int), parent (node)
        self.name = name
        self.h = h
        self.g = g
        self.totalPathWeight = totalPathWeight
        self.parent = parent
        self.f = totalPathWeight + h
        
    def __eq__(self, other):
      if not isinstance(other, self.__class__):
         return False
      if self.name == other.name and self.h == other.h:
         return True
      else:
         return False