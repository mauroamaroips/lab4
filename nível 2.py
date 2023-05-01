import multiprocessing as mp

def produtor_pipe(pipe_conn):
    grupo_alunos = ['Mauro', 'David', 'Jorge']
    pipe_conn.send(grupo_alunos)
    print(f"{grupo_alunos} enviado pelo subprocesso produtor_pipe ({mp.current_process().name})")
    pipe_conn.close()

def consumidor_pipe(pipe_conn):
    grupo_alunos = pipe_conn.recv()
    print(f"{grupo_alunos} recebido pelo subprocesso consumidor_pipe ({mp.current_process().name})")
    pipe_conn.close()

def produtor_queue(queue):
    grupo_alunos = ['Amaro', 'Teixeira', 'Costa']
    queue.put(grupo_alunos)
    print(f"{grupo_alunos} enviado pelo subprocesso produtor_queue ({mp.current_process().name})")

def consumidor_queue(queue):
    grupo_alunos = queue.get()
    print(f"{grupo_alunos} recebido pelo subprocesso consumidor_queue ({mp.current_process().name})")

if __name__ == "__main__":
    print("processo (MainProcess)")

    print("Comunicação com Pipe")
    parent_conn, child_conn = mp.Pipe()
    produtor_pipe_process = mp.Process(target=produtor_pipe, args=(child_conn,))
    consumidor_pipe_process = mp.Process(target=consumidor_pipe, args=(parent_conn,))

    produtor_pipe_process.start()
    consumidor_pipe_process.start()

    produtor_pipe_process.join()
    consumidor_pipe_process.join()

    print("Comunicação com Queue")
    queue = mp.Queue()
    produtor_queue_process = mp.Process(target=produtor_queue, args=(queue,))
    consumidor_queue_process = mp.Process(target=consumidor_queue, args=(queue,))

    produtor_queue_process.start()
    consumidor_queue_process.start()

    produtor_queue_process.join()
    consumidor_queue_process.join()