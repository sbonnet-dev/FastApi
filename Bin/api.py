import logging

from fastapi import Depends, FastAPI, Request, Security
from fastapi.security import HTTPBearer, APIKeyHeader
from pydantic import BaseModel


X_API_KEY = APIKeyHeader(name='X-API-Key')

def check_authentication_header(x_api_key: str = Depends(X_API_KEY)):
	if x_api_key == "e47e24c3-a11e-4186-8d22-fe0ae3455343":
		return {
			"key": "e47e24c3-a11e-4186-8d22-fe0ae3455343",
			"service": "myapi"
		}
	raise HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Invalid API Key",
    )


logging.basicConfig(
    format="%(asctime)s %(process)-5d %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level="DEBUG"
)


users_db = []

class Communication(BaseModel):
    user_id: str
    status: float

token_auth_scheme = HTTPBearer() 
app = FastAPI(title="API Services", 
	swagger_ui_parameters={"defaultModelsExpandDepth": -1},
	description='Template API Services to quickly build an API in Python')

@app.get("/", tags=["Health check"],
	summary='Check status')
async def root():
    return {"status": "OK"}

@app.get("/api/v1/users", 
	tags=["Users"], 
	summary='List all current user',
    response_description='Description for the response value')
async def read_items(auth = Depends(check_authentication_header), skip: int = 0, limit: int = 10):
	#readAudioFile()
	return users_db[skip : skip + limit]

@app.post("/api/v1/users", 
	tags=["Users"], 
	summary='Not implemented',
    response_description='none')
async def create_item(item: Communication, auth = Depends(check_authentication_header)):
	return item

@app.get("/api/v1/users/{id}/man", tags=["Users"], 
	summary='Declare a new man',
    response_description='Description for the response value')
async def start(id: str, q: str | None = None, a=Depends(check_authentication_header)):
	exist_count = users_db.count({"user_id" : id})
	if exist_count == 0:
		users_db.append({"user_id" : id, "genre": "male"})
		logging.info(f"Services started.")
		return {"code": "200", "status": "enabled", "user_id" : id}
	else:
		return {"code": "200", "status": "enabled", "user_id" : id}
		
@app.get("/api/v1/users/{id}/women", tags=["Users"], 
	summary='Declare a woman',
    response_description='Description for the response value')
async def stop(id: str , q: str | None = None, a=Depends(check_authentication_header)):
	for idx, obj in enumerate(users_db):
		if obj['user_id'] == id:
			users_db.pop(idx)

	logging.info(f"Services stopped.")
	return {"code": 200, "status": "disabled", "user_id" : id}

