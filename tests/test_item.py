"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import pytest

@pytest.fixture
def get_product():
    product = Item("product", 500, 10)
    return product

def test_item_creation():
    expected_all_count = len(Item.all) + 1
    name = "product"
    price = 500
    quantity = 10
    item = Item(name, price, quantity)
    assert item.name == name
    assert item.price == price
    assert item.quantity == quantity
    assert len(Item.all) == expected_all_count


@pytest.mark.parametrize("price, quantity", [
    (500.0, 10),
    (300, 20.0),
    (0.0, 6),
    (1, 0),
    (0, 0)
])
def test_calculate_total_price(get_product, price, quantity):
    get_product.price = price
    get_product.quantity = quantity
    assert get_product.calculate_total_price() == price * quantity


@pytest.mark.parametrize("rate", [1, 2, 3, 0.5, 1.0])
def test_apply_discount(get_product, rate):
    product = Item("product", 500, 10)
    Item.pay_rate = rate
    product.apply_discount()
    assert product.price == get_product.price * Item.pay_rate


def test_name_getter(get_product):
    expected = "product"
    assert get_product.name == expected


def test_name_setter(get_product):
    expected = "new_name"
    get_product.name = "new_name"
    assert get_product.name == expected


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == '100'
    assert Item.all[0].quantity == '1'
    assert Item.all[1].name == 'Ноутбук'
    assert Item.all[1].price == '1000'
    assert Item.all[1].quantity == '3'
    assert Item.all[2].name == 'Кабель'
    assert Item.all[2].price == '10'
    assert Item.all[2].quantity == '5'
    assert Item.all[3].name == 'Мышка'
    assert Item.all[3].price == '50'
    assert Item.all[3].quantity == '5'
    assert Item.all[4].name == 'Клавиатура'
    assert Item.all[4].price == '75'
    assert Item.all[4].quantity == '5'


@pytest.mark.parametrize('string', ['5', '5.5', '0.5', '55', '55.55'])
def test_string_to_number(string):
    assert type(Item.string_to_number(string)) == int
