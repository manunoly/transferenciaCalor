__author__ = 'manuel'

import time
import random
from multiprocessing import Process, Queue
import os, psutil

class TareaCalcular:

    def __init__(self, cid, cola):
        self.__cid=cid
        self.__cola = cola
        self.Th = .0
        self.Tg = .0
        self.To = .0

    def __del__(self):
        print("HIJO {0} - Muere".format(self.__cid))

    def convergen(self, converge):
        cola.put([converge, self.__cid, self.To, self.Tg, self.Th])

    def run(self):

        # Generamos un tiempo de espera aleatorio
        s=1+int(19*random.random())

        time.sleep(s)
        if s < 1:
            self.convergen(True)
        else:
            self.convergen(False)

def matar_procesos(pid):
    parent = psutil.Process(pid)
    children = parent.get_children(recursive=True)

    for child in children:
        child.kill()
    psutil.wait_procs(children, timeout=5)

cola = Queue()

piscina = []
for i in range(1,100):
    piscina.append(Process(target=TareaCalcular(i, cola).run))

for proceso in piscina:
    proceso.start()

resultado = []
while piscina:

    if not cola.empty():
        valorC = cola.get()
        if valorC[0]:
            valorF = valorC
            matar_procesos(os.getpid())
            break
        else:
            resultado.append(valorC)
            for proceso in piscina:
                if not proceso.is_alive():
                    proceso.join()
                    piscina.remove(proceso)
                    del(proceso)
    # Para no saturar, dormimos al padre durante 1 segundo
    print("esperando a que los procesos hagan su trabajo")
    time.sleep(1)


print("PADRE: todos los hijos han terminado, cierro")

for valor in resultado:
    print(valor)
