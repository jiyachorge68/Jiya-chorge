
import math

def physical_chemistry_calculator():
    print("===================================")
    print("   PHYSICAL CHEMISTRY CALCULATOR")
    print("===================================")
    print("1. Calculate Moles")
    print("2. Calculate Molarity")
    print("3. Calculate pH")
    print("4. Calculate pOH")
    print("5. Calculate pH from pOH")

    choice = input("\nEnter your choice (1-5): ")

    try:
        if choice == "1":
            mass = float(input("Enter mass of solute (g): "))
            molar_mass = float(input("Enter molar mass (g/mol): "))

            if mass < 0 or molar_mass <= 0:
                print("Enter valid positive values.")
                return

            moles = mass / molar_mass
            print(f"Number of moles = {moles:.4f} mol")

        elif choice == "2":
            moles = float(input("Enter moles of solute: "))
            volume = float(input("Enter solution volume (L): "))

            if moles < 0 or volume <= 0:
                print("Enter valid positive values.")
                return

            molarity = moles / volume
            print(f"Molarity = {molarity:.4f} mol/L")

        elif choice == "3":
            h_concentration = float(
                input("Enter H+ concentration (mol/L): ")
            )

            if h_concentration <= 0:
                print("Concentration must be greater than zero.")
                return

            ph = -math.log10(h_concentration)
            print(f"pH = {ph:.4f}")

        elif choice == "4":
            oh_concentration = float(
                input("Enter OH- concentration (mol/L): ")
            )

            if oh_concentration <= 0:
                print("Concentration must be greater than zero.")
                return

            poh = -math.log10(oh_concentration)
            print(f"pOH = {poh:.4f}")

        elif choice == "5":
            poh = float(input("Enter pOH: "))
            ph = 14 - poh  # At 25°C

            print(f"pH = {ph:.4f} at 25°C")

        else:
            print("Invalid choice. Please select 1 to 5.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    physical_chemistry_calculator()

