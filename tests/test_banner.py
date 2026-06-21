import app.banner


def test_banner_contains_text():
    banner = app.banner.get_banner()
    assert "CI DEMO" in banner
