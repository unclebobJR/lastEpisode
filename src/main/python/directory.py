from os import listdir
import os.path
class Directory(object):
    
  def __init__(self, rootFolder):
    self.rootFolder = rootFolder
    self.name = os.path.basename(self.rootFolder)
    self.files = []
    self.subdirs = []
    self.readEntries()
    
  def readEntries(self):
    if os.path.exists(self.rootFolder):
      for f in listdir(self.rootFolder):
        if os.path.isdir(os.path.join(self.rootFolder, f)):
          self.subdirs.append(f)
        else:
          self.files.append(f)
    else:
      self.files = []