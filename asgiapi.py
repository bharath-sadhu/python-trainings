from fastapi import FastAPI, status, HTTPException, Header, Depends
from typing import List, Optional
from pydantic import BaseModel

class inputPayload(BaseModel):
    company:str
    class Config:
        orm_mode = False

class outputPayload(BaseModel):
     returnResponse: str
     class Config:
          orm_mode = False

app = FastAPI(docs_url="/documentation")

companies=["Cloudwick", "Apple"]

@app.get("/home")
async def healthcheck():
     return "OK"

@app.get("/home/failure")
async def healthcheckFailure():
     return HTTPException(status_code=403, detail="")

@app.post("/home/register")
async def registerCompany(payload: inputPayload):
     companies.append(payload.company)
     return "Succesfully added"

@app.get("/home/verify/{company}")
async def getCOmpany(company: str):
     if company.lower() in (company.lower() for company in companies):
          return "Valid one"
     return HTTPException(status_code=400, detail="Not valid")


@app.get("/home/verify")
async def getCOmpanyAsQuery(company: str):
     if company.lower() in (company.lower() for company in companies):
          return "Valid one"
     return HTTPException(status_code=400, detail="Not valid")


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons