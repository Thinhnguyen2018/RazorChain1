from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "user"

    userID = Column(String, primary_key=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    studentID = Column(String)
    phone_num = Column(String)
    walletID = Column(String)


    possession: Mapped["Possession"] = relationship(back_populates="user")
    wallet: Mapped["WalletInfor"] = relationship(back_populates="user")
    transactions: Mapped["UserTransaction"] = relationship(back_populates="user")


class Possession(Base):
    __tablename__ = "userpossession"

    walletID = Column(String, primary_key=True)
    userID = Column(String, ForeignKey("user.userID"), primary_key=True)
    assetID = Column(String)
    wallet_balance = Column(Integer)

    user: Mapped["User"] = relationship(back_populates="possession")


class WalletInfor(Base):
    __tablename__ = "walletinfor"

    walletID = Column(String, ForeignKey("user.walletID"), primary_key=True)
    wallet_add = Column(String)
    
    user: Mapped["User"] = relationship(back_populates="wallet")


class Asset(Base):
    __tablename__ = "asset"

    assetID = Column(String, primary_key=True)
    asset_categoryID = Column(String, ForeignKey("asset_category.asset_categoryID"))
    asset_name = Column(String)
    total_supply = Column(Integer)
    asset_symbol = Column(String)
    
    asset_category = relationship("AssetCategory", back_populates="assets")


class AssetCategory(Base):
    __tablename__ = "asset_category"

    asset_categoryID = Column(String, primary_key=True)
    category_desc = Column(String)
    
    assets = relationship("Asset", back_populates="asset_category")


class Transaction(Base):
    __tablename__ = "transaction"
    
    transactionID = Column(String, primary_key=True)
    
    # Define custom default value for transactionID
    def generate_transaction_id(context):
        db_session = context.get_bind()
        max_id = db_session.execute("SELECT MAX(transactionID) FROM transaction").scalar()
        if max_id is None:
            return "txn001"  # Start with txn001 if no records exist
        else:
            prefix = max_id[:3]  # Extract prefix (e.g., "txn")
            next_id = int(max_id[3:]) + 1  # Extract numerical part and increment
            return f"{prefix}{next_id:03d}"  # Format next_id with leading zeros
    
    transactionID.default = generate_transaction_id

    assetID = Column(String)
    amount = Column(Integer)
    message = Column(String)
    transaction_hash = Column(String)
    status = Column(String)
    block_num = Column(String)
    timestamp = Column(DateTime, default=datetime.now)

    userTransaction: Mapped["UserTransaction"] = relationship(back_populates="transaction")

class ParticipantType(Base):
    __tablename__ = "participanttype"

    participant_typeID = Column(String, primary_key=True)
    participant_desc = Column(String)



class UserTransaction(Base):
    __tablename__ = "usertransaction"

    userID = Column(String, ForeignKey("user.userID"), primary_key=True)
    transactionID = Column(String, ForeignKey("transaction.transactionID"), primary_key=True)
    participant_typeID = Column(String)

    # Relationships
    user = relationship("User", back_populates="transactions")
    transaction = relationship("Transaction", back_populates="userTransaction")
    

