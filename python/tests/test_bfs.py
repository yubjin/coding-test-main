import unittest
from src.bfs.change_word import change_word
from src.bfs.shortest import shortest


class TestBfs(unittest.TestCase):
    def test_change_word(self):
        self.assertEqual(change_word("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]),4)
        self.assertEqual(change_word("hit","cog",["hot", "dot", "dog", "lot", "log"]),0)
    def test_short(self):
        self.assertEqual(shortest(6,[[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]]),3)