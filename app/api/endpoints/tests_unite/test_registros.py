import pytest
from httpx import AsyncClient
from app.api.endpoints.registros import router
from app.api.models.registro import Registro

# Prueba unitaria para el método GET
@pytest.mark.asyncio
async def test_read_registro():
    registro_id = 4
    async with AsyncClient(app=router.app, base_url="http://test") as client:
        response = await client.get(f"/registros/{registro_id}")
    assert response.status_code == 200
    assert "id" in response.json()
    assert "StockCode" in response.json()
    assert "Description" in response.json()
    assert "Quantity" in response.json()
    assert "Price" in response.json()
    assert "Country" in response.json()

# Prueba unitaria para el método DELETE
# Creamos una función de ayuda para hacer una solicitud DELETE a la API
async def delete_registro(client: AsyncClient, registro_id: int):
    response = await client.delete(f"/registros/{registro_id}")
    return response

# Aplicar prueba unitaria para el método DELETE
@pytest.mark.asyncio
async def test_delete_registro():
    registro_id = 4 # Este registro si existe en la base de datos

    async with AsyncClient(app=router) as client:
        # Hacer la solicitud DELETE para eliminar el registro con ID 4
        response = await delete_registro(client, registro_id)

        # Verificar que la solicitud haya tenido éxito (código de estado 200 a 299)
        assert response.status_code in range(200, 300)

        # Verificar que la respuesta contenga el mensaje de éxito
        assert response.json() == {"message": "Registro eliminado con éxito"}

# Prueba unitaria para el método POST
# Función de ayuda para hacer una solicitud POST a la API
async def create_registro(client: AsyncClient, registro_data: dict):
    response = await client.post("/registros/", json=registro_data)
    return response

# Aplicar la prueba unitaria para el método POST create_registro
@pytest.mark.asyncio
async def test_create_registro():
    # Datos de prueba para el nuevo registro
    nuevo_registro_data = {
        "StockCode": "12345",
        "Description": "Registro Prueba Unitaria",
        "Quantity": 10,
        "Price": 19.99,
        "Country": "USA",
    }

    async with AsyncClient(app=router) as client:
        # Solicitud POST para crear el nuevo registro
        response = await create_registro(client, nuevo_registro_data)

        # Verificar que la solicitud haya tenido éxito (código de estado 200 a 299)
        assert response.status_code in range(200, 300)

        # Verificar que la respuesta contiene la información del nuevo registro
        registro_nuevo = response.json()
        assert "id" in registro_nuevo
        assert registro_nuevo["StockCode"] == nuevo_registro_data["StockCode"]
        assert registro_nuevo["Description"] == nuevo_registro_data["Description"]
        assert registro_nuevo["Quantity"] == nuevo_registro_data["Quantity"]
        assert registro_nuevo["Price"] == nuevo_registro_data["Price"]
        assert registro_nuevo["Country"] == nuevo_registro_data["Country"]