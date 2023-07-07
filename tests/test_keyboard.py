from src.keyboard import Keyboard
import pytest


@pytest.fixture
def get_keyboard():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    return keyboard


def test_init_keyboard(get_keyboard):
    assert isinstance(get_keyboard, Keyboard)
    assert get_keyboard.name == 'Dark Project KD87A'
    assert get_keyboard.price == 9600
    assert get_keyboard.quantity == 5


def test_language(get_keyboard):
    assert get_keyboard.language == 'EN'
    with pytest.raises(AttributeError):
        get_keyboard.language = "CN"


def test_change_lang(get_keyboard):
    assert get_keyboard.language == "EN"
    get_keyboard.change_lang()
    assert get_keyboard.language == "RU"
    get_keyboard.change_lang().change_lang()
    assert get_keyboard.language == "RU"
