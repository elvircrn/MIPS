"""Contains a set of registers."""
class RegisterSet:
    def __init__(self):
        self.registers = [0 for _ in range(32)]
        self.touched = [False for _ in range(32)]

    def print_value(self, ind):
        print "[" + str(ind) + "]: " + str(self.registers[ind])

    def print_values(self):
        print "Registers:\n"
        for i in xrange(len(self.registers)):
            self.print_value(i)

    def __getitem__(self, code):
        # Register name given in the format R<id>
        if isinstance(code, basestring):
            return self.registers[int(code[1:])]

        # Register name given in the format <id>
        return self.registers[code]

    def __setitem__(self, code, value):
        ind = 0

        # Register name given in the format R<id>
        if isinstance(code, basestring):
            ind = int(code[1:])
        # Register name given in the format <id>
        elif isinstance(code, int):
            ind = int(code)

        self.touched[ind] = True
        self.registers[ind] = value

    def print_touched(self):
        for i in xrange(32):
            if self.touched[i]:
                self.print_value(i)
