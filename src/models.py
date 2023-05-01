import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    population = Column(Integer)
    gravity = Column(String(40))
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    edited = Column(Date)
    created = Column(Date)
    url = Column(String(100), unique = True)

    def to_dict(self):
        return {}

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    birth_year = Column(Date)
    eye_color = Column(String(20))
    gender = Column(String(10))
    hair_color = Column(String(20))
    height = Column(Integer)
    mass = Column(Integer)
    skin_color = Column(String(30))
    edited = Column(Date)
    created = Column(Date)
    origin_planet_url = Column(String(100), ForeignKey('planet.url'))
    url = Column(String(100), unique = True)

    def to_dict(self):
        return {}
    
class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    person_id = Column(Integer, ForeignKey('person.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
