from directory import Directory
class StubDirectory(Directory):
    
  def __init__(self, rootFolder):
    self.rootFolder = rootFolder
    self.name = ""
    self.files = []
    self.subdirs = []
