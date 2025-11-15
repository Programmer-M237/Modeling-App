class Entity:
    def __init__(self, name: str, type: str, object):
        self.name = name
        self.type = type
        self.object = object

class EntityManager:
    _instance = None
    _items = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def add_entity(self, entity: Entity) -> bool:
        key = (entity.name, entity.type)
        if key in self._items:
            print(f"Duplicates entity blocked: {key}")
            return False
        self._items[key] = entity.object
        print(self._items)
        return True
    
    def get_all_entities(self) -> list[Entity]:
        return list(self._items.values())

    def name_exists_with_different_type(self, name: str, type: str) -> bool:
        for (name_, type_) in self._items.keys():
            if name == name_ and type_ != type:
                return True
        return False