class Resident:
  def __init__(self, id, generators):
    self.id = id
    self.region = generators['region'].generate(self.id)
    self.region.addResident(self)
    self.issues = {}
    
    for k in generators['issues'].keys
      self.issues[k] = generators['issues'][k]