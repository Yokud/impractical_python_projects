"""Main programm."""

import sys
import random


def get_nickname(names_list, lastnames_list):
    """Return randomly generated nickname."""
    return "{} {}".format(random.choice(names_list),
                          random.choice(lastnames_list))

def main():
    """Print randomly generate gachi-nickname."""
    names = ("Billy", "Boss of the", "Van", "Artist", "Slave", "Boy")

    lastnames = ("Herrington", "Gym", "Deep dark fantasies", "Fisting", "Spanking",
                 "Performance", "Fucking", "Cum", "Skin")

    try_again = True

    print("Добро пожаловать в программу для генерации Гачи-имён.\n"
          "Надеюсь, вам понравится ею пользоваться.")

    while try_again:
        print("\n\n", '=' * 50, sep = '')
        print("Ваше гачи-имя: ", end = '')
        print(get_nickname(names, lastnames), file = sys.stderr)
        try_again = input("\nХотите попробовать ещё раз?"
                          "(Введите 'n' для отказа): ").lower() != 'n'
        print("=" * 50)

    print("\nЗавершение работы")

if __name__ == "__main__":
    main()
