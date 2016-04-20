from generators.issue import AYE, NAY

class Pollster:
  def __init__(self, regions, issues, residents):
    self.regions = regions
    self.residents = residents
    self.issues = issues
  def popularOpinionOnIssue(self, issue, region = None):
    if issue not in self.issues: raise InvalidPollError(issue)
    aye = 0
    nay = 0
    if region == None:
      residents = self.residents
    else:
      residents = region.residents
    for r in residents:
      if r.issues[issue] == AYE:
        aye += 1
      else:
        nay += 1
    return (aye, nay)
  def electoralCollegeOnIssue(self, issue):
    if issue not in self.issues: raise InvalidPollError(issue)
    aye = 0
    nay = 0
    for r in self.regions:
      ayes, nays = self.popularOpinionOnIssue(issue, r)
      if ayes > nays:
        aye += len(r.residents)
      elif ayes < nays:
        nay += len(r.residents)
    return (aye, nay)
  def popularOpinionOnCandidates(self, candidates, region = None):
    red, blue = candidates
    vRed = vBlue = 0
    if region == None:
      residents = self.residents
    else:
      residents = region.residents
    for r in residents:
      winner = r.vote(candidates)
      if winner == None:
        break
      elif winner == red:
        vRed += 1
      elif winner == blue:
        vBlue += 1
    return (vRed, vBlue)
    
class InvalidPollError(Exception):
  def __init__(self, value):
    self.value = value