from src.phone import Phone
from src.item import Item
import pytest


@pytest.fixture
def get_phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


@pytest.fixture
def get_item():
    item = Item("Смартфон", 10000, 20)
    return item


def test_init_phone(get_phone):
    assert isinstance(get_phone, Phone)
    assert get_phone.name == "iPhone 14"
    assert get_phone.price == 120_000
    assert get_phone.quantity == 5
    assert get_phone.number_of_sim == 2


def test_repr(get_phone):
    assert repr(get_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(get_phone, get_item):
    assert get_phone + get_item == 25


def test_number_of_sim_getter(get_phone):
    assert get_phone.number_of_sim == 2


def test_number_of_sim_setter(get_phone):
    get_phone.number_of_sim = 3
    assert get_phone.number_of_sim == 3
    with pytest.raises(ValueError):
        get_phone.number_of_sim = 0
    with pytest.raises(ValueError):
        get_phone.number_of_sim = 1.1
    with pytest.raises(ValueError):
        get_phone.number_of_sim = -1
    with pytest.raises(ValueError):
        get_phone.number_of_sim = "bla bla bla"

