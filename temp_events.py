### This singleton will be used to store events data temporarily before they are being moved to the events singleton 

from typing import Any
import uuid
from entities import Entity,EntityManager

class Events:
    def __init__(self, name: str, database: Any=None): # dThe database is expected to be any because because some objects will be stored in a list while others will be stored in a dictionary
        self.name = name
        self.database = database
        
    def set_database(self, database: Any):
        self.database = database