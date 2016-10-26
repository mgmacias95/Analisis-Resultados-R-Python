#!/usr/bin/env python
# -*- coding: utf-8 -*-

from QAP import *
import time
import sys
from tabulate import tabulate
import csv

class Estadistico:
    
    def __init__(self):
        self.ficheros = ["datos/chr20a.dat", "datos/chr20c.dat", "datos/chr22b.dat",
            "datos/chr25a.dat","datos/esc32a.dat","datos/esc64a.dat","datos/esc128.dat",
            "datos/kra32.dat", "datos/lipa90a.dat","datos/sko42.dat","datos/sko49.dat",
            "datos/sko81.dat","datos/sko90.dat","datos/sko100f.dat","datos/tai64c.dat","datos/tai80a.dat",
            "datos/tai100a.dat","datos/tai150b.dat","datos/tai256c.dat","datos/tho150.dat"]
        self.mejores_sol = [2192, 14142, 6194, 3796, 130, 116, 64, 88700, 360630, 15812, 23386,
            90998, 115534, 149036, 1855928, 13499184, 21052466, 498896643, 44759294, 8133398]
        self.tiempos = []
        self.valores = []
        self.desviaciones = []
        self.semilla = 31
        self.nombre_csv = "resultados.csv"

    def calcula_desv(self):
        for i in range(len(self.ficheros)):
            self.desviaciones.append(100*((self.valores[i] - self.mejores_sol[i])/self.mejores_sol[i]))

    desv = lambda self: sum(self.desviaciones)/len(self.ficheros)

    tiempo = lambda self: sum(self.tiempos)/len(self.tiempos)

    def imprime(self):
        self.calcula_desv()
        table = [[self.ficheros[i], self.valores[i], self.tiempos[i], 
            self.desviaciones[i]] for i in range(len(self.ficheros))]
        print(tabulate(table, headers=["Fichero", "Coste", "Tiempo", "Desviación"], 
            tablefmt="latex"))
        print("Desviación = ",self.desv())
        print("Tiempo = ",self.tiempo())

    def csv(self):
        with open("Resultados/"+self.nombre_csv, 'w') as csvfile:
            fieldnames = ["Coste","Tiempo","Desviacion"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(self.ficheros)):
                writer.writerow({'Coste':str(self.valores[i]), 
                    'Tiempo':str(self.tiempos[i]), 'Desviacion':str(self.desviaciones[i])})
        csvfile.close()

    def mejor_csv(self):
        with open("mejor_csv.csv", 'w') as csvfile:
            fieldnames = ["Caso","Coste"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(self.ficheros)):
                writer.writerow({'Caso':self.ficheros[i].split("/",1)[1], 
                    'Coste':str(self.mejores_sol[i])})
        csvfile.close()
