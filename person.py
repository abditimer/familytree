# TODO: To create abstract class, i need to inherit ABC
from abc import ABC, abstractmethod
from datetime import datetime

class Person:
    """
    An abstract class used to represent a person in a family

    ...

    Attributes
    ----------
    name : str
        The name of the family member
    dob : str
        The DOB of the family member, in dd-mm-YYYY format
    height : float
        height of an individual in cm
    weight : float
        weight of an individual in kg
    isMale : boolean
        True if male, False if female
    isFemale : boolean
        True if female, False if male

    Methods
    -------
    calculate_age()
        calculates the age of a person
    calculate_relationship()
        calculates the relationship to another person
    calculate_BMI()
        calculates BMI
    
    """
    def __init__(self, name, dob, height, weight, isMale):
        self.name = name
        self.dob = dob
        self.height = height
        self.weight = weight
        self.isMale, self.isFemale = self.set_gender(isMale)
        
    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_height(self, inMetres):
        if inMetres:
            return int(self.height) / 100
        else:
            return int(self.height)
    
    def get_weight(self):
        return int(self.weight)

    def get_gender(self):
        # If person is Male
        if self.isMale:
            return 'Male'
        else:
            return 'Female'

    def print_gender(self):
        return f'{self.get_name()} is a {self.get_gender()}'

    def set_gender(self, isMale):
        if (isMale):
            return True, False
        else:
            return False, True

    def calculate_age(self):
        
        dob = datetime.strptime(self.get_dob(), '%d-%m-%Y')
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
    
    def calculate_bmi(self):
        # bmi = W / H ** 2
        return round((self.get_weight() / (self.get_height(True) ** 2)), 1)

    def __str__(self):
        return (
            f'Hi, my name is {self.get_name()}. '\
            f'I am {self.calculate_age()} years old, '\
            f'born on {self.get_dob()}.'
        )
                

    


