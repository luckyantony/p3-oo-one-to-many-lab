class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}")
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all.append(self)
        
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class")
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class")
        pet.owner = self
        if pet not in self._pets:
            self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)