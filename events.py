from typing import Any
import uuid
from entities import Entity,EntityManager

class Events:
    def __init__(self, name: str, _type: str, database: Any=None): # dThe database is expected to be any because because some objects will be stored in a list while others will be stored in a dictionary
        self.name = name
        self._type = _type
        self.id = uuid.uuid4()
        self.database = database
        
class EventsManager:
    _instance = None
    _events = {}
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def add(self, event): # The adding of the entity to the entity manager also occurs here
        self._events[event.id] = event
        ent = Entity(event.name, "event", event)
        EntityManager.add_entity(EntityManager, ent)
        
    def delete(self, event_uuid):
        if event_uuid in self._events:
            del self._events[event_uuid]