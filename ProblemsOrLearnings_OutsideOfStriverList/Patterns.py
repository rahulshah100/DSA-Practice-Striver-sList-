class Pattern:
    def __init__(self, rows, pattern):
        self.rows = int(rows/2)
        self.pattern = pattern

    def bottomtotop(self):
        j = self.rows - 1
        k = 1
        for i in range(self.rows):
            print(j * ' ', end="")
            print(f"{k * self.pattern}")
            j -= 1
            k += 1

    def toptobottom(self):
        k = 0
        for i in range(self.rows, 0, -1):
            print(i * self.pattern, end="")
            print(k * " ")
            k += 1

    def bottomtotopreversed(self):
        for i in range(1, self.rows):
            print(i * self.pattern)

    def toptobottomreversed(self):
        k = 0
        for i in range(self.rows, 0, -1):
            print(k * " ", end="")
            print(i * self.pattern)
            k += 1

    def diamond(self):
        spaces = self.rows - 1
        for i in range(1, self.rows + 1):
            j = i - 1
            print(spaces * " ", end="")
            print(i * self.pattern, end="")
            print(j * self.pattern)
            spaces -= 1
        spaces = 0
        for i in range(self.rows, 0, -1):
            j = i - 1
            print(spaces * " ", end="")
            print(i * self.pattern, end="")
            print(j * self.pattern)
            spaces += 1


P = Pattern(10, '*')
P.bottomtotop()
print()
P.toptobottom()
print()
P.bottomtotopreversed()
print()
P.toptobottomreversed()
print()
P.diamond()
