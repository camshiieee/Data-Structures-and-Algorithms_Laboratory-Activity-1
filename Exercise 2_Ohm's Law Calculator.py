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
    try:
        current = voltage / resistance
        print("\nThe current is", format(current, '.2f'), "A.")
    except ZeroDivisionError:
        print("\nError: Resistance cannot be zero when calculating current.")
elif option == "c":
    voltage = float(input("\nEnter the value of the voltage: "))
    current = float(input("Enter the value of the current: "))
    try:
        resistance = voltage / current
        print("\nThe resistance is", format(resistance, '.2f'), "Ω.")
    except ZeroDivisionError:
        print("\nError: Current cannot be zero when calculating resistance.")
else:
    print("\nInvalid option!")