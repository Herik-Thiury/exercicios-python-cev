expr = str(input(""))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append("(")
    