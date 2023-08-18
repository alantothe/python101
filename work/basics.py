import random

# Starting with the following list...
planeteers = ["Earth", "Wind", "Captain Planet", "Fire", "Water"]

# Access the second value in `planeteers`

print(planeteers[1])


# Add "Heart" to the end of `planeteers`

planeteers.append("Heart")

print(planeteers)

# Remove "Captain Planet" from the list

planeteers.remove("Captain Planet")

print(planeteers)

# Combine `planeteers` with `rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]` and save the result in a variable called `heroes`

range = ["Red", "Blue", "Pink", "Yellow", "Black"]

heroes = planeteers + range

print(heroes)


# Alphabetize the contents of `heroes` using a function

def alphabetize(heroes):
    return sorted(heroes)


print(alphabetize(heroes))


# Randomize the contents of `heroes` using a function.
# The Python documentation might help: https://docs.python.org/3/library/random.html

def randomize(heroes):
    return random.shuffle(heroes)


randomize(heroes)

print(heroes)

# Initialize a dictionary called `ninja_turtle` with the properties `name`, `weapon` and `radical`
# They should have values of "Michelangelo", "Nunchuks" and a true boolean, respectively

ninja_turtle = {
    "name": "Michelangelo",
    "weapon": "Nunchuks",
    "radical": True
}


# Add a key `age` to `ninja_turtle`. Set it to whatever numerical value you'd like

ninja_turtle["age"] = 20


# Remove the `radical` key-value pair from `ninja_turtle`

ninja_turtle.pop("radical")


# Add a key `pizza_toppings` to `ninja_turtle`. Set it to an list of strings (e.g., `["cheese", "pepperoni", "peppers"]`)

ninja_turtle["pizza_toppings"] = ["cheese", "pepperoni", "peppers"]


# Access the first element of `pizza_toppings`

ninja_turtle["pizza_toppings"][0]


# Produce an list containing all of `ninja_turtle`'s keys using a function.
# The Python documentation might help: https://docs.python.org/3/tutorial/datastructures.html

ninja_turtle.keys()


# Produce a list containing all of `ninja_turtle`'s values using a function

ninja_turtle.values()
