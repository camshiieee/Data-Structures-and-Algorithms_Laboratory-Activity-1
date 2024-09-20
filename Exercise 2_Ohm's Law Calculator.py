option = str(input("What do you want to calculate?\n" +
                   "a. Voltage\n" +
                   "b. Current\n" +
                   "c. Resistance\n" +
                   "\nYour choice: "))

if option == "a":
    current = float(input("\nEnter the value of the current: "))
    resistance = float(input("Enter the value of the resistance: "))
    voltage = current * resistance
    print("\nThe voltage is", format(voltage, '.2f'), "V.")
elif option == "b":
    voltage = float(input("\nEnter the value of the voltage: "))
    resistance = float(input("Enter the value of the resistance: "))
    current = voltage / resistance
    print("\nThe current is", format(current, '.2f'), "A.")
elif option == "c":
    voltage = float(input("\nEnter the value of the voltage: "))
    current = float(input("Enter the value of the current: "))
    resistance = voltage / current
    print("\nThe resistance is", format(resistance, '.2f'), "Ω.")
else:
    print("\nInvalid option!")