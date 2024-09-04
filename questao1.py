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


