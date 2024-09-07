class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        if owner:
            owner.add_pet(self)

    def __str__(self):
        return f"{self.name} the {self.pet_type}"


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of Pet.")
        pet.owner = self
        if pet not in self.pets_list:
            self.pets_list.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)
