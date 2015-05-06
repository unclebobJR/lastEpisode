from os import listdir
import os.path
class Directory(object):
    
  def __init__(self, rootFolder):
    self.rootFolder = rootFolder
    self.name = os.path.basename(self.rootFolder)
    self.readEntries()
    
  def readEntries(self):
    if os.path.exists(self.rootFolder):
      self.entries = [ f for f in listdir(self.rootFolder) ]
    else:
      self.entries = []