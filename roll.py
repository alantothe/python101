print("Welcome to the Iron Rattler! How tall are you (in feet)?")
height = int(input())

if height < 4:
    print("Sorry, you'll fly out of your seat if we let you on.")
elif height < 7:
    print("All aboard!")
else:
    print("If you value your head, you should not get on this ride.")


def double(number=5):
    return number * 2


double()
# => 10


class_number = 22

f"I have taught SEI {class_number} times."

person1 = "Lauren"
person2 = "Frank"
occupation = "consultant"

f"{person1} is a {occupation}. {person2} is a {occupation} as well."
# => "Lauren is a consultant. Frank is a consultant as well."


1 + 2  # Addition
# => 3

6 - 5  # Subtraction
# => 1

5 * 2  # Multiplication
# => 10

30 / 5  # Division
# => 6.0

31 // 5  # Note: Integer Division
# => 6

30 % 5  # Modulo (Remainder)
# => 0

31 % 5
# => 1

3 ** 2  # Exponentiation
# => 9
