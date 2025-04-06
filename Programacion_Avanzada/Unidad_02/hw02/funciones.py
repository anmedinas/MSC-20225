#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''@author: Andres C. Medina'''

# Modulos Necesarios 
import numpy as np

# Constructor de funciones 
def f(x):
    """ 
    Función que calcula una función cuadrática para una lista de valores reales

    Parametros : 
    x : list 
        lista de valores numéricos (enteros o flotantes) para 
        los cuales se calcularán los cuadrados.

    Return :
    list 
        retorna una lista de valores elevados al cuadrado
    
    Ejemplo :     
    >>> f([1, 2, 3, 4])
    [1, 4, 9, 16]
    """ 
    return list(map(lambda i: i**2, x))

def g(x, y):
    """ 
    Función que calcula suma de seno y coseno 
    
    Parámetros:
    x : list
        Lista de valores numéricos (enteros o flotantes) para calcular el seno.
    y : list
        Lista de valores numéricos (enteros o flotantes) para calcular el coseno.

    Return:
    list
        Una lista con los resultados de la suma de seno y coseno de los 
        valores correspondientes en las listas de entrada.

    Ejemplo:
    >>> g([0, np.pi/2], [np.pi/2, np.pi])
    [1.0, 0.0]
    """
    return [np.sin(a) + np.cos(b) for a, b in zip(x, y)]

def h(x, y, z):
    """ 
    Función cúbica que toma tres listas de valores numéricos y 
    devuelve una lista con el producto de ellas.

    Parámetros:
    x : list
        Lista de valores numéricos (enteros o flotantes) para multiplicar.
    y : list
        Lista de valores numéricos (enteros o flotantes) para multiplicar.
    z : list
        Lista de valores numéricos (enteros o flotantes) para multiplicar.

    Retorna:
    list
        Una lista con el producto de los valores correspondientes en las tres listas de entrada.

    Ejemplo:
    >>> h([1, 2, 3], [4, 5, 6], [7, 8, 9])
    [28, 80, 162]
    """
    return [a * b * c for a, b, c in zip(x, y, z)]


class Funcion:
    """
    Representa una función matemática génerica.

    Atributos:
        nombre (str): Nombre de la función.
        variables (list): Lista de nombres de las variables.
        expresion (callable): Función matemática.

    Métodos:
        evaluar(*valores):
            Evalúa la función con los valores de entrada.
            Soporta np.linspace y np.arange.
    """

    def __init__(self, nombre, variables, expresion):
        """
        Inicializa la función matemática.

        Parámetros:
            nombre (str): Nombre de la función.
            variables (list): Lista de nombres de variables.
            expresion (callable): Función matemática.
        """
        self.nombre = nombre
        self.variables = variables
        self.expresion = expresion

    def evaluar(self, *valores):
        """
        Evalúa la función con los valores proporcionados.

        Parámetros:
            valores (np.ndarray): Arrays de valores generados con np.linspace o np.arange.

        Retorna:
            np.ndarray: Resultados de la evaluación.
        """
        if len(valores) != len(self.variables):
            raise ValueError(f"Se esperaban {len(self.variables)} argumentos, pero se recibieron {len(valores)}.")

        # Si hay una sola variable, aplica la función directamente
        if len(self.variables) == 1:
            return self.expresion(valores[0])

        # Si hay múltiples variables, crea una malla
        grid = np.meshgrid(*valores, indexing = 'ij')

        # Evalúa la función usando la malla
        return self.expresion(*grid)