class Entity:
    """
    Singleton entity registry for storing all entities (objects, events, functional objects).
    All instances share the same registry, ensuring a single source of truth.
    """
    _instance = None
    entities = {}

    def __new__(cls):
        """Enforce singleton pattern - only one instance exists."""
        if cls._instance is None:
            cls._instance = super(Entity, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the singleton (called each time, but instance is reused)."""
        pass

    def add_entity(self, name: str, type: str, obj) -> None:
        """
        Add an entity to the global registry.
        
        Args:
            name: The name/identifier of the entity
            type: The type (e.g., 'Object', 'Event', 'FunctionalObject')
            obj: The entity object to store
            
        Raises:
            ValueError: If name or type is empty
        """
        if not name or not name.strip():
            raise ValueError("Entity name cannot be empty")
        if not type or not type.strip():
            raise ValueError("Entity type cannot be empty")
        
        key = (name.strip(), type.strip())
        
        if key in self.entities:
            print(f"Warning: Overwriting existing entity '{name}' of type '{type}'")
        
        self.entities[key] = obj

    def delete_entity(self, name: str, type: str) -> bool:
        """
        Delete an entity from the global registry.
        
        Args:
            name: The name of the entity to delete
            type: The type of the entity to delete
            
        Returns:
            bool: True if entity was deleted, False if not found
        """
        key = (name.strip() if name else "", type.strip() if type else "")
        
        if key in self.entities:
            del self.entities[key]
            return True
        return False

    def get_entity(self, name: str, type: str):
        """
        Retrieve an entity from the registry.
        
        Args:
            name: The name of the entity
            type: The type of the entity
            
        Returns:
            The entity object if found, None otherwise
        """
        key = (name.strip() if name else "", type.strip() if type else "")
        return self.entities.get(key)

    def entity_exists(self, name: str, type: str) -> bool:
        """
        Check if an entity exists in the registry.
        
        Args:
            name: The name of the entity
            type: The type of the entity
            
        Returns:
            bool: True if entity exists, False otherwise
        """
        key = (name.strip() if name else "", type.strip() if type else "")
        return key in self.entities

    def get_entities_by_type(self, type: str) -> dict:
        """
        Get all entities of a specific type.
        
        Args:
            type: The type to filter by (e.g., 'Object', 'Event', 'FunctionalObject')
            
        Returns:
            dict: Dictionary of entities matching the type {(name, type): obj}
        """
        type = type.strip() if type else ""
        return {k: v for k, v in self.entities.items() if k[1] == type}

    def get_entities_by_name(self, name: str) -> dict:
        """
        Get all entities with a specific name (regardless of type).
        
        Args:
            name: The name to filter by
            
        Returns:
            dict: Dictionary of entities matching the name
        """
        name = name.strip() if name else ""
        return {k: v for k, v in self.entities.items() if k[0] == name}

    def get_all_entities(self) -> dict:
        """
        Get all entities in the registry.
        
        Returns:
            dict: Copy of the entities dictionary
        """
        return self.entities.copy()

    def get_all_types(self) -> set:
        """
        Get all unique entity types currently registered.
        
        Returns:
            set: Set of all entity types
        """
        return {k[1] for k in self.entities.keys()}

    def clear_all_entities(self) -> None:
        """Clear all entities from the global registry."""
        self.entities.clear()

    def count_entities(self, type: str = None) -> int:
        """
        Get the number of entities, optionally filtered by type.
        
        Args:
            type: Optional type to filter by
            
        Returns:
            int: Number of entities (total or of specific type)
        """
        if type is None:
            return len(self.entities)
        return len(self.get_entities_by_type(type))

    @classmethod
    def reset_singleton(cls) -> None:
        """
        Reset the singleton instance and clear all entities.
        Use with caution - mainly for testing purposes.
        """
        cls.entities = {}
        cls._instance = None

    def __repr__(self) -> str:
        """String representation of the entity registry."""
        return f"<Entity Registry: {len(self.entities)} entities, {len(self.get_all_types())} types>"