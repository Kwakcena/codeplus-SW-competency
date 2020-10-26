from itertools import product

buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
N = input()

buttons_number = int(input())
broken_buttons = []
if buttons_number != 0:
    broken_buttons = list(input().split())

possible_buttons = list(filter(lambda x: x not in broken_buttons, buttons))


def move_using_only_plus_minus_button():
    return abs(100 - int(N))


def move_with_numbers_and_plus_minus():
    result = 10 ** 6
    for unit in range(1, 7):
        numbers = list(product(possible_buttons, repeat=unit))
        for number in numbers:
            current_channel = ''.join(number)
            button_count = abs(int(N) - int(current_channel)) + len(
                current_channel)
            if result > button_count:
                result = button_count
    return result


print(min(move_with_numbers_and_plus_minus(),
          move_using_only_plus_minus_button()))
