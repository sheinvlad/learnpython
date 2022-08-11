#dictionaries
dict1 = {1:'py', 2:'c'}
print(dict1)

#print value by its tag
print(dict1[1])
print(dict1[2])

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some cities
cities['NY'] = 'New York'
#overwrite CA member
cities['CA'] = 'LA'

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("CA State has: ", cities['CA'])

print(cities)

print('-' * 10)
for state, city in list(cities.items()):
    print(f"State is {state}, city is {city}")

print('-' * 10)
city = cities.get('NY')
print(city)
