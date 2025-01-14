from peewee import *
from .base_model import BaseModel

class Species(BaseModel):
    species_id = CharField()
    hp_multiplier = DoubleField()
    strength_multiplier = DoubleField()
    forage_multiplier = DoubleField()
