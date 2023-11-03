from threading import Thread

import os

def fun1():
    pid = os.getpid()
    print('hijo', pid)

if __name__ == "__main__":
        pid=os.getpid()
        print("Proceso padre: ", pid)
        #fun1()
        Thread = Thread(target=fun1)
        Thread.start()
        Thread.join()


import multiprocessing

# Función que realiza una tarea en un subproceso
def worker_function(worker_id):
    print(f"Subproceso {worker_id} realizando tarea")

if __name__ == "__main__":
    num_workers = 4  # Número de subprocesos que se crearán

    # Crear una lista para almacenar los subprocesos
    processes = []

    # Crear y ejecutar subprocesos
    for i in range(num_workers):
        process = multiprocessing.Process(target=worker_function, args=(i,))
        processes.append(process)
        process.start()

    # Esperar a que todos los subprocesos terminen
    for process in processes:
        process.join()

    print("Proceso principal ha terminado")
