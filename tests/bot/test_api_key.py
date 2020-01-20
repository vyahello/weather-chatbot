from chat.bot import BOT_API_TOKEN

_api_key: str = str()


def test_api_key() -> None:
    assert BOT_API_TOKEN == _api_key
