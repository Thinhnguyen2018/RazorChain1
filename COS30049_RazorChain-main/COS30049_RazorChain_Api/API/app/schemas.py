from pydantic import BaseModel, EmailStr
from typing import Optional, Union

class CustomResponse(BaseModel):
    status: int
    content: dict
    
class UserResponse(BaseModel):
    email: str
    phone_num: str
    userID: str
    studentID: str
    name: str
    walletID: str
    wallet_balance: int
    wallet_add: str
    can_collect_award: bool

    class Config:
        orm_mode = True
        from_orm = True
        from_attributes = True
        
class CategoryBase(BaseModel):
    asset_categoryID: str
    category_desc: str
    


class AssetResponse(BaseModel):
    assetID: str
    total_supply: int
    asset_symbol: str
    asset_categoryID: str
    asset_name: str
    category_desc: str

    class Config:
        orm_mode = True
        from_orm = True
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    studentID: Optional [str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None


