number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(number[2])

# Arrays are like lists these are the meothods

# append is like push

# extend is like concat

# pop is like pop

# remove is like shift

# insert is like unshift

# sort is like sort

# reverse is like reverse

# count is like count

# index is like indexOf

# copy is like slice

# clear is like clear

# len is like length


number.append(11)

print(number)


number.extend([12, 13, 14, 15])

print(number)


# pop works a little different than js you can pass in a
# index to remove or it will remove the last item in the array
number.pop()

print(number)

number.pop(4)

print(number)


# sorted is a global method in python
sorted(number)

# sort works on strings too (unicode)
sorted("alan")
print(sorted("alan"))

# reverse works on strings too (unicode)

# remove will remove the first instance of the item passed in
number.remove(11)

print(number)
