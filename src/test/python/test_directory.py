import unittest
import os
import shutil
from lastepisode import Directory

class TestDirectory(unittest.TestCase):
  
  def setUp(self):
    self.testRootDir = "/tmp/TVSHOWS"
    self.serie = "The_Flash"
    self.serieDir = os.path.join(self.testRootDir, self.serie)
    self.season = "Season01"
    self.episode = "The_Flash_S01E01.mkv"
    self.episode2 = "The_Flash_S01E02.mkv"
    self.seasonPath = os.path.join(self.serieDir, self.season)
    self.episodePath = os.path.join(self.seasonPath, self.episode)
    if not os.path.exists(self.seasonPath):
      os.makedirs(self.seasonPath)
    open(self.episodePath, 'a').close()
    open(os.path.join(self.serieDir, self.episode2), 'a').close()
      
  def test_givenEmptyDir_expectNoEntries(self):
    directory = Directory("")
    self.assertTrue(directory.files == [])
    
  def test_givenDir_expectEntries(self):
    directory = Directory(self.serieDir)
    self.assertTrue(directory.files == [self.episode2])
    
  def test_givenDir_expectName(self):
    directory = Directory(self.serieDir)
    self.assertTrue(directory.name == self.serie)
    
  def test_givenDir_expectDirEntries(self):
    directory = Directory(self.serieDir)
    self.assertTrue(directory.subdirs == [self.season])

  def tearDown(self):
    shutil.rmtree(self.testRootDir)
