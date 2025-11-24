#%%
#Day 2 of 30 days of python programming
# snake_case variable naming convention
first_name = "Mileva"   #variable declaration and assignment
last_name = "Perisic"   # assignment operator is = and mens storing data in a variable
full_name = first_name + last_name
country = "Yugoslavia"
city = "Belgrade"
age = 125
year = 1900
is_married = False
is_true = True
is_light_on = True
person_info = {
    'first_name': first_name,
    'last_name': last_name,
    'country': country,
    'city': city,
    'age': age
}

# built-in fuctions

# print()
# len()
# type()
# int()
# float()
# str()
# complex()
# bool()
# list()
# tuple()
# set()
# dict()
# open()
# range()
# sum()
# min()
# max()
# abs()
# round()
# pow()
# help()
# dir()
# id()
# input()
# file()
# sorted()
# zip()
# enumerate()
# eval()
# chr()
# ord()
# etc. 


#%%

print(first_name, last_name, country, city, age)
first_name_to_list = list(first_name)
print(first_name_to_list)
# %%
age_to_float = float(age)
print(age_to_float)
# %%
person_info_to_list = list(person_info)
print(person_info_to_list)
# %%
type(is_married)
# %%
type(age_to_float)
# %%
len(full_name)
# %%
print(full_name)
# %%
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)
# %%
num_str = '10.6'
num_float = float(num_str)
print(num_float)

# %%
