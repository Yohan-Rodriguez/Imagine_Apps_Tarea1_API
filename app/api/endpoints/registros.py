from fastapi import APIRouter, HTTPException
from supabase_py import create_client
import httpx
from ..models.registro import Registro
from ...db.database import get_supabase_client


router = APIRouter()

# Credenciales de tu proyecto en Supabase
SUPABASE_URL = "https://ndkclxyzvcgqrhzxzouv.supabase.co" 
SUPABASE_API_KEY = "tu_api_key_de_supabase"  
SUPABASE_HEADERS = {"apikey": SUPABASE_API_KEY}

# Obtener el cliente de Supabase
supabase = get_supabase_client()
   
# Implementa las operaciones CRUD:
# Método POST para crear un nuevo registro
@router.post("/registros/", response_model=Registro)
async def create_registro(registro: Registro):
    try:
        # Realizar una solicitud autenticada a la API de Supabase para crear el nuevo registro
        response = supabase.table("online_retail_II").insert(registro.dict()).execute()

        # Estado de la respuesta del servidor
        status_code = response["status_code"]

        if status_code in range(200, 300):
            registro_nuevo = response['data'][0] 
            return registro_nuevo

        else:
            # Si el código de estado no está en el rango 200 a 299, mostramos la respuesta del servidor
            raise HTTPException(status_code=status_code, detail=response["data"])

    except HTTPException as http_exc:
        # Capturar y reenviar excepción HTTP si es generada por FastAPI
        raise http_exc

    except Exception as e:
        # Mostrar detalles adicionales de la respuesta del servidor en caso de cualquier otra excepción
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")    

# Método Get
@router.get("/registros/{registro_id}", response_model=Registro)
async def read_registro(registro_id: int):
    try:
        # Convertir el ID a una cadena
        registro_id_str = str(registro_id)

        # Realizar una solicitud autenticada a la API de Supabase
        response = supabase.table("online_retail_II").select("*").eq("id", registro_id_str).execute()

        if response["status_code"] == 200 and len(response["data"]) > 0:
            # Devolver el primer registro encontrado
            return response["data"][0]
        else:
            raise HTTPException(status_code=404, detail="Registro not found")

    except httpx.HTTPError as http_err:
        # Manejar errores de HTTP, como problemas de conexión, etc.
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {http_err}")

    except Exception as e:
        # Manejar excepciones adicionales
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

# Método PUT para actualizar un registro por su ID
@router.put("/registros/{registro_id}", response_model=Registro)
async def update_registro(registro_id: int, registro: Registro):
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{SUPABASE_URL}/rest/v1/online_retail_II/{registro_id}",
            headers=SUPABASE_HEADERS,
            json=registro.dict(), 
        )
        print(response)      
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)   
    
    else:
        return response.json()


# Método Delete
@router.delete("/registros/{registro_id}", response_model=dict)
async def delete_registro(registro_id: int):
    try:
        # Convertir el ID a una cadena
        registro_id_str = str(registro_id)

        # Realizar una solicitud autenticada a la API de Supabase para eliminar el registro
        response = supabase.table("online_retail_II").delete().eq("id", registro_id_str).execute()

        if response["status_code"] in range(200, 300):
            # Verificar si la respuesta tiene contenido
            if response["data"]:
                return {"message": "Registro eliminado con éxito"}
            else:
                return {"message": "Registro no encontrado"}

        else:
            raise HTTPException(status_code=404, detail="Registro not found")

    except httpx.HTTPError as http_err:
        # Manejar errores de HTTP, como problemas de conexión, etc.
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {http_err}")

    except Exception as e:
        # Manejar otras excepciones
        raise HTTPException(status_code=500, detail=f"Response: Registro ya no existe en la base de datos")
    