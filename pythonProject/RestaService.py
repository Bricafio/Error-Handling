from fastapi import FastAPI
from fastapi.responses import JSONResponse

from RestaController import AEsMenorQueBException, ANumeroIgualABException

app = FastAPI()

@app.get("/resta/{a}/{b}")
def restar(a: int, b: int):
    if a < b:
        raise AEsMenorQueBException()
    if a == b:
        raise ANumeroIgualABException()

    resultado = a - b
    return JSONResponse(content={"resultado": resultado})