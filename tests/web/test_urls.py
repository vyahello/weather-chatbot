from src.web.urls import CommonUrl


def test_common_url() -> None:
    assert CommonUrl("https://path/to/url").compose() == "https://path/to/url"
