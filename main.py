class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        if celsius < -273.15:
            raise ValueError("Invalid temperature value: below absolute zero")
        fahrenheit = celsius * 9/5 + 32
        return fahrenheit
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        if fahrenheit < -459.67:
            raise ValueError("Invalid temperature value: below absolute zero")
        celsius = (fahrenheit - 32) * 5/9
        return celsius
temperature_converter = TemperatureConverter()
try:
    fahrenheit = temperature_converter.celsius_to_fahrenheit(25)
    print(fahrenheit)
except ValueError as e:
    print(e)
try:
    celsius = temperature_converter.fahrenheit_to_celsius(77)
    print(celsius)
except ValueError as e:
    print(e)
