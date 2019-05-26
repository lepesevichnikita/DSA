import unittest

from sympy import isprime

from src.schnorr_scheme import SchnorrSchemeKeygen


class SchnorrSchemeKeygenDefaultTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.schnorrSchemeKeygen = SchnorrSchemeKeygen()
        cls.schnorrSchemeKeygen.generate_new_keys()
        cls.public_key = cls.schnorrSchemeKeygen.public_key
        cls.privateKey = cls.schnorrSchemeKeygen.private_key

    def test_has_p(self):
        self.assertTrue(self.public_key.has_p, "Hasn't P")

    def test_has_q(self):
        self.assertTrue(self.public_key.has_q, "Hasn't Q")

    def test_has_g(self):
        self.assertTrue(self.public_key.has_g, "Hasn't G")

    def test_has_y(self):
        self.assertTrue(self.public_key.has_y, "Hasn't Y")

    def test_p_is_prime(self):
        self.assertTrue(isprime(self.public_key.p), "P isn't prime number")

    def test_q_is_divider_of_p_minus_one(self):
        p, q, _, _ = self.public_key.to_list()
        self.assertTrue((p - 1) % q == 0, "Q isn't divider of P minus One")

    def test_q_is_order_of_g_modulo_p(self):
        p, q, g, _ = self.public_key.to_list()
        self.assertTrue(pow(g, q, p) == 1, "Q isn't order pf G modulo P ")

    def test_x_is_less_than_q(self):
        q = self.public_key.q
        x = self.privateKey
        self.assertLess(x, q, "X isn't less than Q")


if __name__ == '__main__':
    unittest.main()
