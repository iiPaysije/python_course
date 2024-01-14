# Example of list comprehensions and why it is usefull

temps = [221, 331, 443, 556]

# ----------------------------------
# using for loops, EXAMPLE 1

temps_as_float = []

for temp in temps:
    temps_as_float.append(temp / 10)

print(temps_as_float, 'using loops')

# ----------------------------------
#using comprehensions, EXAMPLE 2

new_temps = [temp / 10 for temp in temps]
print(new_temps, 'using list comprehensions')

# ----------------------------------
# using if with comprehensions

new_temps = [temp / 10 for temp in  temps if temp > 0]
print(new_temps, 'with if conditional')

# ----------------------------------
#using if else with comprehension
# [value if value-conditional elese other_value for value in list]
new_temp = [temp / 10 if temp > 0 else 0 for temp in temps]
print(new_temp, 'with if else conditional')