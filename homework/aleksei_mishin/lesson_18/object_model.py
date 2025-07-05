from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class ObjectData(BaseModel):
    color: Optional[str] = None
    size: Optional[str] = None


class RequestCreateObjectModel(BaseModel):
    name: str
    data: ObjectData


class RequestUpdateObjectModel(BaseModel):
    name: Optional[str] = None
    data: Optional[ObjectData] = None


class ResponseObjectModel(BaseModel):
    id: int
    name: str
    data: ObjectData


class ResponseObjectsList(BaseModel):
    data: List[ResponseObjectModel]
