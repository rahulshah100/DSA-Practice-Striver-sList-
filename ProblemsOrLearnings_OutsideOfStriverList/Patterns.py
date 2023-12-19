class Pattern:
    def __init__(self, rows, pattern):
        self.rows = rows
        self.pattern = pattern

    def BottomToTop(self):
        for i in range(1, self.rows + 1):
            print((self.rows - i) * ' ', end="")
            print(f"{self.pattern * i}")

    def ToptoBottom(self):
        for i in range(self.rows, 0, -1):
            print(i * self.pattern)

    def BottomToTopRev(self):
        for i in range(1, self.rows + 1):
            print(i * self.pattern)

    def ToptoBottomRev(self):
        for i in range(self.rows, 0, -1):
            print((self.rows - i) * " ", end="")
            print(i * self.pattern)

    def Diamond(self):
        for i in range(1, self.rows + 1):
            print((self.rows - i) * ' ', end="")
            print(i * self.pattern, end="")
            print((i - 1) * self.pattern)
        for i in range(self.rows - 1, 0, -1):
            print((self.rows - i) * " ", end="")
            print((2*i - 1) * self.pattern)


P = Pattern(4, '*')
P.BottomToTop()
print()
P.ToptoBottom()
print()
P.BottomToTopRev()
print()
P.ToptoBottomRev()
print()
P.Diamond()