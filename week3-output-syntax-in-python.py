# create some varriables
name = "Jack"
age = 25
cash = 27.10

#seperate with commas
print("name:", name, ", age:", age, ", cash:", cash)

# us the "f-string" style -- variables directly using curly braces
print(f"Name: {name}, Age: {age}, Cash: {cash}")

#use format style
print("Name: {}, Age: {}, Cash ${:,.2f}".format(name, age, cash))