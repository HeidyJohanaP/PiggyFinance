from fastapi import FastAPI
from fastapi import HTTPException
import datetime
import db.movimientos_db
from db.movimientos_db import database_movs

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenido a Piggy Grow"}

@app.get("/mov")
async def movimientos():
    return database_movs

@app.get("/mov/{id}")
async def movimientos_por_id(id: int):
    if id in database_movs:
        #return {"message": database_movs[id]}
        return database_movs[id]    
    raise HTTPException(status_code = 404, detail = "No se registra el movimiento.")


#http://127.0.0.1:8000/categoria?categoria=Alimentos
@app.get("/categoria")
async def movimientos_por_categoria(categoria: str):
    return db.movimientos_db.filtrar_por_categoria(categoria)    


#http://127.0.0.1:8000/fecha?dia_inicio=2020-12-01&dia_fin=2020-12-01
@app.get("/fecha")
async def movimientos_por_dia(dia_inicio: datetime.date, dia_fin: datetime.date):
    return db.movimientos_db.filtrar_por_fecha(dia_inicio, dia_fin)


@app.post("/mov/nuevo")
async def crear_movimiento(movimiento: db.movimientos_db.Movimiento):
    orden_creada = db.movimientos_db.crear_movimiento(movimiento)
    if orden_creada:
        return {"message" : "Movimiento creado exitosamente."}
    else:
        raise HTTPException(status_code=400, detail="Ya existe un movimiento con el ID especificado.")

#Tarea Julián
@app.put("/mov/actualizar")
async def actualizar_movimiento(movimiento: db.movimientos_db.Movimiento):
    orden_actualizada = db.movimientos_db.actualizar_movimiento(movimiento)
    if orden_actualizada: 
        return {"message" : "Movimiento actualizado exitosamente."}
    else:
        raise HTTPException(status_code=400, detail="No existe un movimiento con el ID especificado.")