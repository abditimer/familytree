from person import Person
print('Hi')
abdi = Person('abdi', '03-05-1993', '195', '100', True)
print(f'{abdi.get_name()}')
print(f'{abdi.calculate_bmi()}')
print('')

sara = Person('sara', '04-04-1943', '155', '60', False)
print(f'{sara.get_name()}')
print(f'{sara.calculate_age()}')

print('Bye')

