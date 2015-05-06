import unittest
import os
from serie import Serie

class TestSerie(unittest.TestCase):
  
  def setUp(self):
    self.testRootDir = "/tmp/TVSHOWS"
    self.serie = "The_Flash"
    self.season = "Season01"
    self.episode = "The_Flash_S01E01.mkv"
    self.seasonPath = os.path.join(self.testRootDir, self.serie, self.season)
    self.episodePath = os.path.join(self.seasonPath, self.episode)
    if not os.path.exists(self.seasonPath):
      os.makedirs(self.seasonPath)
    open(self.episodePath, 'a').close()
    
  def test_givenNoSerie_expectNoName(self):
    serie = Serie("")
    self.assertTrue(serie.name == "")
    
  def test_givenSerieDir_expectName(self):
    serie = Serie(os.path.join(self.testRootDir, self.serie))
    self.assertTrue(serie.name == self.serie)