import os
import re
class Episode(object):

  MOVIE_EXTENSIONS = ['.mkv', '.avi', '.divx']
  def __init__(self, fileName):
    self.name = ""
    self.episodeNr = -1
    self.seasonNr = -1
    (base, ext) = os.path.splitext(fileName)
    if ext in Episode.MOVIE_EXTENSIONS:
      self.name = base
      self.parseNameforSeasonEpisode()
  
  def parseNameforSeasonEpisode(self):
    result = re.search(r"[sS](\d\d?)[eE](\d\d?)", self.name)
    if result != None:
      self.seasonNr = int(result.group(1))
      self.episodeNr = int(result.group(2))
