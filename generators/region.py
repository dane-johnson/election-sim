from generators import Generator

import random

class Region:
  def __init__(self, name):
    self.name = name
    self.residents = []
  def addResident(self, resident):
    self.residents.append(resident)
  def addResidents(self, residents):
    self.residents.extend(residents)
  def __str__(self):
    return self.name

    
class RegionGenerator(Generator):
  def __init__(self, names):
    nRegions = int(random.triangular(2,10,5))
    self.regions = []
    for i in range(nRegions):
      iName = random.randrange(len(names))
      name = names[iName]
      names.remove(name)
      self.regions.append(Region(name))
      
      self.divides = []
      for i in range(nRegions - 1):
        divide = random.randrange(1, 100)
        while divide in self.divides:
          divide = random.randrange(1, 100)
        self.divides.append(divide)
      self.divides.sort()
  
  def generate(self, id):
    iRegion = 0
    for d in self.divides:
      if (id < d): break
      iRegion += 1
    return self.regions[iRegion]
    
  def __str__(self):
    s = ''
    for r in self.regions: s += '%s\n' % r
    first = True
    for d in self.divides:
      if not first: s += ', '
      s += str(d)
      first = False
    s += '\n'
    return s
  def __iter__(self):
    return iter(self.regions)