from sqlalchemy import Column,  String, create_engine, Integer, text, inspect
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
Base = declarative_base()
from datetime import date

class CarsAndBidsTable(Base):
    __tablename__ = 'cars_bids_listings'
    id = Column(Integer(), primary_key=True) 
    make  = Column(String())
    model  = Column(String())
    mileage  = Column(String())
    vin  = Column(String())
    status  = Column(String())
    location = Column(String())
    engine  = Column(String())
    drivetrain  = Column(String())
    transmission  = Column(String())
    bodystyle = Column(String())
    exteriorcolor = Column(String())
    interiorcolor = Column(String())
    price = Column(String())
    soldtype = Column(String())
    numbids = Column(String())
    y_n_reserve = Column(String())
    year = Column(String())
    date = Column(String())
    url = Column(String())
    
class VinAuditTable(Base):
    __tablename__ = 'vin_audit_data'
    id = Column(Integer(), primary_key=True)    
    vin = Column(String())
    market_value_mean = Column(String())
    market_value_std = Column(String())
    count = Column(String())
    count_over_days = Column(String())

class ModelsScore(Base):
    __tablename__ = 'models_score'
    id = Column(Integer(), primary_key=True)    
    path = Column(String())
    test_score = Column(String())
    environment = Column(String())

