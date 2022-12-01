'''Advent of code Day 1 Problem 1
'''
example_input_text = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

def find_elf_with_most_calories(input_text: str) -> int:
    most_calories = 0
    elf_calorie_lists = input_text.split('\n\n')
    for elf in elf_calorie_lists:
        calories_in_meal = sum([int(line) for line in elf.split('\n') if line])
        if calories_in_meal > most_calories:
            most_calories=calories_in_meal
    return most_calories

def find_elf_with_most_calories_v2(input_text: str) -> int:
    calories_by_elf = []
    elf_calorie_lists = input_text.split('\n\n')
    for elf in elf_calorie_lists:
        calories_in_meal = sum([int(line) for line in elf.split('\n') if line])
        calories_by_elf.append(calories_in_meal)
    
    calories_by_elf.sort(reverse=True)
    return sum(calories_by_elf[0:3])

if __name__ == "__main__":
    assert(find_elf_with_most_calories(example_input_text)==24000)
    assert(find_elf_with_most_calories_v2(example_input_text)==45000)

    input_data=open('./1.input', 'r').read()
    print(f"Part 1: {find_elf_with_most_calories(input_data)}")
    print(f"Part 2: {find_elf_with_most_calories_v2(input_data)}")