from playwright.sync_api import Page
import pytest


#Title test
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "lilAI - Smart Automated Community Management"

#ShieldBot image correct source test
def test_srcImageShieldBot(page: Page):
    page.goto("/")
    img = page.locator("img.main-illustration.transform-img-meta")
    assert img.get_attribute("src") == "images/assets/ShieldLilai.png"

#ShieldBot image visibility test
def test_srcImageShieldBotVisibility(page: Page):
    page.goto("/")
    img = page.locator("img[src='images/assets/ShieldLilai.png']")
    assert img.is_visible()

#Buy button test
def test_buyButton(page: Page,context):
    page.goto("/")
    with context.expect_page() as new_page_info:
        page.get_by_text("Buy $LILAI").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    assert "coingecko" in new_page.url

#Subscribe button
# def test_subscribeButton(page: Page):
#     page.goto("/")
#     page.get_by_role("textbox", name="Enter your email").click()
#     page.locator("#btmail").fill("test@test.com")
#     page.get_by_role("button", name="Subscribe").click()

#Roadmap site
def test_roadmap(page: Page):
    page.goto("/")
    page.get_by_role("button", name="Roadmap").click()
    page.wait_for_load_state()

    assert "Q1" in page.locator(".relative.ml-6").first.text_content()
    assert "Q2" in page.locator("div:nth-child(3) > .relative").first.text_content()
    assert "Q3" in page.locator("div:nth-child(4) > .relative").first.text_content()
    assert "Q4" in page.locator("div:nth-child(5) > .relative").first.text_content()
    assert "Stretch Goals" in page.locator("div:nth-child(6) > .relative").first.text_content()