import unittest
from src.bfs.change_word import change_word


class TestBfs(unittest.TestCase):
    def test_change_word(self):
        self.assertEqual(change_word("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]),4)
        self.assertEqual(change_word("hit","cog",["hot", "dot", "dog", "lot", "log"]),0)
