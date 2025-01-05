from random import choices


def fruit():
    fruits = ["apple", "banana", "orange", "grape", "kiwi"]
    return choices(fruits, k=1)[0]


def meal(beverage):
    my_fruit = fruit()
    print(f"Your fruit is {my_fruit} and bevarage is {beverage}")
    if my_fruit == "orange":
        return f"Your meal is a {my_fruit} and {beverage}"
    return f"Your meal is a steak and {beverage}"
