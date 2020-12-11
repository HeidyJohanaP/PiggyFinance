from typing import Dict
from pydantic import BaseModel
import datetime

class Movimiento(BaseModel):
    id: int
    fecha: datetime.date
    valor: int
    categoria: str
    descripcion: str
    tipo: str

#Diccionario
database_movs = Dict[int, Movimiento]

database_movs = {
    1: Movimiento(**{"id":1,
                    "fecha": '2020-12-01',
                    "valor": 50000,
                    "categoria": "Alimentos",
                    "descripcion": "Almuerzo en Leños Steak",
                    "tipo": "Gasto"}),
    2: Movimiento(**{"id":2,
                    "fecha": '2020-12-01',
                    "valor": 20000,
                    "categoria": "Transporte",
                    "descripcion": "Taxi al trabajo",
                    "tipo": "Gasto"}),
    3: Movimiento(**{"id":3,
                    "fecha": '2020-12-01',
                    "valor": 20000,
                    "categoria": "Alimentos",
                    "descripcion": "Hamburguesa",
                    "tipo": "Gasto"}),
    4: Movimiento(**{"id":4,
                    "fecha": '2020-12-02',
                    "valor": 1000000,
                    "categoria": "Salario",
                    "descripcion": "Quincena",
                    "tipo": "Ingreso"}),
    5: Movimiento(**{"id":5,
                    "fecha": '2020-12-02',
                    "valor": 6000,
                    "categoria": "Alimentos",
                    "descripcion": "Desayuno",
                    "tipo": "Gasto"}),                                                                                

}


def filtrar_por_fecha(dia_inicio: datetime.date, dia_fin: datetime.date):
    lista_movs = []
    for m in database_movs:
        if database_movs[m].fecha >= dia_inicio and database_movs[m].fecha <= dia_fin:
            lista_movs.append(database_movs[m])  
    return lista_movs


def filtrar_por_categoria (cat: str):
    lista_movs = []
    for m in database_movs:
        if database_movs[m].categoria == cat:
            lista_movs.append(database_movs[m])  
    return lista_movs


def crear_movimiento(movimiento: Movimiento):
    if movimiento.id in database_movs:
        return False
    else:
        database_movs[movimiento.id] = movimiento
<<<<<<< HEAD
        return True

#Creado Julián
def actualizar_movimiento(movimiento: Movimiento):
    if movimiento.id in database_movs:
        database_movs[movimiento.id] = movimiento
        return True
    else:
        return False
=======
        return True
>>>>>>> c4d42a415733acbbb72062c33c26c165da0142f7
