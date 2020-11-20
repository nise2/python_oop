import unittest

from .Rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 3)

    def test_get_perimeter(self):
        self.assertEqual(self.rectangle.perimeter(), 16)

    def test_get_surface(self):
        self.assertEqual(self.rectangle.surface(), 15)


if __name__ == 'main':
    unittest.main()
