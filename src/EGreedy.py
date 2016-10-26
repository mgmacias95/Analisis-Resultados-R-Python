#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Estadistico import *
from Greedy import *

class EGreedy(Estadistico):
    def __init__(self):
        super(EGreedy, self).__init__()
        self.nombre_csv = "resultados_greedy.csv"

    def ejecuta(self):
        for f in self.ficheros:
            print(f)
            g = Greedy(f, self.semilla)
            antes = time.time()
            gs = g.greedy()
            despues = time.time()
            self.tiempos.append(despues - antes)
            self.valores.append(g.evalua_sol(gs))
        self.imprime()

e = EGreedy()
e.ejecuta()
e.csv()
