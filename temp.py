# temp_converter.py
temp = int(input("Starting Temp? (Numbers only)"))


convert = input("Convert to ...")


def convert(temp, type):
    if type == "F":
        print(temp - 32 / 1.8)
    elif type == "C":
        print( temp * 1.8 + 32)
    elif type == "K":
        print("convert to C and F")
    else:
        print("Invalid Input")



