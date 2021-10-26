from django.test import SimpleTestCase

from example.core.tools import double, treble


class DoubleTests(SimpleTestCase):
    def test_zero(self):
        result = double(0)
        self.assertEqual(result, 0)

    def test_one(self):
        result = double(1)
        self.assertEqual(result, 2)


class TrebleTests(SimpleTestCase):
    def test_zero(self):
        result = treble(0)
        self.assertEqual(result, 0)

    def test_one(self):
        result = treble(1)
        self.assertEqual(result, 3)
