def letra_a_no_texto(texto: str):
    texto = texto.lower()
    quantidade = texto.count("a")
    return f"A letra 'a' aparece {quantidade} vezes no texto." if quantidade > 0 else "A letra não aparece no texto."

print(letra_a_no_texto("olo"))