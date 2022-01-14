import GameOfLife
import unittest
import io


class TestProject(unittest.TestCase):
    def test_constructor(self):
        gol = GameOfLife
        self.assertEqual(gol.rows, 0)
        self.assertEqual(gol.cols, 0)
        self.assertEqual(gol.to_string(), "")

    def test_grid_load_1(self):
        gol = GameOfLife
        gol.load_file("blinker.gol")
        self.assertEqual(gol.rows, 5)
        self.assertEqual(gol.cols, 5)

    def test_grid_load_2(self):
        gol = GameOfLife
        gol.load_file("glider.gol")
        self.assertEqual(gol.rows, 9)
        self.assertEqual(gol.cols, 9)

    def test_grid_load_3(self):
        gol = GameOfLife
        gol.load_file("toad.gol")
        self.assertEqual(gol.rows, 6)
        self.assertEqual(gol.cols, 6)

    def test_grid_load_4(self):
        gol = GameOfLife
        gol.load_file("tub.gol")
        self.assertEqual(gol.rows, 5)
        self.assertEqual(gol.cols, 5)

    def test_grid_save_1(self):
        gol = GameOfLife
        gol.load_file("beacon.gol")
        gol.save_file("test.gol")
        file = io.open("test.gol", "rb", buffering=0)
        actual = file.read()
        file.close()
        expected = b"6 6 0 0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 0"
        self.assertEqual(actual, expected)

    def test_grid_save_2(self):
        gol = GameOfLife
        gol.load_file("blinker.gol")
        gol.save_file("test.gol")
        file = io.open("test.gol", "rb", buffering=0)
        actual = file.readline()
        file.close()
        expected = b"5 5 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0\n"
        self.assertEqual(actual, expected)

    def test_grid_save_3(self):
        gol = GameOfLife
        gol.load_file("glider.gol")
        gol.save_file("test.gol")
        file = io.open("test.gol", "rb", buffering=0)
        actual = file.readline()
        file.close()
        expected = b"9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 " \
                   b"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n"
        self.assertEqual(actual, expected)

    def test_grid_save_4(self):
        gol = GameOfLife
        gol.load_file("toad.gol")
        gol.save_file("test.gol")
        file = io.open("test.gol", "rb", buffering=0)
        actual = file.read()
        file.close()
        expected = b"6 6 0 0 0 0 0 0 0 1 1 1 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n"
        self.assertEqual(actual, expected)

    def test_grid_save_5(self):
        gol = GameOfLife
        gol.load_file("tub.gol")
        gol.save_file("test.gol")
        file = io.open("test.gol", "rb", buffering=0)
        actual = file.read()
        file.close()
        expected = b"5 5 0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 0 0 0 0 0\n"
        self.assertEqual(actual, expected)

    def test_number_of_neighbors(self):
        gol = GameOfLife
        gol.load_file("blinker.gol")
        self.assertEqual(0, gol.get_neighbors(0,0))
        self.assertEqual(1, gol.get_neighbors(1,2))
        self.assertEqual(2, gol.get_neighbors(2,2))
        self.assertEqual(1, gol.get_neighbors(3,2))
        self.assertEqual(0, gol.get_neighbors(0,4))
        self.assertEqual(0, gol.get_neighbors(4,0))
        self.assertEqual(0, gol.get_neighbors(4,4))
        self.assertEqual(1, gol.get_neighbors(0,2))
        self.assertEqual(0, gol.get_neighbors(2,0))
        self.assertEqual(0, gol.get_neighbors(2,4))
        self.assertEqual(1, gol.get_neighbors(4,2))


unittest.main()
