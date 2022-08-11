#regular variables 
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avarage_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")

#strings
name = "Jim"
car = "Golf"
print("Name is",name, "and car is", car)

#for foramtted strings
age = 35
height = 185
weight = 80
total = age + height + weight
math = 12.555
math_round = round(math)


#formatted strings
print(f"Name is {name} and car is {car}")
print(f"If I add {age}, {height} and {weight} I get {total}.")
print(f"Math is {math} and math_round is {math_round}.")

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


#More strings to print
print("Its fleece was white as {}.".format('snow'))
print("*" * 10)


end1 = "A"
end2 = "B"
end3 = "C"
end4 = "D"

print(end1 + end2) # if , end=' ' - then AB CD will be output
print(end3 + end4) # if without   - then AB "newline" CD

#Multistring print
print(""" 
We can type 
anything we want here and 
in any form we want """)


tabby_cat = "\t I'm tabbed in."
print(tabby_cat)