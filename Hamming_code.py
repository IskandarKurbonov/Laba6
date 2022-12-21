class HAMMING_CODE:
    def pass_code(self):
        self.h = [0, 0, 0, 0, 0, 0]
        for i in range(39):
            if i & 1:
                self.h[0] ^= int(self.hc[i - 1], 2)
            if (i >> 1) & 1:
                self.h[1] ^= int(self.hc[i - 1], 2)
            if (i >> 2) & 1:
                self.h[2] ^= int(self.hc[i - 1], 2)
            if (i >> 3) & 1:
                self.h[3] ^= int(self.hc[i - 1], 2)
            if (i >> 4) & 1:
                self.h[4] ^= int(self.hc[i - 1], 2)
            if (i >> 5) & 1:
                self.h[5] ^= int(self.hc[i - 1], 2)

    def get_code(self, str_int):
        bin_str = bin(str_int)[2:].zfill(64)
        self.hc = '0' + '0' + bin_str[0] + '0' + bin_str[1:4] + '0' + bin_str[4:11] + '0' + \
                  bin_str[11:26] + '0' + bin_str[26:64]
        self.pass_code()
        self.hc = bin(self.h[0])[2:] + bin(self.h[1])[2:] + bin_str[0] + bin(self.h[2])[2:] + \
                  bin_str[1:4] + bin(self.h[3])[2:] + bin_str[4:11] + bin(self.h[4])[2:] + \
                  bin_str[11:26] + bin(self.h[5])[2:] + bin_str[26:64]

    def correct_code(self):
        self.pass_code()
        index = 0
        for i in range(6): index += self.h[i] << i
        if index == 0:
            print('no error')
            return
        print('error in {0} element = {1}'.format(index, self.hc[index - 1]))
        if self.hc[index - 1] == '1':
            self.hc = self.hc[:index - 1] + '0' + self.hc[index:]
        else:
            self.hc = self.hc[:index - 1] + '1' + self.hc[index:]


if __name__ == '__main__':
    with open('TextForTest.txt', 'r') as f:
        test = int(f.read())
    h = HAMMING_CODE()
    h.get_code(test)
    print(h.hc)
    h.hc = h.hc[:5]+'1'+h.hc[6:]
    h.correct_code()
    print(h.hc)
