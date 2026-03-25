class Lexer:
    def __init__(self, text):
        self.text = text
        self.i = 0

    def znak(self):
        if self.i < len(self.text):
            return self.text[self.i]
        return None

    def skaner(self):
        z = self.znak()

        if z is None:
            return ("EOF", "")

        if z.isspace():
            start = self.i
            while self.znak() is not None and self.znak().isspace():
                self.i += 1
            return ("WS", self.text[start:self.i])
        
        if z.isdigit():
            start = self.i
            while self.znak() is not None and self.znak().isdigit():
                self.i += 1
            return ("INT", self.text[start:self.i])

        if z.isalpha() or z == "_":
            start = self.i
            while self.znak() is not None and (self.znak().isalnum() or self.znak() == "_"):
                self.i += 1

            slowo = self.text[start:self.i]
            if slowo in ["if", "print", "for", "while"]:
                return ("LOGIC", slowo)
            
            if slowo in ["int", "str", "double", "bool"]:
                return ("TYPE", slowo)
        
            return ("ID", slowo)

        if z in "+-*/=>!":
            self.i += 1
            return ("OP", z)

        if z == "{":
            self.i += 1
            return ("LBRACE", "{")

        if z == "}":
            self.i += 1
            return ("RBRACE", "}")
        
        if z == "(":
            self.i += 1
            return ("LPAREN", "{")

        if z == ")":
            self.i += 1
            return ("RPAREN", "}")

        raise ValueError(f"Błąd: {z}")