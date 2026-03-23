from pathlib import Path
import shutil

DRY_RUN = False  # change to False when ready

base = Path(r"C:\Users\jerem\OneDrive\Desktop\IntroProgramming")

folders = [
    "01_Basics/loops",
    "01_Basics/lists",
    "01_Basics/functions",
    "02_Assignments/early",
    "02_Assignments/improved",
    "02_Assignments/math_programs",
    "03_Practice_Programs",
    "03_Practice_Programs/utilities",
    "04_Projects/hangman",
    "04_Projects/character_generator",
    "04_Projects/slot_machine",
    "05_Exams",
    "06_Misc/notes",
]

moves = {
    "2026_02_02.py": "01_Basics/loops/guessing_game.py",
    "2026_02_09.py": "01_Basics/loops/range_practice.py",
    "2026_03_2026.py": "01_Basics/loops/fizzbuzz.py",
    "p.py": "01_Basics/loops/fizzbuzz_alt.py",
    "practice_problem.py": "01_Basics/functions/factorial.py",
    "functions.py": "01_Basics/functions/function_practice.py",
    "index.py": "01_Basics/functions/age_calculator.py",
    "2026_01_21a.py": "02_Assignments/early/basic_printing.py",
    "2026_01_21.py": "02_Assignments/early/weight_loss.py",
    "2026_02_10_extracredit.py": "02_Assignments/early/pyramid_pattern.py",
    "2026_02_24.py": "02_Assignments/improved/world_population_v2.py",
    "2026_02_10_pyramid.py": "02_Assignments/math_programs/pyramid_analysis.py",
    "2026_02_17.py": "02_Assignments/math_programs/compound_interest.py",
    "CSCT101_S01 - 0 - jfrancis2 (1).py": "02_Assignments/math_programs/leibniz_pi.py",
    "my_utilities.py": "03_Practice_Programs/utilities/my_utilities.py",
    "2026_02_11.py": "04_Projects/slot_machine/slot_machine_basic.py",
    "slot_test.py": "04_Projects/slot_machine/slot_machine_full.py",
    "hangman.py": "04_Projects/hangman/main.py",
    "hangman_art.py": "04_Projects/hangman/hangman_art.py",
    "hangman_words.py": "04_Projects/hangman/hangman_words.py",
    "main.py": "04_Projects/character_generator/main.py",
    "player.py": "04_Projects/character_generator/player.py",
    "2026_03_02.py": "05_Exams/practice_exam_bmi.py",
    "midterm_prac.py": "05_Exams/midterm_practice.py",
    "2026_03_04ex.py": "05_Exams/exam1_luminosity.py",
    "exam.py": "06_Misc/exam.py",
    "practice_2026_02_02.py": "06_Misc/practice_2026_02_02.py",
}

if not DRY_RUN:
    for folder in folders:
        (base / folder).mkdir(parents=True, exist_ok=True)

for old_name, new_relative_path in moves.items():
    old_path = base / old_name
    new_path = base / new_relative_path

    if old_path.exists():
        if new_path.exists():
            print(f"Skipped (already exists): {new_relative_path}")
            continue

        if DRY_RUN:
            print(f"[DRY RUN] Would move: {old_name} -> {new_relative_path}")
        else:
            new_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(old_path), str(new_path))
            print(f"Moved: {old_name} -> {new_relative_path}")
    else:
        print(f"Skipped (not found): {old_name}")

print("Done.")
