import random
from list_utils import find_max, remove_duplicates

def generate_random_numbers(count, min_val, max_val):
    """
    Generiert eine Liste von Zufallszahlen.
    """
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(min_val, max_val))
    return numbers

if __name__ == "__main__":
    print("Willkommen zum Zufallszahlen-Generator und Listen-Helfer!")

    random_list = generate_random_numbers(10, 1, 50)
    print(f"Generierte Liste: {random_list}")

    max_num = find_max(random_list)
    if max_num is not None:
        print(f"Die größte Zahl ist: {max_num}")

    list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 1]
    print(f"\nListe mit Duplikaten: {list_with_duplicates}")

    unique_list = remove_duplicates(list_with_duplicates)
    print(f"Liste ohne Duplikate: {unique_list}")