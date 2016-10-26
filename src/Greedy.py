#!/usr/bin/env python
# -*- coding: utf-8 -*-

from QAP import *

class Greedy(QAP):
    """
    Clase que implementa la búsqueda Greedy
    """
    def __init__(self, nombre_fichero, semilla):
        super(Greedy, self).__init__(nombre_fichero, semilla)

    """
    Método greedy. Se basa en dos vectores: el potencia de flujo que es la sumatoria
    de flujos de una unidad al resto y el potencial de distancia que es la sumatoria
    de la distancia k al resto. Se tomará la que más flujo tenga y la que menor 
    distancia tenga.
    """
    def greedy(self):
        # inicializamos los vectores de potencias
        pflujo = []
        pdistancia = []

        # calculamos la potencia de cada unidad según su distancia al centro y su flujo
        for i in range(0,self.n):
            pflujo.append(sum(self.mflujo[i]))
            pdistancia.append(sum(self.mdistancia[i]))

        # inicializamos el vector solución
        sol = [0]*self.n

        # lo vamos rellenando metiendo en la posición i de sol la unidad con
        # más flujo y menor distancia
        for i in range(0,self.n):
            # obtenemos la unidad con más flujo
            u_f = pflujo.index(max(pflujo))
            # y la unidad con menor distancia
            u_d = pdistancia.index(min(pdistancia))
            # asignamos a la unidad con más flujo la localización más cercana
            sol[u_f] = u_d
            # en esas ponemos dichos valores a menos y más infito respectivamente
            # para que no vuelvan a ser escogidos
            pflujo[u_f] = -math.inf
            pdistancia[u_d] = math.inf

        # devolvemos la solución encontrada
        return sol
