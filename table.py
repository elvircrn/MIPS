from sys import stdout
import copy

class Table:
    def __init__(self):
        self.default_width = 10
        self.default_height = 3
        self.default_size = 5
        self.character = '*'

        # TODO: Find a better way to initialize a matrix
        s = ' ' * self.default_size
        row = [s for _ in xrange(self.default_width)]
        self.values = [copy.copy(row) for _ in xrange(self.default_height)]

    def nrow(self):
        return len(self.values)

    def _write_full(self, x, y):
        self.values[x][y] = "IF"
        self.values[x][y + 1] = "ID"
        self.values[x][y + 2] = "EX"
        self.values[x][y + 3] = "MEM"
        self.values[x][y + 4] = "WB"

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

    def draw(self):
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

