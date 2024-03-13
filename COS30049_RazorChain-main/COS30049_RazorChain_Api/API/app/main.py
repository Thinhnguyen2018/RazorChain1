from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import schemas
from services import userService, assetService
from database import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RazorChain Api") 

# List of allowed origins (replace "*" with your specific origins)
allowed_origins = [
    "http://localhost",
    "http://localhost:3000",  # Example frontend URL
]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,  # Allow cookies
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allow specified HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/users/{userId}", response_model=schemas.CustomResponse)
def read_user(userId: str, db: Session = Depends(get_db)):
    user = userService.get_user(db, user_id=userId)
    if user is None:
        return schemas.CustomResponse(
            status=404,
            content={
                  "message": "User not found",
            }
        ).dict()
    
    return schemas.CustomResponse(
        status=200,
        content={
            "message": "Success",
            "userID": userId,
            "userDetail": schemas.UserResponse.from_orm(user)
        }
    ).dict()


@app.get("/assets", response_model=schemas.CustomResponse)
def read_assets(db: Session = Depends(get_db)):
    assets = assetService.get_assets(db)
    if assets is None:
        return schemas.CustomResponse(
            status=400,
            content={
                "message": "Something went wrong",
            }
        )
    
    # Convert each ORM object to a Pydantic model individually
    asset_responses = []
    for asset in assets:
        asset_dict = asset.__dict__
        asset_dict['category_desc'] = asset.asset_category.category_desc
        asset_responses.append(schemas.AssetResponse(**asset_dict))
    
    return schemas.CustomResponse(
        status=200,
        content={
            "message": "Success",
            "data": [asset.dict() for asset in asset_responses]
        }
    )

@app.post("/collect-award", response_model=schemas.CustomResponse)
def collect_award(db: Session = Depends(get_db)):
    res = userService.increase_wallet_balance(db,  '1', 10)
    if res is False:
        return schemas.CustomResponse(
            status=400,
            content={
                  "message": "Something went wrong",
            }
        ).dict()
    
    user = userService.get_user(db, user_id='1')
    return schemas.CustomResponse(
        status=200,
       content={
            "message": "Success",
            "userID": '1',
            "userDetail": schemas.UserResponse.from_orm(user)
        }
    ).dict()


@app.put("/users/{userId}/update", response_model=schemas.CustomResponse)
def update_user(userId: str, payload: schemas.UserUpdate, db: Session = Depends(get_db)):
   # Check if the user exists
    user = userService.get_user(db, user_id=userId)
    if user is None:
        return schemas.CustomResponse(
            status=404,
            content={
                  "message": "User not found",
            }
        ).dict()

    # Update the user information
    updated_user = userService.update_user(db, user_id=userId, user_info=payload)
    
    if updated_user is None:
        return schemas.CustomResponse(
            status=400,
            content={
                  "message": "Something went wrong",
            }
        ).dict()
    
    user = userService.get_user(db, user_id=userId)
    return schemas.CustomResponse(
        status=200,
       content={
            "message": "Success",
            "userID": userId,
            "userDetail": schemas.UserResponse.from_orm(user)
        }
    ).dict()
