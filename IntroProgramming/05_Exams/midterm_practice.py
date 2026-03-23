"""
Jeremy Francis
2026_02_25
Midterm Practice
"""


def classify_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


def main():
    count = 0
    total = 0
    min_grade = ""
    max_grade = 0
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_f = 0
    while True:
        user_input = float(input("Enter a grade (-1 to quit): "))
        if user_input == -1:
            break
        count += 1
        total += user_input
        letter = classify_grade(user_input)
        print(letter)
        if letter == "A":
            count_a += 1
        elif letter == "B":
            count_b += 1
        elif letter == "C":
            count_c += 1
        elif letter == "D":
            count_d += 1
        elif letter == "F":
            count_f += 1
        if user_input > max_grade:
            max_grade = user_input
        if min_grade == "" or user_input < min_grade:
            min_grade = user_input

    print("num grades: " + str(count))
    print("Avg grade: " + str(total / count), end=" ")
    print(classify_grade(total / count))
    print("Max grades: " + str(max_grade))
    print("Min grades: " + str(min_grade))
    print(f"Grades: A:{count_a},B:{count_b},C:{count_c},D:{count_d},F:{count_f}")


if __name__ == "__main__":
    main()
