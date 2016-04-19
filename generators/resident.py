class Resident:
  def __init__(self, id, generators):
    self.id = id
    self.region = generators['region'].generate(self.id)
    self.region.addResident(self)
    self.issues = {}
    
    for k in generators['issues'].keys():
      self.issues[k] = generators['issues'][k].generate(self.id)
  def __str__(self):
    s = 'ID: %d\n' % self.id
    s += 'Region: %s\n' % self.region.name
    s += 'Opinions: '
    for k in self.issues.keys():
      s += '%s->%s\t' % (k, ('aye' if self.issues[k] else 'nay'))
    s += '\n'
    return s