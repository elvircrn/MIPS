class RAM:
    def __init__(self):
        self.ram = [0 for _ in xrange(15)]
    
    def print_vals(self):
        for i in xrange(len(self.ram)):
            print "[" + str(i) + "]: " + self(self.ram[i])
