from directory import Directory
import os
from episode import Episode
class Serie(object):
  def __init__(self, serieDir):
    self.serieDir = Directory(serieDir)
    self.episodes = []
    
  def gatherEpisodes(self, rootFolder=None, mainDir=None):
    if rootFolder == None and mainDir == None:
      rootFolder = self.serieDir.rootFolder
      mainDir = self.serieDir.subdirs
      self._addToEpisodes(self.serieDir.files)
    for subDir in mainDir:
      subsubDir = Directory(os.path.join(rootFolder, subDir))
      self._addToEpisodes(subsubDir.files)
      if len(subsubDir.subdirs) > 0:
        self.gatherEpisodes(subsubDir.rootFolder, subsubDir.subdirs)
  
  def getName(self):
    return self.serieDir.name
  
  def getLastEpisode(self):
    lastEpisodePerSeason = {}
    lastEpisode = -1
    for episode in self.episodes:
      if lastEpisodePerSeason.has_key(episode.seasonNr):
        if episode.episodeNr > lastEpisodePerSeason[episode.seasonNr]:
          lastEpisodePerSeason[episode.seasonNr] = episode.episodeNr        
      else:
          lastEpisodePerSeason[episode.seasonNr] = episode.episodeNr
    lastSeason = -1
    for season in lastEpisodePerSeason.keys():
      if season > lastSeason:
        lastSeason = season
        lastEpisode = lastEpisodePerSeason[season]
    return lastEpisode
  
  def _addToEpisodes(self, files):
    for aflevering in files:
      episode = Episode(aflevering)
      if episode.name != "":
        self.episodes.append(episode)
