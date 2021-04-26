
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""


    celsius = float(input("Enter a temperature in Celsius to be converted to K: "))

    # Converting formulas
    kelvin = 273.15 + celsius
    print("This is the temperature in degrees Kelvin: ", kelvin)

    return kelvin



def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    celsius = float(input("Enter a temperature in Celsius to be converted to F: "))

    # Converting formulas
    fahrenheit = 1.8 * celsius + 32
    print("This is the temperature in degrees Fahrenheit: ", fahrenheit)

    return fahrenheit



def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    fahrenheit = float(input("Enter a temperature in Fahrenheit to be converted to C: "))

    # Converting formulas
    celsius = ((fahrenheit - 32) * (5/9))
    print("This is the temperature in degrees Celsius: ", celsius)

    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a F measurement, and returns that temperature converted into K"""
    fahrenheit = float(input("Enter a temperature in Fahrenheit to be converted to K: "))

    # Converting formulas
    kelvin = ((fahrenheit - 32) * (5/9) + 273.15)
    print("This is the temperature in degrees Kelvin: ", kelvin)

    return round(kelvin, 2)


def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a K measurement, and returns that temperature converted into Celsius"""
    kelvin = float(input("Enter a temperature in Kelvin to be converted to C: "))

    # Converting formulas
    celsius = kelvin - 273.15
    print("This is the temperature in degrees Celsius: ", celsius)

    return round(celsius, 2)

def convertKelvinToFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into F"""
    kelvin = float(input("Enter a temperature in Kelvin to be converted to F: "))

    # Converting formulas
    fahrenheit = kelvin * 9/5 - 459.67
    print("This is the temperature in degrees Fahrenheit: ", fahrenheit)

    return round(fahrenheit, 2)