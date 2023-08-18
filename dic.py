
# calls a dictionary

# no dot notation

# looks like a JSON object


alan = {

    "age": 26,
    "name": "Alan",
    "from": "Peru",


}


# grabs keys from dictionary

alan.keys()

print(alan.keys())

# grabs values from dictionary

alan.values()

print(alan.values())

# grabs items from dictionary

alan.items()

print(alan.items())

# grabs a specific value from a dictionary

alan["age"]

print(alan["age"])

# ranges


list(range(1, 10))

print(list(range(1, 10)))

for i in range(1, 10):
    print(i)

# if you add a third argument it will increment by that number

for i in range(1, 10, 2):
    print(i)


# to decrement you can use a negative number and
# set the first argument to the highest number

for i in range(10, 1, -2):
    print(i)

len(alan)
print("-------------")
print(len(alan))
