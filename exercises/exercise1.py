def find_numbers(a, b):
    numbers = []

    for number in range(a, b+1):
        if not number % 11 and number % 7:
            numbers.append(number)
    return numbers

# print(find_numbers(1000, 2500))
