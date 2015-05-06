import unittest
import os
from serie import Serie

class TestSerie(unittest.TestCase):
  
  def setUp(self):
    self.testRootDir = "/tmp/TVSHOWS"
    self.serie = "The_Flash"
    self.season = "Season01"
    self.episode = "The_Flash_S01E01"
    self.seasonPath = os.path.join(self.testRootDir, self.serie, self.season)
    self.episodePath = os.path.join(self.seasonPath, self.episode + ".mkv")
    if not os.path.exists(self.seasonPath):
      os.makedirs(self.seasonPath)
    open(self.episodePath, 'a').close()
    
  def test_givenNoSerie_expectNoName(self):
    serie = Serie("")
    self.assertTrue(serie.name == "")
    
  def test_givenSerieDir_expectName(self):
    serie = Serie(os.path.join(self.testRootDir, self.serie))
    self.assertTrue(serie.name == self.serie)
    
  def test_givenSerieDir_expectSeason(self):
    serie = Serie(os.path.join(self.testRootDir, self.serie))
    self.assertTrue(serie.seasons == [self.season])
    
  def test_givenSerieDir_expectEpisodes(self):
    serie = Serie(os.path.join(self.testRootDir, self.serie))
    serie.gatherEpisodes()
    self.assertTrue(str(serie.episodes[0]) == self.episode + "=1:1")
