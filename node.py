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
   def __init__(self, page, parent, qw):
      self.page = page
      self.name = page.title() #might be unnecessary since it's a quick command from page      
      self.parent = parent
      if parent is None:
         self.totalPathWeight = 0      #calculating g
      else:
         self.totalPathWeight = 1
      self.h = 0
      self.f = 0
      

   # def getCurrPathWeight(self):
   #    return 1
   
   def calcFn(self, qw):
      self.h = heuristic.Heuristics.calculateH(self.page, qw)
      self.f = self.totalPathWeight + self.h
      # print(self.name + " f(n): " + str(self.f))
      return self.f
        
   def __eq__(self, other):
      if not isinstance(other, self.__class__):
         return False
      if self.name == other.name and self.h == other.h:
         return True
      else:
         return False
   
   def __lt__(self, other):
      return self.f < other.f
   
   def __hash__(self):
      return hash(self.name)
   
   def __str__(self) -> str:
      if self.parent is not None:
         stri =  "[" + self.name + "=> parent: " + self.parent.name + ", f: " + str(self.f) + ", g:" + str(self.totalPathWeight)
      else:
         stri =  "[" + self.name + "=> parent: NONE";
      return stri