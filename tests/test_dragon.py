import unittest
from dragons import dragon_name

class test_dn(unittest.TestCase):
    def test_dragon_name(self):
        self.assertEqual(dragon_name('fish'), 'Fafnir')
