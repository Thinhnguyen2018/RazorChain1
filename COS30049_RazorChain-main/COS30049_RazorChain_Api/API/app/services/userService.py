import models
from schemas import UserUpdate
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: str):
    # User
    user = db.query(models.User).filter(models.User.userID == user_id).first()
    if not user:
        return None
    
    # Possession
    possession = db.query(models.Possession).filter(models.Possession.userID == user_id).first()
    user.wallet_balance = possession.wallet_balance
    
    # Wallet
    walet = db.query(models.WalletInfor).filter(models.WalletInfor.walletID == user.walletID).first()
    user.wallet_add = walet.wallet_add
    
    # Get collect
    user.can_collect_award = check_can_be_awarded(db)
    
    return user

def increase_wallet_balance(db: Session, user_id: str, points: int):
    # Retrieve the Possession object for the specified user_id
    possession = db.query(models.Possession).filter(models.Possession.userID == user_id).first()

    if possession:
        # Increment the wallet_balance by 10 units
        possession.wallet_balance += points

        # Commit the changes to the database
        db.commit()

        return True  # Indicate success
    else:
        return False  # Possession object not found for the specified user_id

def update_user(db: Session, user_id: str, user_info: UserUpdate):
    # Retrieve the user object from the database
    user = db.query(models.User).filter(models.User.userID == user_id).first()
    if user is None:
        return None  # User not found

    # Update the user information with the provided data
    for field, value in user_info.dict().items():
        setattr(user, field, value)

    # Commit the changes to the database
    db.commit()

    # Return the updated user
    return user

def check_can_be_awarded(db: Session) -> bool:
    # TODO: check_can_be_awarded
    # Query to check if UserTransaction meets the conditions
    # result = db.query(models.UserTransaction) \
    #     .join(models.UserTransaction.transaction) \
    #     .filter(models.UserTransaction.participant_typeID == '02',
    #             models.Transaction.message == 'award',
    #             models.Transaction.amount == 10) \
    #     .first()

    # return result is None
    return True