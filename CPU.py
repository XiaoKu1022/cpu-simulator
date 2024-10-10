from Register import Registers


program_mem = [
    0b0110000000101100,
    0b0110000111111010,
    0b0000000100010001,
    0b0000000100010001,
    0b0010000000000000,
    0b0000000000000001,
    0b0110111111111111
    ]


class CPU:
    def __init__(self):
        self.GPRs = Registers.GPRs()
        self.PSF  = Registers.PSF()
        self.PC   = Registers.PC()
    
    def Step(self):
        pc = self.PC.pc
        ins = program_mem[pc]
        self.Exec(ins)
        self.PC.pc += 1

    def Decode(self, ins):
        op  = (ins & 0b1111000000000000) >> 12
        rd  = (ins & 0b0000111100000000) >> 8
        rs1 = (ins & 0b0000000011110000) >> 4
        rs2 = (ins & 0b0000000000001111) >> 0
        imm = (ins & 0b0000000011111111) >> 0
        fn  = (ins & 0b0000000000001111) >> 0

        rs1 = self.GPRs.get(rs1)
        rs2 = self.GPRs.get(rs2)

        return [op,
                [rd, rs1, rs2], # R-Type
                [rd, imm],      # I-Type
                [rs1, fn],      # J-Type
                ]
    
    def Exec(self, ins):
        [op, [rd, rs1, rs2], [rd, imm], [rs1, fn]] = self.Decode(ins)

        def set_flag(val):
            ## Zero
            if val == 0:
                self.PSF.set(1, 'zero')
            else:
                self.PSF.set(0, 'zero')

            ## Sing
            if (val & 0b1000000000000000) == 1:
                self.PSF.set(1, 'sing')
            else:
                self.PSF.set(0, 'sing')

            ## Carry
            if val > 0xF:
                self.PSF.set(1, 'carry')
            else:
                self.PSF.set(0, 'carry')

        match op:
            case 0x0: # LDI
                self.GPRs.set(rd, imm)

            case 0x1: # ADD
                result = rs1 + rs2
                set_flag(result)
                self.GPRs.set(rd, result)

            case 0x2: 
                pass
            
            case 0x3: # RSH !!! (funct)
                result = rs1 >> 1
                set_flag(result)
                self.GPRs.set(rd, result)

            case 0x4: # AND
                result = rs1 & rs2
                set_flag(result)
                self.GPRs.set(rd, result)

            case 0x5: # NOR
                result = ~(rs1 | rs2)
                set_flag(result)
                self.GPRs.set(rd, result)
                
            case 0x6: # JMP
                match fn:
                    case 0x0: # 直接
                        self.PC.pc = rs1
                    case 0x1:
                        if self.PSF.get('zero') == 1:
                            self.PC.pc = rs1
                    case 0x2:
                        if self.PSF.get('sing') == 1:
                            self.PC.pc = rs1
                    case 0x3:
                        if self.PSF.get('carry') == 1:
                            self.PC.pc = rs1

            case 0x7: 
                pass
            case 0x8:
                pass
            case 0x9:
                pass
            case 0xA:
                pass
            case 0xB:
                pass
            case 0xC:
                pass
            case 0xD:
                pass
            case 0xE:
                pass
            case 0xF:
                pass



cpu = CPU()
for _ in range(len(program_mem)):
    cpu.Step()

