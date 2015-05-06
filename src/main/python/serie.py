from directory import Directory
import os
from episode import Episode
class Serie(object):
  def __init__(self, serieDir):
    self.serieDir = Directory(serieDir)
    self.episodes = []
    
  def gatherEpisodes(self):
    for season in self.serieDir.subdirs:
      seasonDir = Directory(os.path.join(self.serieDir.rootFolder, season))
      self._addToEpisodes(seasonDir.files)
    self._addToEpisodes(self.serieDir.files)
  
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
