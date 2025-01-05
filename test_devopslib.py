from devopslib.randomfruits import fruit, meal


def test_fruit():
    fruit_choice = fruit()
    assert fruit_choice in ["apple", "banana", "orange", "grape", "kiwi"]

def test_meal():
    result = meal("milk")
    assert "milk" in result


