import uuid


class Events:
    def __init__(self, name, present, previous, database, triggers, protocol, properties):
        self.id = uuid.uuid4()
        self.name = name
        self.present_state = present
        self.previous_state = previous
        self.database = database
        self.triggers = triggers
        self.protocol = protocol
        self.properties = properties
