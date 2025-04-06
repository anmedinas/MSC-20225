#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''@author: Andres C. Medina'''

from matplotlib import pyplot as plt
import math
import time

def medir_tiempo(func):
    """
    Decorador para medir el tiempo de ejecución de una función.

    Args:
        func (callable): La función a decorar.

    Returns:
        callable: La función decorada.
    """
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de '{func.__name__}': {fin - inicio:.6f} segundos")
        return resultado
    return wrapper


class PuntoBase:
    """
    Superclase que define un punto en un espacio bidimensional.
    """
    def __init__(self, x, y):
        """
        Inicializa un nuevo punto en el espacio bidimensional.

        Args:
            x (float): Coordenada en el eje X.
            y (float): Coordenada en el eje Y.
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Las coordenadas deben ser números reales (int o float)")
        if math.isinf(x) or math.isinf(y):
            raise ValueError("Las coordenadas no pueden ser infinitas")
        if math.isnan(x) or math.isnan(y):
            raise ValueError("Las coordenadas no pueden ser NaN (Not a Number)")
        self.x = x
        self.y = y

    def __str__(self):
        """
        Devuelve una representación en cadena del punto.

        Returns:
            str: Representación en formato "(x, y)".
        """
        return f"({self.x}, {self.y})"


class Punto2D(PuntoBase):
    """
    Subclase que extiende la funcionalidad de PuntoBase para incluir operaciones adicionales.
    """
    def __call__(self, escalar):
        """
        Permite usar el objeto como una función para realizar la multiplicación por un escalar.

        Args:
            escalar (float): Valor por el cual se multiplicarán las coordenadas del punto.

        Returns:
            Punto2D: Un nuevo punto con las coordenadas escaladas.
        """
        return Punto2D(self.x * escalar, self.y * escalar)

    def __mul__(self, escalar):
        """
        Multiplica el punto por un escalar.

        Args:
            escalar (float): Valor por el cual se multiplicarán las coordenadas del punto.

        Returns:
            Punto2D: Un nuevo punto con las coordenadas escaladas.
        """
        return Punto2D(self.x * escalar, self.y * escalar)

    def __rmul__(self, escalar):
        """
        Permite la multiplicación con el escalar en cualquier orden.

        Args:
            escalar (float): Valor por el cual se multiplicarán las coordenadas del punto.

        Returns:
            Punto2D: Un nuevo punto con las coordenadas escaladas.
        """
        return self.__mul__(escalar)

    def __add__(self, otro):
        """
        Suma las coordenadas de dos puntos.

        Args:
            otro (Punto2D): Otro punto a sumar.

        Returns:
            Punto2D: Un nuevo punto con las coordenadas sumadas.
        """
        return Punto2D(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        """
        Resta las coordenadas de dos puntos.

        Args:
            otro (Punto2D): Otro punto a restar.

        Returns:
            Punto2D: Un nuevo punto con las coordenadas restadas.
        """
        return Punto2D(self.x - otro.x, self.y - otro.y)
    
    def grafica(self):
        """
        Grafica el punto en un plano bidimensional con etiquetas de ejes y un 
        título. La gráfica incluye una cuadrícula, líneas de referencia en los 
        ejes y el punto resaltado.

        Returns:
            None
        """
        plt.figure(figsize=(6, 6))
        plt.scatter(self.x, self.y, color='blue', label=f'Punto ({self.x}, {self.y})')
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.title('Gráfica del Punto')
        plt.legend(loc='best')
        plt.show()

    @medir_tiempo
    def distancia(self, otro):
        """
        Calcula la distancia euclidiana entre este punto y otro punto.

        Args:
            otro (PuntoBase): El otro punto con el cual calcular la distancia.

        Returns:
            float: La distancia euclidiana entre los dos puntos.
        """
        return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)
    
    def __abs__(self):
        """
        Calcula la distancia euclidiana del punto al origen (0, 0).

        Returns:
            float: La distancia del punto al origen.
        """
        return math.sqrt(self.x**2 + self.y**2)