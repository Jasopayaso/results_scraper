from sqlalchemy import Column, Boolean, Integer, String, UniqueConstraint, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func

Base = declarative_base()

class Results(Base):
    __tablename__ = 'Results'
    id = Column(Integer, primary_key = True)
    date: Column(String(100))
    home_team: Column(String(100))
    home_score: Column(Integer, nullable = False, default = 0)
    away_team: Column(String(100))
    away_score: Column(Integer, nullable = False, default = 0)
    winner: Column(String(100), nullable = False, default = 'Draw')
    game_id: Column(Integer)