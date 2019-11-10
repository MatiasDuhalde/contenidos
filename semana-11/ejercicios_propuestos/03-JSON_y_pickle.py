import json
import os
import pickle
import random


CARATTERISTICAS_CAMMINO = 'caratteristicas.json'
OPERAS_CAMMINO = 'operas.json'

class Obra:
    """
    Clase para las Obras de Antonini Da Ossa
    """

    def __init__(self, nome=None, autore=None, anno=None, posto=None,
                 stile=None, descrizione=None):

        self.nome = nome
        self.autore = autore
        self.anno = anno
        self.posto = posto
        self.stile = stile
        self.descrizione = descrizione

    def __getstate__(self):
        """
        Serializa las obras, agregando el atributo 'messaggio' al diccionario.
        """
        self.messagio = " ".join(random.sample(self.descrizione.split(), 3))
        new_dict = self.__dict__.copy()
        new_dict["messagio"] = self.messagio
        return new_dict


def cargar_obras(ruta_obras):
    """

    Funcion que carga las obras con las características pedidas,
    y luego entrega la lista de Obras.
    :param ruta_obras: Path de archivo de obras a cargar

    NOTA: DEBE USARSE la funcion obras_hook() como
     object hook para hacer el filtrado

    """
    with open(ruta_obras, 'r', encoding='utf-8') as obras_file:
        obras = json.load(obras_file, object_hook=obras_hook)
    return obras


def obras_hook(dict_obras):
    """
    Object hook que hace los objetos de la clase Obra y los añade a una lista.
    HINT: Utilizar aquí el archivo caratteristicas ;)
    """
    with open(CARATTERISTICAS_CAMMINO, 'r', encoding='utf-8') as caracteristicas_file:
        caracteristicas = json.load(caracteristicas_file)
    new_dict = dict()
    for key_ in caracteristicas:
        new_dict[key_] = dict_obras[key_]
    return Obra(**new_dict)


def generar_mensaje(lista_obras):
    """
    Serializa las obras y las guarda en archivos
    :param lista_obras: Lista de objetos de tipo obra cargados.
    """
    if not "Obras" in os.listdir():
        os.mkdir("Obras")
    for obra in lista_obras:
        with open(f"Obras/{obra.nome}-{obra.autore}.opera", 'wb') as obra_file:
            pickle.dump(obra, obra_file)

# Implementación
LISTA_OBRAS = cargar_obras(OPERAS_CAMMINO)
generar_mensaje(LISTA_OBRAS)
