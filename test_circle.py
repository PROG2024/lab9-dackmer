"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle
# TODO write 3 tests as described above


class TestCircle(unittest.TestCase):
    def test_add_area_typical(self):
        circle1 = Circle(3)
        circle2 = Circle(4)
        combined_circle = circle1.add_area(circle2)
        self.assertAlmostEqual(combined_circle.get_area(), 78.54, places=2)

    def test_add_area_one_circle_zero_radius(self):
        circle1 = Circle(3)
        circle2 = Circle(0)
        combined_circle = circle1.add_area(circle2)
        self.assertAlmostEqual(combined_circle.get_area(), 28.274, places=3)

    def test_circle_constructor_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)


if __name__ == '__main__':
    unittest.main()

