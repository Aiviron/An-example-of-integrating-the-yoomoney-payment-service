from pydantic import BaseModel
from datetime import datetime

class TariffModel(BaseModel):
    id:          int       # int8    -> int
    title:       str       # varchar -> str
    description: str       # text    -> str
    price:       int       # int8    -> int (цены в копейках, храним в int)
    currency:    str       # varchar -> str