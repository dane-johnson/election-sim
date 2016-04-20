from generators import Generator

import random

AYE = 1
NAY = 0

class IssueGenerator(Generator):
  def __init__(self, name):
    self.name = name
    self.mod = random.randrange(2)
    nRegions = int(random.triangular(2, 10, 5))
    
    self.divides = []
    for i in range(nRegions - 1):
      divide = None
      while divide == None or divide in self.divides:
        divide = random.randrange(1,100)
      self.divides.append(divide)
    self.divides.sort()
  def generate(self, id):
    iRegion = 0
    for d in self.divides:
      if id < d: break
      iRegion += 1
    return (iRegion % 2) ^ self.mod #use the mod to ensure it does not always start nay