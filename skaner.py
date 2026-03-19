class Lexer:
    def __init__(self, text):
        self.text = text
        self.i = 0

    def znak(self):
        if self.i < len(self.text):
            return self.text[self.i]
        return None

    def pomin_biale(self):
        while self.znak() is not None and self.znak().isspace():
            self.i += 1

    def skaner(self):
        self.pomin_biale()
        z = self.znak()
        kol = self.i + 1

        if z is None:
            return ("EOF", "")

        if z.isdigit():
            start = self.i
            while self.znak() is not None and self.znak().isdigit():
                self.i += 1
            return ("INT", self.text[start:self.i])

        if z.isalpha() or z == "_":
            start = self.i
            while self.znak() is not None and (self.znak().isalnum() or self.znak() == "_"):
                self.i += 1
            return ("ID", self.text[start:self.i])

        znaki = {
            "+": "PLUS",
            "-": "MINUS",
            "*": "MUL",
            "/": "DIV",
            "(": "LPAREN",
            ")": "RPAREN"
        }

        if z in znaki:
            self.i += 1
            return (znaki[z], z)

        raise ValueError(f"Błąd w kolumnie {kol}: zły znak '{z}'")


tekst = input("Podaj wyrażenie: ")
lexer = Lexer(tekst)

while True:
    try:
        t = lexer.skaner()
        print(t)
        if t[0] == "EOF":
            break
    except ValueError as e:
        print(e)
        break