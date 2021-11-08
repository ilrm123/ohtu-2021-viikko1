import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-1, -1)
        self.varasto3 = Varasto(10, 11)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

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

    def test_lisataan_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(15)

        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_otetaan_enemman_kuin_on(self):
        self.varasto.lisaa_varastoon(3)

        self.varasto.ota_varastosta(4)

        self.assertEqual(self.varasto.saldo, 0.0)

    def test_otetaan_negatiivinen_maara(self):
        ota = self.varasto.ota_varastosta(-1)

        self.assertEqual(ota, 0.0)

    def test_lisataan_negatiivinen_maara(self):
        lisaa = self.varasto.lisaa_varastoon(-1)

        self.assertEqual(lisaa, None)

    def test_virheellinen_tilavuus(self):
        self.assertEqual(self.varasto2.tilavuus, 0.0)

    def test_virheellinen_saldo(self):
        self.assertEqual(self.varasto2.saldo, 0.0)

    def test_saldo_yli(self):
        self.assertEqual(self.varasto3.saldo, 10)

    def test_oikea_tulostus(self):
        self.assertEqual(str(self.varasto), "saldo = 50, vielä tilaa 10")

