'''Advent of code Day 1 Problem 1
'''
def find_elf_with_most_calories(input_text: str) -> int:
    most_calories = 0
    elf_calorie_lists = input_text.split('\n\n')
    for elf in elf_calorie_lists:
        calories_in_meal = sum([int(line) for line in elf.split('\n') if line])
        if calories_in_meal > most_calories:
            most_calories=calories_in_meal
    return most_calories
