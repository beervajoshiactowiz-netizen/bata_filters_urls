from pydantic import BaseModel, HttpUrl,field_validator
from typing import Optional
import re
import json

#products model
class Products(BaseModel):
    brand:str
    color:str
    size: str
    discount:str
    url:str


    #check url
    @field_validator("url", mode="before")
    @classmethod
    def url_check(cls, v):
        if v.startswith("https"):
            return v
        else:
            raise ValueError("invalid Url")
