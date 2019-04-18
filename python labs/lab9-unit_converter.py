def convert_tm(distance, unit):
    if unit == "ft":
        return distance * 0.3048
    elif unit == "mi":
        return distance * 1609.34
    elif unit == "km":
        return distance * 1000
    elif unit == "yd":
        return distance * 0.9144
    elif unit == "in":
        return distance * 0.0254
    else:
        return distance

def convert_fm(distance, unit):
    if unit == "ft":
        return distance / 0.3048
    elif unit == "mi":
        return distance / 1609.34
    elif unit == "km":
        return distance / 1000
    elif unit == "yd":
        return distance / 0.9144
    elif unit == "in":
        return distance / 0.0254
    else:
        return distance

while True:
        distance = input("What is the distance?\n> ")
        if distance.isdigit():
            distance = int(distance)
            break
        else:
            print("Please enter a number")

unit_list = ['ft', 'mi', 'm', 'km', 'yd', 'in',]

while True:
    in_unit = input("What is the input unit? (ft), (mi), (m), (km), (yd), or (in)\n> ").lower().strip()
    if in_unit in unit_list:
        break
    print("input not valid")

while True:
    out_unit = input("What is the output unit? (ft), (mi), (m), (km), (yd), or (in)\n> ").lower().strip()
    if out_unit in unit_list:
        break
    print("input not valid")

print(f"{distance} {in_unit} is equal to {convert_fm(convert_tm(distance, in_unit), out_unit)} {out_unit}.")
