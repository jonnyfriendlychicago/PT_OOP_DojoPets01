class Ninja: 
    def __init__(self, firstNameNinja, lastNameNinja, ninjaPet, petTreats, petFood): 
        self.firstNameNinja = firstNameNinja
        self.lastNameNinja = lastNameNinja

        self.petTreats = petTreats
        self.petFood = petFood 
        
        self.ninjaPet = ninjaPet

    def acquirePet (self, petName, petType): 
        self.pet = Pet(petName, petType)
        petList = []
    
    def walk(self): 
        pass

    def feed(self):
        pass

    def bathe(self):
        pass 

class Pet:
    def __init__(self, petName, petType, petTricks, petHealth, petEnergy) -> None:
        self.petName = petName
        self.petType = petType
        self.petTricks = petTricks
        self.petHealth = petHealth
        self.petEnergy = petEnergy

    def sleep(): 
        #increases the pets energy by 25
        pass

    def eat(): 
        #increases the pet's energy by 5 & health by 10
        pass

    def play():
        #increases the pet's health by 5
        pass

    def noise():
        #prints out the pet's sound
        pass 

