"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import pytest

@pytest.fixture
def get_product():
    product = Item("product", 500, 10)
    return product


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

