import uuid
import systems


class Object:
    def __init__(self):
        self.name: str
        self.type = "object"
        self.object_type_id: str
        self.id = uuid.uuid4()
        

class Id01(Object):
    def __init__(self, name, number_of_forms, number_of_properties, properties, forms, repetition_allowed):
        super().__init__()
        self.name = name
        self.object_type_id = "01"
        self.number_of_forms = number_of_forms
        self.number_of_properties = number_of_properties
        self.properties = properties
        self.repetition_allowed = repetition_allowed
        
        # Each position has the same radix (number_of_forms)
        self.intrinsic_number_systems = [number_of_forms] * number_of_properties
        self.number_of_elements = pow(number_of_forms, number_of_properties)
        self.system = systems.system_01(self.number_of_elements, self.intrinsic_number_systems, forms, repetition_allowed)
        # print(self.id)
