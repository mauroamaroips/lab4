import time
from multiprocessing import Process, Queue, current_process, Manager


def fibonacci(n):
    a, b = 0, 1
    for item in range(n):
        a, b = b, a + b
    return a


def mostrar_dicionario(dicionario):
    for n in dicionario.keys():
        print(f"Fib({n}) = {dicionario[n]}")


def gerar_chaves(fibo_dict, qtd):
    for i in range(qtd):
        fibo_dict[i+1] = None


def calcular_valores(q, fibo_dict):
    cont = 0
    while not q.empty():
        n = q.get()
        if n:
            fibo_dict[n] = fibonacci(n)
            cont = cont + 1
    print(f"{current_process().name} - calculou {cont} termo(s) da série")


def calcular_valores_pool(fibo_dict, n):
    # print(f"Processo {current_process().name} a calcular Fib({n})")
    fibo_dict[n] = fibonacci(n)


if __name__ == '__main__':
    qtd_valores = 10000
    numero_de_processos = 4
    inicio = time.time()
    manager = Manager()
    dicionario_fibonacci_par = manager.dict()
    gerar_chaves(dicionario_fibonacci_par, qtd_valores)
    fila_de_valores_fibonacci = Queue()
    # print(dicionario_fibonacci_par.keys())
    for k in dicionario_fibonacci_par.keys():
        fila_de_valores_fibonacci.put(k)
    lista_de_processos = []
    for _ in range(numero_de_processos):
        p = Process(target=calcular_valores, args=(fila_de_valores_fibonacci, dicionario_fibonacci_par))
        p.start()
        lista_de_processos.append(p)
    [p.join() for p in lista_de_processos]
    fim = time.time()
    print(f"Tempo utilizado para calcular os primeiros {qtd_valores} termos da série de Fibonacci utilizando "
          f" multiprocessamento {fim - inicio:.10f}s")
    mostrar_dicionario(dicionario_fibonacci_par)

# Nível 4

# Pergunta 1

# manager = Manager(): cria um objeto Manager do módulo multiprocessing,
# que permite criar objetos compartilhados entre processos.

# dicionario_fibonacci_par = manager.dict(): cria um dicionário compartilhado
# que é gerido pelo objeto Manager criado anteriormente.

# gerar_chaves(dicionario_fibonacci_par, qtd_valores): uma função que recebe um dicionário e preenche as
# chaves com valores None até o número máximo de chaves informado em qtd_valores.

# [p.join() for p in lista_de_processos]: aguarda o fim de cada processo da lista_de_processos usando a função join().
# Existe uma itera sobre cada processo na lista_de_processos
# e chama join() para aguardar a finalização de cada um deles.

# Pergunta 3

#Em relação à análise crítica, podemos dizer que a abordagem utilizada para dividir o trabalho
# entre os processos é eficiente, uma vez que cada processo recebe uma chave da "queue" e não há
# conflito de acesso ao dicionário compartilhado. Entretanto, o número de processos criados pode não ser adequado para a
# quantidade de termos a serem calculados (são inicializados 4 processo).

# Por exemplo, se a quantidade de termos a serem calculados for muito grande, o número de processos criados pode
# tornar-se excessivo, levando a uma sobrecarga do operativo e a um aumento no tempo total de processamento.
# Por outro lado, se a quantidade de termos for muito pequena, a criação de processos
# adicionais pode não resultar em ganhos significativos de desempenho.

# Para além disso, a implementação do cálculo da série de Fibonacci utilizado nos processos pode ser melhorada,
# uma vez que a versão atual não utiliza nenhum tipo de otimização.
# Por exemplo, uma implementação utilizando recursão pode levar a ganhos significativos de desempenho.