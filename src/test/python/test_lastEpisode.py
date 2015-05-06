import unittest
from stub_directory import StubDirectory
from lastepisode import LastEpisode

class TestLastEpisodeContextOneSerie(unittest.TestCase):
  
  def setUp(self):
    self.serie = "The_Flash"
    self.rootDir = "TVSHOWS"
    self.stubDirSeries = StubDirectory(self.rootDir)
    self.stubDirSeries.subdirs = [self.serie]
    self.stubDirFlash = StubDirectory(self.serie)
    self.stubDirFlash.subdirs = ["Season01"]
    self.stubDirFlash.files = ["The_Flash_S01E01.mkv", "The_Flash_S01E02.mkv", "The_Flash_S01E03.mkv"]

  def test_happyFlowLastEpisode_expect3(self):
    lastEpisode = LastEpisode(self.rootDir)
    lastEpisode.rootDir = self.stubDirSeries
    lastEpisode.gatherSeries()
    lastEpisode.series[self.serie].serieDir = self.stubDirFlash
    lastEpisode.series[self.serie].gatherEpisodes()
    self.assertTrue(lastEpisode.series[self.serie].getLastEpisode() == (3, 1))
    
