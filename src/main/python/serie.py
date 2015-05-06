from directory import Directory
import os
from episode import Episode
class Serie(object):
  def __init__(self, serieDir):
    self.serieDir = Directory(serieDir)
    self.name = self.serieDir.name
    self.seasons = self.serieDir.subdirs
    self.episodes = []
    
  def gatherEpisodes(self):
    for season in self.seasons:
      seasonDir = Directory(os.path.join(self.serieDir.rootFolder, season))
      self.addToEpisodes(seasonDir.files)
    self.addToEpisodes(self.serieDir.files)
        
  def addToEpisodes(self, files):
    for aflevering in files:
      episode = Episode(aflevering)
      if episode.name != "":
        self.episodes.append(episode)
