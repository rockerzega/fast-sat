from pydantic import BaseModel
from typing import Optional

class DataClient(BaseModel):
  fechaInicio: str
  fechaFin: str
  certificate: Optional[str]
  key: Optional[str]
  password: Optional[str]
  instance: str

class Certificate(BaseModel):
  certificate: str
  key: str
  password: str
  instance: str

class DateFind(BaseModel):
  fechaInicio: str
  fechaFin: str
