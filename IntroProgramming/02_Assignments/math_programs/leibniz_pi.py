"""
Jeremy Francis
2026_02_19
Leibniz Pi Formula
"""


def leibniz_pi_form(iterations):
    total = 0
    sign = 1
    for i in range(1, iterations + 1):
        denominator = (2 * i) - 1
        total = total + (sign / denominator)
        sign *= -1
    pi_value = total * 4
    return pi_value


# PROGRAM START
def main():
    print("\nLEIBNIZ PI FORMULA\n")
    while True:
        try:
            user_input = int(
                input(
                    "Please enter the amount of iterations you want to run for the formula: "
                )
            )
            if user_input <= 0:
                print("Please enter a number greater than 0.")
            else:
                result = leibniz_pi_form(user_input)
                print(
                    "\nThe calculated value of pi with "
                    + str(user_input)
                    + " iteration(s) is "
                    + str(result)
                    + "\n"
                )
                break
        except ValueError:
            print("Invaild input. Please enter a whole number.")


if __name__ == "__main__":
    main()
