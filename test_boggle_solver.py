import unittest
from boggle_solver import Boggle

class TestBoggleSolver(unittest.TestCase):
    """
    test empty dictionary
    """

    def test_dictionary_empty(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    """
    test empty grid
    """

    def test_grid_empty(self):
        grid = []
        dictionary = ["ABC"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    """
    test 1x1 grid that can't form a 3 letter word
    """

    def test_one_by_one(self):
        grid = [["A"]]
        dictionary = ["A", "AA", "AAA"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    """
    simple 2x2 grid
    """

    def test_two_by_two(self):
        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = ["A", "B", "AC", "ACA", "ACB", "DE"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), ["ACB"])

    """
    test 3x3 normal TestCase
    """

    def test_three_by_three(self):
        grid = [["A", "B", "C"],
                ["D", "H", "I"],
                ["E", "F", "G"]]
        dictionary = ["ABC", "ABDHI", "BAD"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), ["ABC", "ABDHI", "BAD"])

    """
    test 4x4 normal case
    """

    def test_four_by_four(self):
        grid = [["B", "E", "E", "R"],
                ["D", "R", "E", "D"],
                ["V", "E", "R", "Y"],
                ["A", "B", "C", "D"]]
        dictionary = ["BEE", "VERB", "VERY"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), ["BEE", "VERB", "VERY"])

    """
    test diagonal movement allowed
    """

    def test_diagonal(self):
        grid = [["A", "X", "X"],
                ["X", "B", "X"],
                ["X", "X", "C"]]
        dictionary = ["ABC"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), ["ABC"])

    """
    test multi-letter tile (IE)
    """

    def test_multi_letter_tile(self):
        grid = [["IE", "A"],
                ["B", "C"]]
        dictionary = ["IEAB"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), ["IEAB"])

    """
    test case insensitivity
    """

    def test_case_insensitive(self):
        grid = [["a", "b", "c"],
                ["d", "e", "f"],
                ["g", "h", "i"]]
        dictionary = ["ABC"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), ["ABC"])

    """
    test no duplicates
    """

    def test_no_duplicates(self):
        grid = [["A", "A"],
                ["A", "A"]]
        dictionary = ["AAA"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), ["AAA"])