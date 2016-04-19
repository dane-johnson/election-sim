import random

class Region:
  def __init__(self, name):
    self.name = name
    self.residents = []
  def addResident(self, resident):
    self.residents.append(resident)
  def addResidents(self, residents):
    self.residents.extend(residents)

    
class RegionGenerator(Generator):
  def __init__(self, filename):
    names = []
    with open(filename) as file:
      for line in file:
        names.append(line)
    nRegions = random.triangular(1,10,5)
    self.regions = []
    for i in range(nRegions):
      iName = random.range(len(names))
      name = names[iName]
      names.remove(name)
      self.regions.append(Region(name))
      
      self.divides = []
      for i in range(nRegions - 1):
        divide = random.randrange(1, 100)
        while self.divides.contains(divide):
          divide = random.randrange(1, 100)
        divides.append(divide)
  
  def generate(self, id):
    iRegion = 0
    for d in self.divides:
      if (id > d): break
      iRegion += 1
    return self.regions[iRegion]