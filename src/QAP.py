#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
import csv
import statistics

class QAP(object):
    """
    Clase donde se encapsularán los distintos algoritmos para el cálculo de
    soluciones y donde se guardarán los datos de una instancia QAP
    """

    """
    Constructor de la clase, donde a partir del nombre de un fichero se inicializa
    una instancia del problema QAP rellenando las matrices de flujos y distancias.
    """
    def __init__(self, nombre_fichero, semilla):
        # generamos una semilla con el reloj del sistema
        random.seed(semilla)
        # abrimos el fichero a leer
        f = open(nombre_fichero, 'r')
        # lo guardamos en una lista
        dat = list(f.read().split())
        dat = [int(i) for i in dat]
        self.nombre_csv = "Resultados/conver.csv"
        self.soluciones_obtenidas = []
        self.iter = []
        self.promediar = False
        # y lo cerramos
        f.close()
        # guardamos el tamaño
        self.n = dat.pop(0)
        # y el contenido de las matrices
        self.mflujo = []
        for i in range(0,self.n*self.n,self.n):
            self.mflujo.append(dat[i:i+self.n])

        dat = dat[self.n*self.n:]

        self.mdistancia = []
        for i in range(0,self.n*self.n,self.n):
            self.mdistancia.append(dat[i:i+self.n])
        
    """
    Método para evaluar la calidad de una solución. Para ello, multiplicamos 
    el flujo por la distancia y sumamos
    """
    def evalua_sol(self, sol):
        # hacemos un bucle evaluando el flujo y la distancia de cada unidad con
        # las demás.
        sumatoria = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                sumatoria += self.mflujo[i][j] * self.mdistancia[sol[i]][sol[j]]

        return sumatoria # devolvemos el coste de la solucion encontrada

    """
    Método para intercambiar dos valores de una lista
    """
    def swap(self,i,j,l):
        l[i], l[j] = l[j], l[i]

        return l

    """
    Método para generar un vecino
    """
    def genera_vecino(self, sol_act):
        # generamos dos enteros aleatorios
        i,j = random.sample(range(self.n-1),2)

        # en la solución actual, los intercambiamos y devolvemos el vecino
        # también devolvemos el i y el j calculados por random para poder
        # tener en cuenta sólo esas posiciones de la lista a la hora de calcular
        # el coste
        return i, j, self.swap(i,j,sol_act)

    """
    Método para generar un vecindario
    """
    def genera_vecindario(self, num_vecinos, sol_act):
        # generamos num_vecinos aleatorios con la función genera vecino
        # pasamos la solución actual por copia para que no sea modificada
        vecinos = [self.genera_vecino(list(sol_act)) for i in range(num_vecinos)]
        # le añadimos a cada vecino su coste con respecto de la solución actual
        vecinos = [(v, self.coste_vecino(sol_act,v[0],v[1])) for v in vecinos]
        # los ordenamos por menor coste con los i y j cambiados.
        vecinos = sorted(vecinos, key=lambda v: v[1])
        # # los devolvemos sin los valores i j encontrados por random
        # return [vecinos[i][2] for i in range(num_vecinos)]
        return vecinos

    """
    Método para saber el coste de un vecino
    """
    def coste_vecino(self, sol_act, r, s):
        # guardamos en una lista todos los indices desde 0 hasta n menos r y s
        indices = set(list(range(self.n))) - set([r,s])
        # inicializamos la sumatoria
        sumatoria = 0
        # evaluamos la solución vecina
        for k in list(indices):
            sumatoria += self.mflujo[r][k] * (self.mdistancia[sol_act[s]][sol_act[k]] - \
                self.mdistancia[sol_act[r]][sol_act[k]]) + self.mflujo[s][k] * \
                (self.mdistancia[sol_act[r]][sol_act[k]] - self.mdistancia[sol_act[s]][sol_act[k]]) \
                + self.mflujo[k][r] * (self.mdistancia[sol_act[k]][sol_act[s]] - \
                self.mdistancia[sol_act[k]][sol_act[r]]) + self.mflujo[k][s] * \
                (self.mdistancia[sol_act[k]][sol_act[r]] - self.mdistancia[sol_act[k]][sol_act[s]])

        # devolvemos la sumatoria coste de la nueva solución
        return sumatoria

    """
    Método para generar una solución aleatoria
    """
    def sol_aleatoria(self):
        return random.sample(range(self.n), self.n)

    def csv(self):
        if len(self.iter) == 0:
            self.iter = list(range(len(self.soluciones_obtenidas)))

        if self.promediar:
            aux_iter = []
            aux_sols = []
            num_promedios = int(len(self.soluciones_obtenidas)/25)
            for i in range(0, len(self.soluciones_obtenidas), num_promedios):
                aux_iter.append(self.iter[i])
                aux_sols.append(int(statistics.mean(self.soluciones_obtenidas[i:(i+num_promedios)])))
            self.iter = aux_iter
            self.soluciones_obtenidas = aux_sols


        with open(self.nombre_csv, 'w') as csvfile:
            fieldnames = ["Iteraciones","Coste"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(self.soluciones_obtenidas)):
                writer.writerow({'Iteraciones':str(self.iter[i]), 'Coste':str(self.soluciones_obtenidas[i])})
        csvfile.close()