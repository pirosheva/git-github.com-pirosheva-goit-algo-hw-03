import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min <1:
        return print("min mast be higher than 0")
    if max < 0 or max>=1000:
        return print("max mast be in range from 0 to 1000")
    if quantity == 0 or max-min + 1 < quantity:
        return []
    temp_set = set()
    while len(temp_set) < quantity:
        temp_set.add(random.randint(min, max))
    return sorted(list(temp_set))

min = input("Enter a min value: ")
max = input("Enter a max value: ")
quantity = input("Enter the number of numbers to select: ")
print(get_numbers_ticket(min, max, quantity))