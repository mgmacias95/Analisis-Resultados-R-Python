#!/usr/bin/env python
# -*- coding: utf-8 -*-

from QAP import *

class LocalSearch(QAP):
    """
    Clase que implementa la búsqueda local
    """
    def __init__(self, nombre_fichero, semilla):
        super(LocalSearch, self).__init__(nombre_fichero, semilla)

    """
    Función principal de la clase
    """
    def local_search(self, punto_inicio, max_iter=25000):
        # hacemos el bucle hasta que o el coste no mejore o hayamos recorrido el
        # vecindario entero (hacemos un máximo de iteraciones)
        # guardamos el coste de nuestra primera solución
        coste = self.evalua_sol(punto_inicio)
        # inicializamos un contador de iteraciones
        iteraciones = 0
        # inicializamos el vector de Don't look bits
        dlb = [0]*self.n
        # inicializamos un flag para ver si ha habido mejora o no
        improve_flag = True
        # y la solución actual
        sol_act = punto_inicio

        # empezamos con el bucle externo
        while iteraciones < max_iter and improve_flag:
            # bucle interno, tal y como está descrito en la pag 23 del seminario 2a
            for i in range(0,self.n):
                if dlb[i] == 0:
                    improve_flag = False
                    # empezamos en i+1 para no repetir soluciones ya analizadas
                    for j in range(self.n):
                        coste_prima = self.coste_vecino(sol_act, i, j)
                        # si el coste es negativo quiere decir que ha habido mejora
                        if coste_prima < 0:
                            # si ha habido mejora nos quedamos con la solución buena
                            sol_act = self.swap(i,j,sol_act)
                            coste += coste_prima  # actualizamos el coste de sol_act
                            dlb[i] = 0
                            dlb[j] = 0
                            improve_flag = True
                    # si no ha habido mejora ponemos el dlb a 1 para no volver a
                    # mirar esa solución
                    if not improve_flag:
                        dlb[i] = 1  
            # incrementamos el numero de iteraciones
            iteraciones += 1
        # devolvemos la solución actual junto a su coste
        return sol_act, coste
