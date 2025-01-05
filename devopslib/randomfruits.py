from random import choices


def fruit():
    fruits = ["apple", "banana", "orange", "grape", "kiwi"]
    return choices(fruits, k=1)[0]
