from directory import Directory
from serie import Serie
import sys
import os
class LastEpisode(object):
    
  def __init__(self, rootDir):
    self.rootDir = Directory(rootDir)
    self.series = {}

  def gatherSeries(self):
    for serie in self.rootDir.subdirs:
      self.series[serie] = Serie(self.rootDir.join(serie))
      
      
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
      lastEpisode = last.series[serie].getLastEpisode()
      if lastEpisode == -1:
        print serie + " : No episodes found"
      else:
        print serie + " : " + str(lastEpisode)
  else:
    print "Argument must be root folder of TV Shows"
    exit(1)
  