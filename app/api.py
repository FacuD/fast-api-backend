from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend import Connection
from sqlalchemy.exc import ProgrammingError

class Query(BaseModel):
    select: str
    where: Optional[str] = None
    group_by: Optional[str] = None
    order_by: Optional[str] = None
    sort_by: Optional[str] = None

app = FastAPI()

@app.post("/analytics")
async def run_query(query: Query):
    try:
        return Connection().request_query(query.dict())
    except ProgrammingError as error:
        raise HTTPException(status_code = 400, detail =  error.__repr__())
