#lists1

hairs   = ['brown','blonde', 'red']
eyes    = ['blue', 'grey', 'hollow']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits    = ['apple', 'orange', 'pear', 'banana']
change    = [1, 'pennies', 2, 'dimes', 3, 'quaters']

for number in the_count:
    print(f"This is count {number}")

print("\n")
    
for fruit in fruits:
    print(f"This is a {fruit}")

print("\n")

for i in change:
    print(f"This is change {i}")

print("\n")

#empty list 
elements = []

#use range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list of elements")
    elements.append(i)

print("\n")

for i in elements:
    print(f"element is {i}")


    