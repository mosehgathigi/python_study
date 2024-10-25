person = {
    'name' : 'Moses',
    'age' : 27,
    'location' : ['Kiambu',518,'Thika'],
    'gender' : 'male',
    'address' : {
        'street' : 'Muthaiga',
        'city' : 'Nairobi',
        'country' : 'Kenya'
    },
}
# type
print(type(person))

# age
print(person['age'])
# gender
print(person['gender'])

# Thika
print(person['location'][2])

# kenya
print(person['address']['country'])
# muthaiga
print(person['address']['street'])
# nairobi
print(person['address']['city'])

person['address']['city'] =  'Mombasa'
print(person['address']['city'])

# location to Kangemi, 530, nairobi
person['location'] = ['Kangemi', 530, 'Nairobi']
print(person['location'])

person['occupation'] = 'Software Engineer'
print(person)
print(person.keys())

# values
print(person.values())
# items
print(person.items())
# pop
print(person.pop('occupation'))
print(person)
# .get kenya
print(person.get('country'))
