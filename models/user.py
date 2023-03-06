from pydantic import BaseModel



class User(BaseModel):

    idno:int
    name:str
    password: str
