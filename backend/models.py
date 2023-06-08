from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, List

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class CityModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    trip_ids: List = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
class UpdateUserModel(BaseModel):
    username: Optional[str] = Field(...)
    email: Optional[str] = Field(...)
    age: Optional[int] = Field(...)
    gender: Optional[str] = Field(...)
    trip_ids: Optional[List] = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class PoiModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    formatted_address: str = Field(...)
    geometry: dict = Field(...)
    icon: str = Field(...)
    name: str = Field(...)
    place_id: str = Field(...)
    rating: float = Field(...)
    url: str = Field(...)
    user_ratings_total: int = Field(...)
    city: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class TripModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    city: str = Field(...)
    poi_ids: List = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
class PoiIdListModel(BaseModel):
    poi_id_list: List = Field(...)
    
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }