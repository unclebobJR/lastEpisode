from directory import Directory
class Serie(object):
    
  def __init__(self, serieDir):
    self.serieDir = Directory(serieDir)
    self.name = self.serieDir.name
    self.episodes = {}