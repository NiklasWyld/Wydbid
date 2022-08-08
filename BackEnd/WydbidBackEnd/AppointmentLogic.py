from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
import Wydbid

def appendCustomer(box):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    customers = session.query(Customer).all()

    for customer in customers:
        name = customer.firstname + ' ' + customer.lastname
        box.addItem(name, customer.id)