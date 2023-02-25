from heuristic import *

"""
   Node class used to store information about individual articles
   and how to get there
   
   self              - reference to self
   page              - link to page
   name              - name of article
   h                 - heuristic value (float)
   totalPathWeight   - sum of previous patth weights (int)
   parent            - reference to parent node
   f                 - totalPathWeight + heuristic value (float)
"""
class Node:
   def __init__(self, page, parent):
      self.page = page
      self.name = self.getName(page)
      self.h = Heuristics.calculateH(self.page)
      self.totalPathWeight = 0
      self.parent = parent
      self.f = -1
      
   def setF(self):
      self.f = self.totalPathWeight + self.h
        
   def __eq__(self, other):
      if not isinstance(other, self.__class__):
         return False
      if self.name == other.name and self.h == other.h:
         return True
      else:
         return False
   
   def __lt__(self, other):
      return self.h < self.other
   
   def __hash__(self):
      return hash(self.name)