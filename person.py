# TODO: To create abstract class, i need to inherit ABC
from abc import ABC, abstractmethod

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
    set_gender(isMale)
        sets the gender of the 
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
        #isMale, isFemale = self.set_gender(isMale)
        
    def get_name(self):
        return self.name

    def set_gender(self, isMale):
        if (isMale):
            return True, False
        else:
            return False, True
    


