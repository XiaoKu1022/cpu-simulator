class Memory:
    def __init__(self):
        self.mem = [0 for _ in range(2**16)]
    
    def read(self, address):
        return self.mem[address]
    
    def write(self, address, val):
        self.mem[address] = val
