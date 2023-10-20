class animal:
    '''
    Essa classe é a base para todos os animais
    '''
    def __init__(self, name, species):
        '''
        Construtor da classe animal

        Args:
            name: str
                The name of the animal
            species: str
                The species of the animal
        '''
        self.name = name
        self.species = species

    def speak(self):
        '''
        Make the animal speak

        Returns:
            str: A message representing the animal's speach
        '''
        return f"{self.name} says Hi!"

    def __str__(self):
        '''
        String representing the animal

        Returns:
            str: A string with the animal's name and species
        '''
        return f'{self.name} {self.species}'
    
class dog(animal):
    '''
    Essa classe representa um cahcorro, ela é herdada da classe animal
    '''
    def __init__(self, name, breed):
        '''
        Construtor da classe cachorro

        Args:
            breed: str
                The breed of the dog
        '''
        super().__init__(name, species = "Dog")
        self.breed = breed
    
    def speak(self):
        '''
        Make the dog bark.

        Returns:
            str: A message representing the dog's speach
        '''
        return f'{self.name} barks, woof!'
    
    def wag_tail(self):
        '''
        Make the dog wag its tail.

        Returns:
            str: A message representing the dog wagging its tail
        '''
        return f'{self.name} wags its tail'

# create instance of Dog and Cat classes
my_dog = dog("Chun li", "French Bulldog")

#Call methods to demonstrate funcionality
print(my_dog.speak())
print(my_dog.wag_tail())

#Display information about the animal
print(my_dog)

    



    