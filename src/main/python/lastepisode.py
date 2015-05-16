#!/usr/bin/python

import sys
from os import listdir
import os.path
import re

class LastEpisode(object):
    
  def __init__(self, rootDir):
    self.rootDir = Directory(rootDir)
    self.series = {}

  def gatherSeries(self):
    for serie in self.rootDir.subdirs:
      self.series[serie] = Serie(self.rootDir.join(serie))

class Episode(object):

  MOVIE_EXTENSIONS = ['.mkv', '.avi', '.divx', '.flv', '.mov', '.wmv', '.asf', '.mpg', '.mpeg', '.mp4', '.m4v']
  def __init__(self, fileName):
    self.name = ""
    self.episodeNr = -1
    self.seasonNr = -1
    (base, ext) = os.path.splitext(fileName)
    if ext.lower() in Episode.MOVIE_EXTENSIONS:
      self.name = base
      self.parseNameforSeasonEpisode()
  
  def parseNameforSeasonEpisode(self):
    result = re.search(r"[sS](\d\d?)[eE](\d\d?)", self.name)
    if result != None:
      self.seasonNr = int(result.group(1))
      self.episodeNr = int(result.group(2))
      
  def __str__(self):
    return self.name + "=" + str(self.seasonNr) + ":" + str(self.episodeNr)

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
    return (lastEpisode, season)
  
  def _addToEpisodes(self, files):
    for aflevering in files:
      episode = Episode(aflevering)
      if episode.name != "":
        self.episodes.append(episode)

class Directory(object):
    
  def __init__(self, rootFolder):
    self.rootFolder = rootFolder
    self.name = os.path.basename(self.rootFolder)
    self.files = []
    self.subdirs = []
    self._readEntries()
    
  def _readEntries(self):
    if os.path.exists(self.rootFolder):
      for f in listdir(self.rootFolder):
        if os.path.isdir(os.path.join(self.rootFolder, f)):
          self.subdirs.append(f)
        else:
          self.files.append(f)
    else:
      self.files = []
      
  def join(self, name):
    return os.path.join(self.rootFolder, name)
      
      
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Argument with root dir TVSHows is mandatory. None given"
    exit(1)
  rootDir = sys.argv[1]
  if os.path.exists(rootDir):
    last = LastEpisode(rootDir)
    last.gatherSeries()
    for serie in last.series.keys():
      last.series[serie].gatherEpisodes()
      (lastEpisode, lastSeason) = last.series[serie].getLastEpisode()
      if lastEpisode == -1:
        print serie + " : No episodes found"
      else:
        print serie + ": last episode " + str(lastEpisode) + " of season " + str(lastSeason)
  else:
    print "Argument must be root folder of TV Shows"
    exit(1)
  