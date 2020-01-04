from src.bot import BOT_API_TOKEN

_api_key: str = "523806969:AAGmLcMpcH_wUd69KB6JeN3ETGUtXbjoGz0"


def test_api_key() -> None:
    assert BOT_API_TOKEN == _api_key
