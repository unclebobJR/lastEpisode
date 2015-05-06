import unittest
from episode import Episode

class TestEpisode(unittest.TestCase):
  def test_emptyEpisode_expectEmpty(self):
    episode = Episode("")
    self.assertTrue(episode.name == "")
    
  def test_HappyEpisode_expectBaseName(self):
    episode = Episode("The Flash S01E01.mkv")
    self.assertTrue(episode.name == "The Flash S01E01")
    
  def test_WrongExtension_expectEmpty(self):
    self.assertEpisode("The Flash S01E01.mvk", -1, -1)
    
  def test_HappyEpisode_expectSeasonEpisode(self):
    self.assertEpisode("The Flash S01E01.mkv", 1, 1)
    
  def test_EpisodeSmalcaps_expectSeasonEpisode(self):
    self.assertEpisode("The Flash_s01e01.mkv", 1, 1)
                      
  def test_EpisodeNoZeroes_expectSeasonEpisode(self):
    self.assertEpisode("The Flash_s1e1.mkv", 1, 1)
  
  def test_HappyEpisodeTrueName_expectSeason1Episode4(self):
    self.assertEpisode("Forbrydelsen.(The Killing).S01E04.Day 4.mkv", 1, 4)
    
  def assertEpisode(self, name, season, episodeNr):
    episode = Episode(name)
    self.assertTrue(episode.seasonNr == season)
    self.assertTrue(episode.episodeNr == episodeNr)
