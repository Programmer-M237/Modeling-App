from entities import Entity,EntityManager

class ObjectsManager:
    _instance = None
    _objects = {}
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def add(self, object): # The adding of the entity to the entity manager also occurs here
        self._objects[object.id] = object
        ent = Entity(object.name, "object", object)
        EntityManager.add_entity(EntityManager, ent)
        
    def delete(self, object_uuid):
        if object_uuid in self._objects:
            del self._objects[object_uuid]