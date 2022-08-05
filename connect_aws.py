from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, VARCHAR, Numeric
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

uri = "postgresql://codesmith:TensorFlow01?@cardata.ceq8tkxrvrbb.us-west-2.rds.amazonaws.com:5432/postgres"
engine = create_engine(uri)
Base = declarative_base()

class CarsBidsData(Base):
    __tablename__ = 'CarsBidsData'
    id_ =               Column(Integer, primary_key=True)
    Make =              Column(VARCHAR)
    Model=              Column(VARCHAR)
    Mileage=            Column(VARCHAR)
    VIN=                Column(VARCHAR)
    TitleStatus=        Column(VARCHAR)
    Location=           Column(Integer)
    Engine=             Column(VARCHAR)
    Drivetrain=         Column(VARCHAR)
    Transmission=       Column(VARCHAR)
    BodyStyle=          Column(VARCHAR)
    ExteriorColor=      Column(VARCHAR)
    InteriorColor=      Column(VARCHAR)
    Price=              Column(Numeric)
    SoldType=           Column(VARCHAR)
    NumBids=            Column(Numeric)
    Y_N_Reserve=        Column(VARCHAR)
    Year=               Column(Numeric)

# Base.metadata.create_all(engine)

