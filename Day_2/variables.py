import math

# Day 2: 30 Days of python programming
first_name = 'John'
last_name = 'Smith'
full_name = 'John Smith'
country = 'United States'
city = 'Kona'
age = 30
year = 2024
is_married = False
is_true = True
is_light_on = False
person_info = {
  'first_name' : 'John'
  'last_name' : 'Smith'

# Level 2 Number 1
print('first_name type: ' , type(first_name))
print('last_name type: ' , type(last_name))
print('full_name type: ' , type(full_name))
print('country type: ' , type(country))
print('city type: ' , type(city))
print('age type: ' , type(age))
print('year type: ' , type(year))
print('is_married type: ' , type(is_married))
print('is_true type: ' , type(is_true))
print('is_light_on type: ' , type(is_light_on))
print('Personal info: ' , type(person_info))

print(len(first_name))

# Level 2 Number 4
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

# Level 2 Number 5
radius = 30
area_of_circle = math.pi * pow(radius, 2)
print(area_of_circle)
circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)
r = input('Write radius: ')
area = math.pi * pow(r, 2)
print(area)

# Level 2 Number 6
first_name = input('First name: ')
last_name = input('Last name: ')
country = input('Country: ')
age = input('Age: ')
