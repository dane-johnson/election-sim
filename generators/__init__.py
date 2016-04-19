import random

class Generator:
  def generate(self, id):
    raise NotImplementedError()

from generators.region import RegionGenerator
from generators.issue import IssueGenerator

class GeneratorFactory:
  @staticmethod
  def create(regionFilename, issueFilename):
  
    regionNames = []
    with open(regionFilename) as file:
      for line in file:
        if line.startswith('#') or line == '\n' or line == '': continue
        regionNames.append(line[:-1])
    issueNames = []
    
    with open(issueFilename) as file:
      for line in file:
        if line.startswith('#') or line == '\n' or line == '': continue
        issueNames.append(line[:-1])
    
    dict = {}
    dict['region'] = RegionGenerator(regionNames)
    dict['issues'] = {}
    
    for i in range(int(random.triangular(3, 10, 7))):
      iName = random.randrange(len(issueNames))
      name = issueNames[iName]
      issueNames.remove(name)
      dict['issues'][name] = IssueGenerator(name)
    
    return dict