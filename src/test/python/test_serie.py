import unittest
from serie import Serie
from stub_directory import StubDirectory

class TestSerieContextOneSeason(unittest.TestCase):
  
  def setUp(self):
    self.serie = "The_Flash"
    self.season = "Season01"
    self.episode1 = "The_Flash_S01E01"
    self.episode2 = "The_Flash_S01E02"
    self.episode4 = "The_Flash_S01E04"
    self.stubDir = StubDirectory(self.serie)
    self.stubDir.name = self.serie
    self.stubDir.subdirs = [self.season]
    self.stubDir.files = [self.episode1 + ".mkv", self.episode2 + ".mkv", self.episode4 + ".mkv"]
    
  def test_givenNoSerie_expectNoName(self):
    serie = Serie("")
    self.assertTrue(serie.getName() == "")
    
  def test_givenSerieDir_expectName(self):
    serie = Serie("")
    serie.serieDir = self.stubDir
    self.assertTrue(serie.getName() == self.serie)
    
  def test_givenSerieDir_expectEpisodes(self):
    serie = Serie("")
    serie.serieDir = self.stubDir
    serie.gatherEpisodes()
    self.assertTrue(str(serie.episodes[0]) == self.episode1 + "=1:1")
    
  def test_lastEpisode(self):
    serie = Serie("")
    serie.serieDir = self.stubDir
    serie.gatherEpisodes()
    self.assertTrue(serie.getLastEpisode() == 4)
    

class TestSerieContextMultipleSeasons(unittest.TestCase):
  
  def setUp(self):
    self.serie = "The_Flash"
    self.season1 = "Season01"
    self.season2 = "Season02"
    self.season3 = "Season03"    
    self.episode11 = "The_Flash_S01E01"
    self.episode12 = "The_Flash_S01E04"
    self.episode21 = "The_Flash_S02E01"
    self.episode23 = "The_Flash_S02E03"
    self.episode31 = "The_Flash_S03E02"
    self.stubDir = StubDirectory(self.serie)
    self.stubDir.name = self.serie
    self.stubDir.subdirs = [self.season1, self.season2]
    self.stubDir.files = [self.episode11 + ".mkv", self.episode12 + ".mkv", \
                          self.episode21 + ".mkv", self.episode23 + ".mkv", self.episode31 + ".mkv"]
    
  def test_lastEpisode(self):
    serie = Serie("")
    serie.serieDir = self.stubDir
    serie.gatherEpisodes()
    self.assertTrue(serie.getLastEpisode() == 2)
    