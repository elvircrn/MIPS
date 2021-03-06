from table import Table

class RAM:
    def __init__(self):
        self.ram = [0 for _ in xrange(200)]
        self.touched = [False for _ in xrange(200)]
    
    def print_vals(self):
        print "RAM:\n"
        for i in xrange(len(self.ram)):
            print "[" + str(i) + "]: " + str(self.ram[i])

    def print_touched(self):
        print "RAM:\n"
        for i in xrange(len(self.ram)):
            if self.touched[i]:
                print "[" + str(i) + "]: " + str(self.ram[i])

    def __getitem__(self, ind):
        return self.ram[ind]

    def __setitem__(self, ind, value):
        self.touched[ind] = True
        self.ram[ind] = value

