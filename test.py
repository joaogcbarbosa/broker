import os
from threading import Thread
from multiprocessing import Process, Pipe, Value

# Função para usar com Thread
def f1(c):
    global a  # declara que a variável "a" será alterada globalmente
    a = a + 1  # valor de "a" passa a ser 2
    c = c + 1  # c == 2 e nada é feito com esse valor
    print(os.getpid())  # printa o PID do processo filho

    e.value = e.value + 1

a = 1
if __name__ == "__main__":
    b = 1

    # Usando Thread (ou seja, compartilhando recurso, memória e variáveis do processo pai)
    t = Thread(target=f1, args=(b,))  # envia b para worker "f"
    t.start()  # inicia o processo filho "f1"
    t.join()  # bloqueia a execução do programa até que o processo filho encerre a execução
    print(a, b)  # aqui o print deverá ser a == 2 e b == 2. Visto que a thread compartilha memória com o processo pai, então o valor de "b" deve ser alterado

    # Usando Process (ou seja, com recurso, memória e variáveis isoladas do processo pai)
    t = Process(target=f2, args=(b,))
    t.start()
    t.join()
    print(a, b)
    print(os.getpid())

    # Criando Pipe e Value
    c, d = Pipe()
    e = Value('i', 1)

    # Usando Process com Pipe e Value
    t = Process(target=f3, args=(c, e))
    t.start()
    print(d.recv())
    t.join()
    print(a, b, e.value)
