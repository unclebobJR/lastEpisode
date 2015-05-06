from directory import Directory
from serie import Serie
class LastEpisode(object):
    
  def __init__(self, rootDir):
    self.rootDir = Directory(rootDir)
    self.series = {}

  def gatherSeries(self):
    for serie in self.rootDir.subdirs:
      self.series[serie] = Serie(self.rootDir.join(serie))