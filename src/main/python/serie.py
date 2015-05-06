from directory import Directory
import os
class Serie(object):
  def __init__(self, serieDir):
    self.serieDir = Directory(serieDir)
    self.name = self.serieDir.name
    self.seasons = self.serieDir.subdirs
    self.episodes = []
    
  def gatherEpisodes(self):
    for season in self.seasons:
      seasonDir = Directory(os.path.join(self.serieDir.rootFolder, season))
      for episode in seasonDir.files:
        self.episodes.append(episode)
    for episode in self.serieDir.files:
      self.episodes.append(episode)
