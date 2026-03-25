from skaner import Lexer
from kolory import koloruj

with open("plik_we.txt", "r") as f:
    tekst = f.read()

lexer = Lexer(tekst)

wynik = ""

while True:
    t = lexer.skaner()
    if t[0] == "EOF":
        break
    wynik += koloruj(t)

html = f"""
<html>
<body>
<pre>
{wynik}
</pre>
</body>
</html>
"""

with open("pokolorowane.html", "w") as f:
    f.write(html)