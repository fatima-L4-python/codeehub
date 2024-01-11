# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'dog',
    'name': 'Jack jack',
    'owner': 'Paul',
    'weight': 43,
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'Dobby',
    'owner': 'Zayn',
    'weight': 2,
}

pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Ash',
    'owner': 'Niall',
    'weight': 37,
}

pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")