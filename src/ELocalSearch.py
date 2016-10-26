#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Estadistico import *
from LocalSearch import *

class ELocalSearch(Estadistico):
    def __init__(self):
        super(ELocalSearch, self).__init__()
        self.nombre_csv = "resultados_localsearch.csv"

    def ejecuta(self):
        for f in self.ficheros:
            print(f)
            l = LocalSearch(f, self.semilla)
            antes = time.time()
            ls = l.local_search(l.sol_aleatoria())
            despues = time.time()
            self.tiempos.append(despues - antes)
            self.valores.append(ls[1])
        self.imprime()

e = ELocalSearch()
e.ejecuta()
e.csv()
