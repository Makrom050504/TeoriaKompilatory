KOLORY = {
    "LOGIC": "blue",
    "TYPE": "pink",
    "ID": "black",
    "INT": "green",
    "OP": "red",
    "LBRACE": "purple",
    "RBRACE": "purple",
    "LPAREN": "yellow",
    "RPAREN": "yellow",
    "WS": "black"
}

def koloruj(token):
    typ, wartosc = token

    if typ == "WS":
        return wartosc

    kolor = KOLORY.get(typ, "black")
    return f'<span style="color:{kolor}">{wartosc}</span>'