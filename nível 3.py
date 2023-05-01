import time

def fibonacci(n):
    a, b = 0, 1
    for item in range(n):
        a, b = b, a + b
    return a

def preencher_dicionario_fibonacci_v1(dicionario, qtd):
    for i in range(qtd):
        dicionario[i+1] = fibonacci(i+1)

def preencher_dicionario_fibonacci_v2(dicionario, qtd):
    for i in range(qtd):
        if i < 2:
            dicionario[i+1] = 1
        else:
            dicionario[i+1] = dicionario[i] + dicionario[i-1]

def mostrar_dicionario(dicionario):
    for n in dicionario.keys():
        print(f'Fib({n}) = {dicionario[n]}')

if __name__ == '__main__':
    qtd_valores = 10000
    inicio = time.time()
    dicionario_fibonacci = {}
    preencher_dicionario_fibonacci_v1(dicionario_fibonacci, qtd_valores)
    tempo = time.time() - inicio
    print(f'{tempo:.10f}s para calcular os primeiros {qtd_valores} termos da série de Fibonacci de forma sequencial')
    #mostrar_dicionario(dicionario_fibonacci)
    inicio = time.time()
    dicionario_fibonacci = {}
    preencher_dicionario_fibonacci_v2(dicionario_fibonacci, qtd_valores)
    tempo = time.time() - inicio
    print(f'{tempo:.10f}s para calcular os primeiros {qtd_valores} termos da série de Fibonacci de forma sequencial')
    mostrar_dicionario(dicionario_fibonacci)

# Nível 3

# Pergunta 1

# Este programa implementa duas funções para preencher um dicionário com os primeiros n termos da sequência
# de Fibonacci e uma função para mostrar os valores do dicionário na tela.

# O programa utiliza dois métodos diferentes para calcular os valores da sequência de Fibonacci:
# a função "fibonacci" que calcula os valores sequencialmente e a função "preencher_dicionario_fibonacci_v2"
# que utiliza a definição recursiva da sequência de Fibonacci para calcular os valores.

# O programa imprime o tempo de execução de cada método e, em seguida, imprime os valores da
# sequência de Fibonacci armazenados no dicionário.
# No exemplo dado, o programa calcula e imprime os primeiros 10 termos da sequência de Fibonacci.

# Pergunta 2

# Em Python, um dicionário é uma estrutura de dados que armazena pares de chave-valor.
# As chaves são usadas para indexar e aceder aos valores correspondentes.

# Pergunta 3

# Ao executar o programa com qtd_valores igual a 10000, nota-se que a primeira função
# preencher_dicionario_fibonacci_v1 demora bastante para calcular todos os valores da série de Fibonacci.
# Por outro lado, a segunda função preencher_dicionario_fibonacci_v2 calcula a série muito mais rapidamente.

# Isto ocorre porque a primeira função calcula cada número da série de Fibonacci
# sequencialmente, enquanto a segunda função aproveita a recursividade da
# série de Fibonacci para calcular os números de forma mais eficiente.
# A primeira função tem complexidade de tempo O(n^2), enquanto a segunda tem complexidade de tempo O(n).