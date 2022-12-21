class REED_MULLER:
    def __init__(self, str_int):
        self.v0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.v4 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        self.v3 = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
        self.v2 = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
        self.v1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        self.v4v3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
        self.v4v2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]
        self.v4v1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]
        self.v3v2 = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
        self.v3v1 = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1]
        self.v2v1 = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
        self.b = []
        self.bin_str = bin(str_int)[2:].zfill(11)
        self.a = [int(c, 2) for c in self.bin_str]
        for i in range(16):
            self.b.append((self.a[0] * self.v0[i]) ^ (self.a[1] * self.v4[i]) ^
                          (self.a[2] * self.v3[i]) ^ (self.a[3] * self.v2[i]) ^
                          (self.a[4] * self.v1[i]) ^ (self.a[5] * self.v4v3[i]) ^
                          (self.a[6] * self.v4v2[i]) ^ (self.a[7] * self.v4v1[i]) ^
                          (self.a[8] * self.v3v2[i]) ^ (self.a[9] * self.v3v1[i]) ^
                          (self.a[10] * self.v2v1[i]))

    def pass_code(self):
        quant = 0
        for i in range(4):
            quant = quant + 1 if ((self.b[4 * i] ^ self.b[4 * i + 1] ^ self.b[4 * i + 2] ^
                                   self.b[4 * i + 3]) == 0) else (quant - 1)
        if (quant == 0): print('There >= 2 mistakes. Recovering is impossible')
        self.a[10] = 0 if (quant > 0) else 1
        quant = 0
        for j in range(2):
            for i in range(2):
                quant = quant + 1 if ((self.b[8 * j + 2 * i] ^ self.b[8 * j + 2 * i + 1] ^
                                       self.b[8 * j + 2 * i + 4] ^ self.b[8 * j + 2 * i + 5]) == 0) else (quant - 1)
        if (quant == 0): print('There >= 2 mistakes. Recovering is impossible')
        self.a[9] = 0 if (quant > 0) else 1
        quant = 0
        for j in range(2):
            for i in range(2):
                quant = quant + 1 if ((self.b[8 * j + i] ^ self.b[8 * j + i + 2] ^
                                       self.b[8 * j + i + 4] ^ self.b[8 * j + i + 6]) == 0) else (quant - 1)
        if (quant == 0): print('There >= 2 mistakes. Recovering is impossible')
        self.a[8] = 0 if (quant > 0) else 1
        quant = 0
        for i in range(4):
            quant = quant + 1 if ((self.b[2 * i] ^ self.b[2 * i + 1] ^ self.b[2 * i + 8] ^
                                   self.b[2 * i + 9]) == 0) else (quant - 1)
        if (quant == 0): print('There >= 2 mistakes. Recovering is impossible')
        self.a[7] = 0 if (quant > 0) else 1
        quant = 0
        for j in range(2):
            for i in range(2):
                quant = quant + 1 if ((self.b[4 * j + i] ^ self.b[4 * j + i + 2] ^
                                       self.b[4 * j + i + 8] ^ self.b[4 * j + i + 10]) == 0) else (quant - 1)
        if (quant == 0): print('There >= 2 mistakes. Recovering is impossible')
        self.a[6] = 0 if (quant > 0) else 1
        quant = 0
        for i in range(4):
            quant = quant + 1 if ((self.b[i] ^ self.b[i + 4] ^ self.b[i + 8] ^
                                   self.b[i + 12]) == 0) else (quant - 1)
        if (quant == 0): print('There >= 2 mistakes. Recovering is impossible')
        self.a[5] = 0 if (quant > 0) else 1
        for i in range(16):
            self.b[i] = self.b[i] ^ ((self.a[5] * self.v4v3[i]) ^ (self.a[6] * self.v4v2[i]) ^
                                     (self.a[7] * self.v4v1[i]) ^ (self.a[8] * self.v3v2[i]) ^
                                     (self.a[9] * self.v3v1[i]) ^ (self.a[10] * self.v2v1[i]))
        quant = 0
        for i in range(0, 16, 2):
            quant = quant + 1 if ((self.b[i] ^ self.b[i + 1]) == 0) else (quant - 1)
        self.a[4] = 0 if (quant > 0) else 1
        quant = 0
        for j in range(4):
            for i in range(2):
                quant = quant + 1 if ((self.b[4 * j + i] ^ self.b[4 * j + i + 2]) == 0) else (quant - 1)
        self.a[3] = 0 if (quant > 0) else 1
        quant = 0
        for j in range(2):
            for i in range(2):
                quant = quant + 1 if ((self.b[8 * j + i] ^
                                       self.b[8 * j + i + 4]) == 0) else (quant - 1)
        self.a[2] = 0 if (quant > 0) else 1
        quant = 0
        for i in range(8):
            quant = quant + 1 if ((self.b[i] ^ self.b[i + 8]) == 0) else (quant - 1)
        self.a[1] = 0 if (quant > 0) else 1
        for i in range(16):
            self.b[i] = self.b[i] ^ ((self.a[1] * self.v4[i]) ^ (self.a[2] * self.v3[i]) ^
                                     (self.a[3] * self.v2[i]) ^ (self.a[4] * self.v1[i]))
        quant = 0
        for i in range(16):
            quant = quant + 1 if (self.b[i] == 0) else (quant - 1)
        self.a[0] = 0 if (quant > 0) else 1

    def __str__(self):
        return '{0} {1}'.format(self.a, self.b)


if __name__ == '__main__':
    with open('TextForTest.txt', 'r') as f:
        test = int(f.read())
    rm = REED_MULLER(test)
    print(rm)
    rm.a[0] ^= 1
    rm.pass_code()
    print(rm)
