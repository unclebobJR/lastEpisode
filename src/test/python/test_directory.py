import unittest
from directory import Directory
import os
import shutil

class TestDirectory(unittest.TestCase):
  
  def setUp(self):
    self.testRootDir = "/tmp/TVSHOWS"
    self.serie = "The_Flash"
    self.serieDir = os.path.join(self.testRootDir, self.serie)
    self.season = "Season01"
    self.episode = "The_Flash_S01E01.mkv"
    self.seasonPath = os.path.join(self.serieDir, self.season)
    self.episodePath = os.path.join(self.seasonPath, self.episode)
    if not os.path.exists(self.seasonPath):
      os.makedirs(self.seasonPath)
    open(self.episodePath, 'a').close()
      
  def test_givenEmptyDir_expectNoEntries(self):
    directory = Directory("")
    self.assertTrue(directory.entries == [])
    
  def test_givenDir_expectEntries(self):
    directory = Directory(self.serieDir)
    self.assertTrue(directory.entries == [self.season])
    
  def test_givenDir_expectName(self):
    directory = Directory(self.serieDir)
    self.assertTrue(directory.name == self.serie)

  def tearDown(self):
    shutil.rmtree(self.testRootDir)
    
    
