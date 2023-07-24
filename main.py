from fastapi import FastAPI
from fastapi.routing import APIRouter

from app.api.endpoints import registros

app = FastAPI()

# Routers de los endpoints
app.include_router(registros.router, prefix="/registros", tags=["registros"])

# 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
