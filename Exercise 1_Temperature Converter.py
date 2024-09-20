temperature = float(input("Enter the temperature: "))

conversion = str(input("\nWhat conversion do you want? \n" +
                       "a. From Celsius to Fahrenheit\n" +
                       "b. From Fahrenheit to Celsius\n" +
                       "\nYour choice: "))

if conversion == "a":
    fahrenheit = (temperature * 9/5) + 32
    print(f"\nThe conversion of {temperature} °C is", format(fahrenheit, '.2f'), "°F.")
elif conversion == "b":
    celsius = (temperature - 32) * 5/9
    print(f"\nThe conversion of {temperature} °F is", format(celsius, '.2f'), "C.")
else:
    print("\nInvalid option!")