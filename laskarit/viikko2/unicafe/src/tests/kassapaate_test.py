import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(400)
    def test_init_oikein(self):
        self.assertEqual(self.kassa.edulliset,0)
        self.assertEqual(self.kassa.maukkaat,0)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
    def test_edullinen_kat(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250),10)
        self.assertEqual(str(self.kassa.kassassa_rahaa),"100240")
        self.assertEqual(self.kassa.edulliset,1)
    def test_maukast_kat(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(410),10)
        self.assertEqual(self.kassa.kassassa_rahaa,100400)
        self.assertEqual(self.kassa.maukkaat,1)
    def test_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(200),200)
        self.assertEqual(self.kassa.maukkaat,0)
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200),200)
        self.assertEqual(self.kassa.edulliset,0)
    def test_kortti_maukkasti(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti),True)
        self.assertEqual(self.kassa.maukkaat,1)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti),False)
        self.assertEqual(self.kassa.maukkaat,1)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
    def test_kortti_edullisest(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti),True)
        self.assertEqual(self.kassa.edulliset,1)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti),False)
        self.assertEqual(self.kassa.edulliset,1)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
    def test_lataa_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.kortti,200)
        self.assertEqual(self.kassa.kassassa_rahaa,100200)
        self.assertEqual(str(self.kortti),"saldo: 6.0")
