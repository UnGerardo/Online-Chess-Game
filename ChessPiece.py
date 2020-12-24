class ChessPiece:
    def __init__(self, name, build, x, y):
        self.name = name
        self.type = build
        self.pos = (x, y)
        self.captured = False

    def killed(self):
        self.captured = True
