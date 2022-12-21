from Hamming_code import HAMMING_CODE
from Reed_Muller_Code import REED_MULLER
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        with open('TextForTest.txt', 'r') as f:
            self.test = int(f.read())
        self.h = HAMMING_CODE()
        self.rm = REED_MULLER(self.test)

    def test_HAMMING_CODE(self):
        dolzno_bit = '0000000000000000000000000000000000000000000000000000000000001110101001'
        self.h.get_code(self.test)
        self.h.hc = self.h.hc[:5] + '1' + self.h.hc[6:]
        self.h.correct_code()
        polychilos = self.h.hc
        self.assertEqual(dolzno_bit, polychilos)

    def test_REED_MULLER(self):
        dolzno_bit = '[0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1] [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]'
        self.rm.a[0] ^= 1
        self.rm.pass_code()
        polychilos = self.rm.__str__()
        self.assertEqual(dolzno_bit, polychilos)


if __name__ == '__main__':
    unittest.main()
