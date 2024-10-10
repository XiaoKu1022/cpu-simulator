class Logic:
    def NOT(a):
        if a == 1:
            return 0
        else:
            return 1

    def AND(a,b):
        if a == b and a != 0:
            return 1
        else:
            return 0

    def NAND(a,b):
        return Logic.NOT(Logic.AND(a,b))

    def OR(a,b):
        if a != 0 or b != 0:
            return 1
        else:
            return 0

    def NOR(a,b):
        return Logic.NOT(Logic.OR(a,b))

    def XOR(a,b):
        if a != b:
            return 1
        else:
            return 0

    def XNOR(a,b):
        return Logic.NOT(Logic.XOR(a,b))

class ALU:
    def S_2bit(a):
        c,s = a
        return s
    def C_2bit(a):
        c,s = a
        return c




    def HA(a,b):
        s = Logic.XOR(a,b)
        c = Logic.AND(a,b)
        return c,s


    def FA(a,b,c_in):
        s1 = ALU.S_2bit(ALU.HA(a,b))
        s2 = ALU.S_2bit(ALU.HA(s1,c_in))
        c1 = ALU.C_2bit(ALU.HA(a,b))
        c2 = ALU.C_2bit(ALU.HA(s1,c_in))
        c3 = Logic.OR(c1,c2)
        return c3,s2



    def CLA_16bit(cin, a, b):
        c0 = cin
        [a15,a14,a13,a12,a11,a10,a9,a8,a7,a6,a5,a4,a3,a2,a1,a0,b15,b14,b13,b12,b11,b10,b9,b8,b7,b6,b5,b4,b3,b2,b1,b0]
        fa0 = ALU.FA(a0,b0,c0)
        s0 = ALU.S_2bit(fa0)  
        c1 = ALU.C_2bit(fa0)  
        
        fa1 = ALU.FA(a1,b1,c1)
        s1 = ALU.S_2bit(fa1)  
        c2 = ALU.C_2bit(fa1)  

        fa2 = ALU.FA(a2,b2,c2)
        s2 = ALU.S_2bit(fa2)
        c3 = ALU.C_2bit(fa2)

        fa3 = ALU.FA(a3,b3,c3)
        s3 = ALU.S_2bit(fa3)
        c4 = ALU.C_2bit(fa3)

        fa4 = ALU.FA(a4,b4,c4)
        s4 = ALU.S_2bit(fa4)
        c5 = ALU.C_2bit(fa4)

        fa5 = ALU.FA(a5,b5,c5)
        s5 = ALU.S_2bit(fa5)
        c6 = ALU.C_2bit(fa5)

        fa6 = ALU.FA(a6,b6,c6)
        s6 = ALU.S_2bit(fa6)
        c7 = ALU.C_2bit(fa6)

        fa7 = ALU.FA(a7,b7,c7)
        s7 = ALU.S_2bit(fa7)
        c8 = ALU.C_2bit(fa7)

        fa8 = ALU.FA(a8,b8,c8)
        s8 = ALU.S_2bit(fa8)
        c9 = ALU.C_2bit(fa8)

        fa9 = ALU.FA(a9,b9,c9)
        s9 = ALU.S_2bit(fa9)
        c10 = ALU.C_2bit(fa9)

        fa10 = ALU.FA(a10,b10,c10)
        s10 = ALU.S_2bit(fa10)
        c11 = ALU.C_2bit(fa10)

        fa11 = ALU.FA(a11,b11,c11)
        s11 = ALU.S_2bit(fa11)
        c12 = ALU.C_2bit(fa11)

        fa12 = ALU.FA(a12,b12,c12)
        s12 = ALU.S_2bit(fa12)
        c13 = ALU.C_2bit(fa12)

        fa13 = ALU.FA(a13,b13,c13)
        s13 = ALU.S_2bit(fa13)
        c14 = ALU.C_2bit(fa13)

        fa14 = ALU.FA(a14,b14,c14)
        s14 = ALU.S_2bit(fa14)
        c15 = ALU.C_2bit(fa14)

        fa15 = ALU.FA(a15,b15,c15)
        s15 = ALU.S_2bit(fa15)
        c16 = ALU.C_2bit(fa15)

        return c15,s15,s14,s13,s12,s11,s10,s9,s8,s7,s6,s5,s4,s3,s2,s1,s0