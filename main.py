# functions
def conv_fahrenheit_to_celsius(temp_fahrenheit) -> float:
    calc_temp = float(temp_fahrenheit) - 32
    calc_temp *= (5 / 9)
    return calc_temp


def conv_celsius_to_fahrenheit(temp_celsius) -> float:
    calc_temp = float(temp_celsius) * (9 / 5)
    calc_temp += 32
    return calc_temp

  def ask_for_input(question: str) -> str:
    return input(f"\n{question}\n")


# Enter point for the program
if __name__ == '__main__':

    # Welcome message
    welcome = "\nThis program converts temperatures between Fahrenheit and Celsius."

    # ask for temperature for conversion
    unknown_temp: str = ask_for_input(
        'Please enter the the temperature you would like to convert with (F/C) at the end:')
    unknown_temp = unknown_temp.lower()

    # Checking for valid input
    further_question: bool = False
    if "f" in unknown_temp or "c" in unknown_temp:
        pass
    else:
        further_question = True
        temp_unit = input("\nPlease specify between F/C:")
        temp_unit = temp_unit[0]
        unknown_temp = unknown_temp + " " + temp_unit

    # large if statement flow
    if "f" in unknown_temp:

        known_temp = unknown_temp.rstrip("f")
        known_temp = float(known_temp)
        output_temp = conv_fahrenheit_to_celsius(known_temp)

        # Formatting the floats to one decimal
        output_temp = '{0:.1f}'.format(output_temp)

        print(f"\nThe temperature has been converted to {output_temp} F")

    elif "c" in unknown_temp:

        known_temp = unknown_temp.rstrip("c")
        known_temp = float(known_temp)
        output_temp = conv_celsius_to_fahrenheit(known_temp)

        # Formatting the floats to one decimal
        output_temp = '{0:.1f}'.format(output_temp)

        print(f"\nThe temperature has been converted to {output_temp} C")

    else:
        print("\nEntropy stops at 0 Kelvin.")
