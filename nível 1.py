from multiprocessing import Process, Queue, Pipe
import os
import random


def funcao_comunicacao_queue(q):
    print(f"\tEstou na função funcao_comunicacao_queue e sou o processo {os.getpid()}")
    valor = random.randint(1, 10)
    q.put(valor)


def funcao_comunicacao_pipe(conn):
    print(f"\tEstou na função funcao_comunicacao_pipe e sou o processo {os.getpid()}")
    conn.send(['Olá', 'mundo', 'abril', 2022])
    conn.close()


if __name__ == '__main__':
    print(f"processo principal {os.getpid()}")
    # utilizando queue
    q = Queue()
    processo_1 = Process(target=funcao_comunicacao_queue, args=(q,))
    processo_1.start()
    valor = q.get()
    print(f"valor recebido: {valor}")
    processo_1.join()

    # utilizando pipe
    conn_pai, conn_filho = Pipe()
    processo_2 = Process(target=funcao_comunicacao_pipe, args=(conn_filho,))
    processo_2.start()
    valor = conn_pai.recv()
    print(f"valor recebido: {valor}")
    processo_2.join()

# Nível 1

# q = Queue() - Cria uma fila vazia com um tamanho ilimitado para armazenar elementos em memória.
# A fila pode ser usada para comunicação e sincronização entre threads e processos (nestes caso estamos a trabalhar
# com processos).

# q.put(valor) - Adiciona o valor especificado no final da fila q.
# Se a fila estiver cheia, a operação irá bloquear até que haja espaço disponível.

# valor = q.get() - Remove e retorna o próximo item da fila q.
# Se a fila estiver vazia, a operação irá bloquear até que um item esteja disponível.

# conn_pai, conn_filho = Pipe(): Cria um par de conexões do tipo Pipe (canal de comunicação) entre processos.
# conn_pai é a extremidade que será usada pelo processo pai para enviar mensagens ao processo filho,
# enquanto conn_filho é a extremidade que será usada pelo processo filho para enviar mensagens ao processo pai.

# conn.send(['Olá', 'mundo', 'abril', 2022]): Envia uma mensagem
# (uma lista, no exemplo) através da conexão conn para o outro processo (pai ou filho) conectado a ela.

# conn.recv(): Bloqueia até que uma mensagem seja recebida através da conexão 'conn' e retorna essa mensagem.

# conn.close(): Encerra a conexão 'conn' entre processos.