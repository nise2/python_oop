import unittest

from .Parallelepiped import Parallelepiped


class TestParallelepiped(unittest.TestCase):
    def setUp(self):
        self.parallepiped = Parallelepiped(5, 3, 2)

    def test_volume(self):
        self.assertEqual(self.parallepiped.volume(), 30)


if __name__ == '__main__':
    unittest.main()
