from pydantic import BaseModel
from enum import Enum

class Languages(str, Enum):
    javascript = "javascript"
    pascal = "pascal"
    c_plus_plus = "c++"
    java = "java"
    c_sharp = "c#"
    c = "c"

class Programmer(BaseModel):
    id: int
    name: str
    languages: list[Languages]
