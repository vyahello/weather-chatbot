import pytest
from chat.bot.text import Text, InputText


@pytest.fixture(scope="module")
def input_text() -> Text:
    return InputText(text="/test", pattern=r"\w+")


def test_match(input_text: Text) -> None:
    assert input_text.match()


def test_get(input_text: Text) -> None:
    assert input_text.get() == "test"
