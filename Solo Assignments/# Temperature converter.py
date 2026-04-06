# Temperature converter
import pygame
import sys
class TemperatureConverter:
    background_color = "Blue"
    
    def __init__(self, temperature):
        self.temperature = temperature

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose conversion (1 or 2): ")
    
    if choice == '1':
        temp = float(input("Enter temperature in Celsius: "))
        converter = TemperatureConverter(temp)
        result = converter.celsius_to_fahrenheit()
        print(f"{temp}°C is {result:.2f}°F")
    elif choice == '2':
        temp = float(input("Enter temperature in Fahrenheit: "))
        converter = TemperatureConverter(temp)
        result = converter.fahrenheit_to_celsius()
        print(f"{temp}°F is {result:.2f}°C")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

            