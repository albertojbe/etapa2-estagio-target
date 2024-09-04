# ETAPA 2 DO PROCESSO SELETIVO - TARGET
Alberto Cesar Pinheiro

- Questão 1

```python
def fibonacci(n, contador = 0, termo = 0, numeros = None, f1 = 0, f2 = 1):
    if numeros == None:
        numeros = []
    
    if contador == n:
        return numeros
    
    numeros.append(termo)
    termo = f1 + f2
    return fibonacci(n, contador +1 , termo, numeros, termo, f1)

def view():
    enesimo = int(input("Digite o enésimo termo para saber seu valor em Fibonacci: "))
    sequencia = fibonacci(enesimo)
    print(f"A sequência é {sequencia}")
    if enesimo in sequencia:
        print("O número que você digitou está na sequência")
    else: print("O número que você digitou não está na sequência.")

view()
```


- Questão 2
```python
def letra_a_no_texto(texto: str):
    texto = texto.lower()
    quantidade = texto.count("a")
    return f"A letra 'a' aparece {quantidade} vezes no texto." if quantidade > 0 else "A letra não aparece no texto."

print(letra_a_no_texto("olo"))
```

- Questão 3

``Resultado = 77``

<br>

- Questão 4
```
a) 1, 3, 5, 7, R: 9
b) 2, 4, 8, 16, 32, 64, R: 128
c) 0, 1, 4, 9, 16, 25, 36, R: 49
d) 4, 16, 36, 64, R: 100
e) 1, 1, 2, 3, 5, 8, R: 13
f) 2,10, 12, 16, 17, 18, 19, R: 20
```

<br>

- Questão 5


Ligo o primeiro interruptor por alguns minutos, depois desligo-o e ligo o segundo interruptor. Em seguida, escolho uma sala e vou até ela para observar se a lâmpada está acesa, quente ou fria, e assim descubro a qual interruptor ela pertence. Depois, volto e vou até outra sala para fazer a mesma observação. Dependendo da situação em que a lâmpada se encontra, conseguirei identificar a qual interruptor ela pertence, precisando visitar apenas duas salas, devido ao processo de exclusão.
