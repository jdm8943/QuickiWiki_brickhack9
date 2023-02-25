import heuristic

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
      self.name = page.title() #might be unnecessary since it's a quick command from page
      self.h = heuristic.Heuristics.calculateH(self.page)
      self.parent = parent
      if parent is not None:
         self.totalPathWeight = 0      #calculating g
      else:
         self.totalPathWeight = parent.totalPathWeight + self.getCurrPathWeight(page)
      self.f = self.totalPathWeight + self.h

   def getCurrPathWeight(self, page):
      return 1
        
   def __eq__(self, other):
      if not isinstance(other, self.__class__):
         return False
      if self.name == other.name and self.h == other.h:
         return True
      else:
         return False
   
   def __lt__(self, other):
      return self.h < other.h
   
   def __hash__(self):
      return hash(self.name)
   
   def __str__(self) -> str:
      return self.name