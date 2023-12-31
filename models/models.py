from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, index=True)
    address_1 = Column(String)
    address_2 = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(Integer)
    country = Column(String)
    # owner_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="address")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    email = Column(String)
    password = Column(String)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address", back_populates="user")