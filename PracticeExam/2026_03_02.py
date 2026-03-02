"""
Jeremy Francis
2026_03_02
Practice Exam
"""


def body_mass_index(weight, height):
    bmi = weight / (height * height)
    if bmi <= 18:
        print(f"\nA body mass index of {bmi} is considered underweight")
    elif bmi > 18 and bmi <= 24:
        print(f"\nA body mass index of {bmi} is considered healthy")
    elif bmi > 24 and bmi <= 29:
        print(f"\nA body mass index of {bmi} is considered overweight")
    else:
        print(f"\nA body mass index of {bmi} is considered obese")
    return bmi


def get_height():
    while True:
        # TRY AND EXCEPT BLOCK TO HANDLE ERRORS
        try:
            user_height = float(
                input("Please enter your height in meters (0 to quit): ")
            )
            if user_height < 0:
                print("please enter a number greater than 0")
            else:
                break
        except ValueError:
            print("Invalid entry: please enter a number greater than 0")
    return user_height


def get_weight():
    while True:
        # TRY AND EXCEPT BLOCK TO HANDLE ERRORS
        try:
            user_weight = float(input("Please enter your weight in kg (0 to quit): "))
            if user_weight < 0:
                print("please enter a number greater than 0")
            else:
                break
        except ValueError:
            print("Invalid entry: please enter a number greater than 0")
    return user_weight


def main():
    # CLASSES
    underweight = 0
    healthy = 0
    overweight = 0
    obese = 0
    # RUNNING TOTALS
    total_bmi = 0
    count = 0
    min_bmi = None
    max_bmi = None
    while True:
        user_weight = get_weight()
        # QUIT PROGRAM IF USER ENTERS 0
        if user_weight == 0:
            break
        user_height = get_height()
        # QUIT PROGRAM IF USER ENTERS 0
        if user_height == 0:
            break
        bmi = body_mass_index(user_weight, user_height)
        # ADD +1 COUNT FOR EACH ITERATION
        count += 1
        total_bmi += bmi
        # MAINTAIN MIN VALUE
        if min_bmi is None or bmi < min_bmi:
            min_bmi = bmi
        # MAINTAIN MAX VALUE
        if max_bmi is None or bmi > max_bmi:
            max_bmi = bmi
        # TOTALS FOR CLASSES
        if bmi <= 18.0:
            underweight += 1
        elif bmi > 18.0 and bmi <= 24:
            healthy += 1
        elif bmi > 24.0 and bmi <= 29:
            overweight += 1
        else:
            obese += 1
        print(
            f"""
TOTAL UNDERWEIGHT: {underweight}
TOTAL HEALTHY: {healthy}
TOTAL OVERWEIGHT: {overweight}
TOTAL OBESE: {obese}
AVERAGE BMI: {total_bmi/count}
MINIMUM BMI: {min_bmi}
MAXIMUM BMI: {max_bmi}
"""
        )


if __name__ == "__main__":
    main()
