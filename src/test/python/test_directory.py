import unittest
from directory import Directory

class TestDirectory(unittest.TestCase):
  def test_givenEmptyDir_expectNoEntries(self):
    directory = Directory("")
    self.assertTrue(directory.entries == [])