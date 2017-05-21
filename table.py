from sys import stdout
import copy

class Table:
    def __init__(self):
        self.default_width = 10
        self.default_height = 3
        self.default_size = 5
        self.character = '*'

        # TODO: Find a better way to initialize a matrix
        # s = ' ' * self.default_size
        # row = [s for _ in xrange(self.default_width)]
        # self.values = [copy.copy(row) for _ in xrange(self.default_height)]
        self.values = []

    def nrow(self):
        return len(self.values)

    def is_dash(self, x, y):
        return (x != 0 and y < (len(self.values[x - 1])) and (self.values[x - 1][y] == "RAW"))
    
    def _write_full(self, x, y):
        cycles = ["IF", "ID", "EX", "MEM", "WB"]
        i = 0
        row = y * [' ']
        while(i < len(cycles)):
            if(self.is_dash(x, y)):
                row.extend(["-"])
            elif(x != 0 and i==0 and (self.values[x - 1][y] in ["IF", "-", " "])):
                row.extend([" "])
            else:
                row.extend([cycles[i]])
                i += 1
            y += 1
        self.values.append(row)

    def stall_till_wb(self, y):
        l = len(self.values)
        ind = self.values[l - 1].index("ID")
        ind += 1
        while(self.values[l - 1][ind] in ["-", "RAW"]):
            ind += 1
        ind2 = self.values[y].index("WB")
        n = ind2 - ind + 1
        if(n > 0):
            row = self.values[l - 1][0 : ind]
            row.extend(["RAW"] * n)
            row.extend(self.values[l - 1][ind:])
            self.values[l - 1] = row      

    def ncol(self):
        if (self.nrow() > 0):
            return len(self.values[0]) if self.nrow() > 0 else 0

    def col_maxw(self, col):
        mx = self.default_size
        for i in xrange(self.nrow()):
            mx = max(mx, len(self.values[i][col]))
        return mx

    def _draw_line(self):
        s = sum([self.col_maxw(x) for x in xrange(0, self.ncol())])
        stdout.write(self.character * (s + self.ncol() + 1))

    def pad(self):
        l = len(self.values)
        if(l > 1):
            s = len(self.values[l - 1])
            for i in range(l - 1):
                self.values[i].extend([' '] * (s - len(self.values[i])))

    def draw(self):
        self.pad()
        self._draw_line()
        stdout.write('\n')
        for i in xrange(len(self.values)):
            stdout.write(self.character)
            for j in xrange(len(self.values[i])):
                col = self.col_maxw(j)
                stdout.write((self.values[i][j]).center(col))
                stdout.write(self.character)
            stdout.write('\n')
            self._draw_line()
            stdout.write('\n')
        
        #print self.values
