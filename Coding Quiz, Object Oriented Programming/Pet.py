class Pet:
    species_lifespans = {
        "dog": 13,  
        "cat": 15,
        "hamster": 3,
        "parrot": 50,
        "rabbit": 10,
        "turtle": 50,
        "fish": 5
    }
    
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def age_in_human_years(self):
        # A rough estimate for converting pet years to human years
        if self.species.lower() == "dog":
            return self.age * 7
        elif self.species.lower() == "cat":
            return self.age * 7
        elif self.species.lower() == "hamster":
            return self.age * 4
        elif self.species.lower() == "parrot":
            return self.age * 2
        elif self.species.lower() == "rabbit":
            return self.age * 6
        elif self.species.lower() == "turtle":
            return self.age * 1
        elif self.species.lower() == "fish":
            return self.age * 3
        else:
            return "Species not recognized"

    @classmethod
    def average_lifespan(cls, species):
        return cls.species_lifespans.get(species.lower(), "Species not recognized")

    def display_info(self):
        human_years = self.age_in_human_years()
        lifespan = self.average_lifespan(self.species)
        return (f"Pet Name: {self.name}, Age: {self.age} years, "
                f"Species: {self.species}, Age in Human Years: {human_years}, "
                f"Average Lifespan for Species: {lifespan} years")

# Instantiate several Pet objects with different names, ages, and species
pet1 = Pet("Buddy", 5, "dog")
pet2 = Pet("Whiskers", 3, "cat")
pet3 = Pet("Squeaky", 2, "hamster")

# Print the information for each pet
print(pet1.display_info())
print(pet2.display_info())
print(pet3.display_info())
