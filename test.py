import unittest
import conversions

class Testing(unittest.TestCase):
    def test_CelsiusToFahrenheit(self):
        self.assertEqual(conversions.convertCelsiusToFahrenheit(77), 170.6, "77 degrees C should equal 170.6 F")
        self.assertEqual(conversions.convertCelsiusToFahrenheit(100), 212, "100 degrees C should equal 212 F")
        self.assertEqual(conversions.convertCelsiusToFahrenheit(3), 37.4, "3 degrees C should equal 37.4 F")
        self.assertEqual(conversions.convertCelsiusToFahrenheit(-5), 23, "-5 degrees C should equal 23 F")
        self.assertEqual(conversions.convertCelsiusToFahrenheit(32), 89.6, "32 degrees C should equal 89.6 F")

    def test_CelsiusToKelvin(self):
        self.assertEqual(conversions.convertCelsiusToKelvin(77), 350.15, "77 degrees C should equal 350.15 K")
        self.assertEqual(conversions.convertCelsiusToKelvin(100), 373.15, "100 degrees C should equal 373.15 K")
        self.assertEqual(conversions.convertCelsiusToKelvin(3), 276.15, "3 degrees C should equal 276.15 K")
        self.assertEqual(conversions.convertCelsiusToKelvin(-5), 268.15, "-5 degrees C should equal 268.15 K")
        self.assertEqual(conversions.convertCelsiusToKelvin(32), 305.15, "32 degrees C should equal 305.15 K")

    def test_FahrenheitToCelsius(self):
        self.assertEqual(conversions.convertFahrenheitToCelsius(77), 25, "77 degrees F should equal 25 C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(104), 40, "104 degrees equals 40 C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(5), -15, "5 degrees F equals -15 C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(-13), -25, "-13 degrees F equals -25 C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(32), 0, "32 degrees F should equal 0 C")


    def test_FahrenheitToKelvin(self):
        self.assertEqual(conversions.convertFahrenheitToKelvin(77), 298.15, "77 degrees F should equal 298.15 K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(104), 313.15, "104 degrees F equals 313.15 K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(5), 258.15, "5 degrees F should equal 258.15 K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(-13), 248.15, "-13 degrees F equals  248.15 K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(32), 273.15, "32 degrees F should equal 273.15 K")

    def test_KelvinToCelsius(self):
        self.assertEqual(conversions.convertKelvinToCelsius(77), -196.15, "77 degrees K should equal -196.15 C")
        self.assertEqual(conversions.convertKelvinToCelsius(104), -169.15, "104 degrees K equals -169.15 C")
        self.assertEqual(conversions.convertKelvinToCelsius(5), -268.15, "5 degrees K equals -268.15 C")
        self.assertEqual(conversions.convertKelvinToCelsius(-13), -286.15, "-13 degrees K equals -286.15 C")
        self.assertEqual(conversions.convertKelvinToCelsius(32), -241.15, "32 degrees K should equal -241.15 C")

    def test_KelvinToFahrenheit(self):
        self.assertEqual(conversions.convertKelvinToFahrenheit(77), -321.07, "77 degrees K should equal -321.07 F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(104), -272.47, "104 degrees K equals -272.47 F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(5), -450.67, "5 degrees K equals -450.67 F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(-13), -483.07, "-13 degrees K equals -483.07 F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(32), -402.07, "32 degrees K should equal -402.07 F")



unittest.main()