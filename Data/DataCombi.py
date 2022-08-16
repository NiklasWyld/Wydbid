from PyQt5.QtCore import QDate, QTime
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float
from sqlalchemy.orm import declarative_base
import Wydbid

# ToDo: Add all classes

base = declarative_base()

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

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    password = Column(String(), nullable=False)

    def __init__(self, username: str, name: str, password: str):
        self.username = username
        self.name = name
        self.password = password

class News(base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(), nullable=False)
    description = Column(String(), nullable=False)

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

class Appointment(base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    date = Column(String(), nullable=False)
    time = Column(String(), nullable=False)
    customer_id = Column(Integer, nullable=False)
    appeared = Column(Boolean)
    closed = Column(Boolean)

    def __init__(self, title: str, description: str, date: str, time: str, customer_id: int):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.customer_id = customer_id
        self.appeared = bool(False)
        self.closed = bool(False)

class Order(base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    price = Column(String(), nullable=False)
    customer_id = Column(Integer, nullable=False)
    closed = Column(Boolean)

    def __init__(self, title: str, description: str, price: str, customer_id: int):
        self.title = title
        self.description = description
        self.price = price
        self.customer_id = customer_id
        self.closed = bool(False)