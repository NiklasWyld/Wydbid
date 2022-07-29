from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
import Wydbid

base = declarative_base()

# ToDo: Add all classes

class Customer(base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(), nullable=False)
    lastname = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    adress = Column(String(), nullable=False)
    number = Column(String(), nullable=False)
    gender = Column(String(), nullable=False)
    birthdate = Column(String(), nullable=False)
    information = Column(String(), nullable=False)

    def __init__(self, firstname: str, lastname: str, email: str, adress: str, number: str, gender: str, birthdate: str, information: str):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.adress = adress
        self.number = number
        self.gender = gender
        self.birthdate = birthdate
        self.information = information

class Employee(base):
    __tablename__ = 'employees'

    username = Column(String(), primary_key=True, nullable=False)
    name = Column(String(), nullable=False)
    password = Column(String(), nullable=False)

    def __init__(self, username: str, name: str, password: str):
        self.username = username
        self.name = name
        self.password = password