import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.neg_arvot = Varasto(-10, -10)
        self.ylijaama = Varasto(10, 30)
    
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 1000)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_lisayksessa_vain_positiviisia_arvoja(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_lisayksessa_ei_ylijaama(self):
        self.varasto.lisaa_varastoon(500)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_ottaminen_vain_positiivisilla_arvoilla(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu_maara, 0)
    
    def test_varaston_tyhjentaminen_palauttaa_oikean_maaran_saldon(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 8)
        self.assertAlmostEqual(self.varasto.saldo, 0)
       
    def test_konstruktori_hyvaksyy_vain_positiivisen_tilavuuden(self):
        self.assertAlmostEqual(self.neg_arvot.tilavuus, 0)
        
    def test_konstruktori_hyvaksyy_vain_positiivisen_alku_saldon(self):
        self.assertAlmostEqual(self.neg_arvot.saldo, 0)
        
    def test_konstruktori_laskee_ylijaamatilanteen_oikein(self):
        self.assertAlmostEqual(self.ylijaama.saldo, 10)

    def test_tulostus_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")