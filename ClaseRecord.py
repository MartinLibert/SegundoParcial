import pygame
from copy import deepcopy
from random import choice, randrange

class Record:
    def __init__(self):
        pass

    def obtener_record(self):
        try:
            with open('record') as f:
                return f.readline()  # Lee la primera línea del archivo y la devuelve
        except FileNotFoundError:
            with open('record', 'w') as f:
                f.write('0')  # Escribe '0' en el archivo
                return '0'  # Devuelve '0' como valor predeterminado si el archivo no existe

    def establecer_record(self, record, puntaje):
        rec = max(int(record), puntaje)  # Toma el máximo entre el valor entero de 'record' y 'puntaje'
        with open('record', 'w') as f:
            f.write(str(rec))  # Escribe el valor de 'rec' en el archivo después de convertirlo a una cadena de texto