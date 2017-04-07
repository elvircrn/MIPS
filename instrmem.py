class InstrMem:
    def __init__(self):
        self.instructions = []
        
    def decode_add(self, instruction):
        self.instructions.append(0)
        return 0