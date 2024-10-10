from Header import index


class Registers:
    class GPRs:
        def __init__(self):
            self.gprs = [0 for _ in range(16)]
        
        def get(self, rs):
            if type(rs) == int:
                if rs <= 16:
                    return self.gprs[rs]
            else:
                rs = index.gpr.index(str(rs).lower())
                return self.get(rs)
        
        def set(self, rd, val):
            if type(rd) == int:
                if rd <= 16:
                    self.gprs[rd] = val
            else:
                rd = index.gpr.index(str(rd).lower())
                self.get(rd, val)

    class PC:
        def __init__(self):
            self.pc = 0

    class PSF:
        def __init__(self):
            self.psf = [0 for _ in range(16)]
        
        def get(self, flag = None):
            if flag == None:
                return self.psf
            else:
                if type(flag) == int:
                    mask = 0b1 << flag
                    int_psf = 0
                    for i in range(16):
                        int_psf += self.psf[i] << i
                    return (int_psf & mask) >> flag
                else:
                    flag = index.psf.index(flag)
                    return self.get(flag)
        
        def set(self, val ,flag = None):
            if flag == None:
                self.psf = val
            else:
                if type(flag) == int:
                    if self.get(flag) == val:
                        pass # 已經設置過
                    else:
                        if val == 0:    # Set Down
                            self.psf -= 0b1 << flag
                        else:           # Set Up
                            self.psf += 0b1 << flag
                else:
                    flag = index.psf.index(flag)
                    return self.get(flag)