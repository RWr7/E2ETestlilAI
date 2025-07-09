from playwright.sync_api import Page
import pytest


#Title test
def test_title(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    assert page.title() == "lilAI - Smart Automated Community Management"


#ShieldBot image correct source test
def test_srcImageShieldBot(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    img = page.locator("img.main-illustration.transform-img-meta")
    assert img.get_attribute("src") == "images/assets/ShieldLilai.png"

#ShieldBot image visibility test
def test_srcImageShieldBotVisibility(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    img = page.locator("img[src='images/assets/ShieldLilai.png']")
    assert img.is_visible()