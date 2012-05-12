from twisted.trial import unittest

from x256 import x256


class Testx256(unittest.TestCase):
    """
    Test class for x256 module.
    """

    def setUp(self):
        self.rgb = [220, 40, 150]
        self.xcolor = 162
        self.hex = 'DC2896'
        self.aprox_hex = 'D7087'
        self.aprox_rgb = [215, 0, 135]

    def test_from_rgb(self):
        color = x256.from_rgb(self.rgb)
        self.assertEqual(self.xcolor, color)
        color = x256.from_rgb(self.rgb[0], self.rgb[1], self.rgb[2])
        self.assertEqual(self.xcolor, color)

    def test_from_hex(self):
        color = x256.from_hex(self.hex)
        self.assertEqual(self.xcolor, color)

    def test_to_rgb(self):
        color = x256.to_rgb(self.xcolor)
        self.assertEqual(self.aprox_rgb, color)

    def test_to_hex(self):
        color = x256.to_hex(self.xcolor)
        self.assertEqual(self.aprox_hex, color)
