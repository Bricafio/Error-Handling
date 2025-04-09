from fastapi import HTTPException, status

class AEsMenorQueBException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El primer número no puede ser menor que el segundo"
        )

class ANumeroIgualABException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ambos números son iguales"
        )