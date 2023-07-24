from pydantic import BaseModel

# Modelo de datos para el objeto "Registro"
class Registro(BaseModel):
    StockCode: str
    Description: str
    Quantity: int
    Price: float
    Country: str
