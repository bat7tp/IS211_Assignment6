class ConversionNotPossibleException(Exception):
    pass


def convert():
    from_unit = input("Please enter unit converting from: ")
    to_unit = input("Please enter unit converting to: ")
    value = float(input("Please enter value to be converted: "))

    if from_unit == to_unit:
        same_value = float(value)
        print(same_value)
        return same_value

    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        output_value = 1.8 * value + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        output_value = 273.15 + value
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        output_value = ((value - 32) * (5 / 9))
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        output_value = ((value - 32) * (5 / 9) + 273.15)
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        output_value = value * 9 / 5 - 459.67
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        output_value = value - 273.15
    elif from_unit == "Miles" and to_unit == "Yards":
        output_value = value * 1760
    elif from_unit == "Miles" and to_unit == "Meters":
        output_value = value * 1609.34
    elif from_unit == "Meters" and to_unit == "Yards":
        output_value = value * 1.09361
    elif from_unit == "Meters" and to_unit == "Miles":
        output_value = value / 1609.34
    elif from_unit == "Yards" and to_unit == "Meters":
        output_value = value / 1.09361
    elif from_unit == "Yards" and to_unit == "Miles":
        output_value = value / 1760
    else:
        raise ConversionNotPossibleException("Conversion not possible between those units")

    end_value = float(output_value)
    print(end_value)

    return end_value


convert()





