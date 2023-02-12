from typing import List,Generic, Optional,TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class BookSchema(BaseModel):
    id:Optional[int]=None
    title:Optional[str]=None
    description:Optional[str]=None

    class config:
        orm_mode=True

class RequestBook(BaseModel):
    parameter:BookSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code:str
    status:str
    message:str
    result:Optional[T]


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

