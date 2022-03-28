import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")
    def test_lataaminen_kasvattaa_oikein(self):
        self.maksukortti.lataa_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.12")
    def test_ottaminen_vahentaa_oikein(self):
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.08")
    def test_saldo_ottaminen_ei_neg(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    def test_true_kun_rahat_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2), True)
    def test_false_kun_raha_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(11), False)

