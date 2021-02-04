from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST
from starlette.responses import RedirectResponse, JSONResponse


API_KEY = "1234567asdfgh"
api_key_query = APIKeyQuery(name='api_key', auto_error=False)
app = FastAPI()


class Production(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


app = FastAPI()


@app.get("/productions/")
async def create_production(production: Production, api_key:str=Security(api_key_query)):
    if api_key == API_KEY:
        try:
            production_dict = production.dict()
        except:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, detail="Could not parse payload content"
            )
        if production.price:
            total_price = production.price * production.quantity
            result = {"name": production.name, "total_price": total_price}
        return result
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    