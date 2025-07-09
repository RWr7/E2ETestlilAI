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

#Buy button test
def test_buyButton(page: Page,context):
    page.goto("/")
    page.wait_for_load_state()
    with context.expect_page() as new_page_info:
        page.get_by_text("Buy $LILAI").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    assert "coingecko" in new_page.url

#Subscribe button
# def test_subscribeButton(page: Page):
#     page.goto("/")
#     page.wait_for_load_state()
#     page.get_by_role("textbox", name="Enter your email").click()
#     page.locator("#btmail").fill("test@test.com")
#     page.get_by_role("button", name="Subscribe").click()

#Roadmap site
def test_roadmapSite(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    page.get_by_role("button", name="Roadmap").click()
    page.wait_for_load_state()
    assert "roadmap.html" in page.url
    assert "Q1" in page.locator(".relative.ml-6").first.text_content()
    assert "Q2" in page.locator("div:nth-child(3) > .relative").first.text_content()
    assert "Q3" in page.locator("div:nth-child(4) > .relative").first.text_content()
    assert "Q4" in page.locator("div:nth-child(5) > .relative").first.text_content()
    assert "Stretch Goals" in page.locator("div:nth-child(6) > .relative").first.text_content()

#Team site
def test_teamSite(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    page.get_by_role("button", name="Team").click()
    page.wait_for_load_state()
    assert "team.html" in page.url

#Bridge link
def test_bridgeLink(page: Page,context):
    page.goto("/")
    page.wait_for_load_state()
    with context.expect_page() as new_page_info:
        page.get_by_role("button", name="Bridge").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    assert "debridge" in new_page.url

#Explorer link
def test_explorerLink(page: Page,context):
    page.goto("/")
    page.wait_for_load_state()
    with context.expect_page() as new_page_info:
        page.get_by_role("button", name="Explorer").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    assert "arbiscan" in new_page.url

#Products overview
def test_productsOverview(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    page.get_by_role("button", name="Products").click()
    page.get_by_role("link", name="Products Overview").click()
    page.wait_for_load_state()
    assert "our_products.html" in page.url

#Anti-Spam
def test_antiSpam(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    page.get_by_role("button", name="Products").click()
    page.get_by_role("link", name="Anti-Spam", exact=True).click()
    page.wait_for_load_state()
    assert "lilai_as.php" in page.url

#Community Manager
def test_communityManager(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    page.get_by_role("button", name="Products").click()
    page.locator("#navbarNav").get_by_role("link", name="Community Manager").click()
    page.wait_for_load_state()
    assert "lilai_cm.php" in page.url

#Data Oracle
def test_dataOracle(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    page.get_by_role("button", name="Products").click()
    page.get_by_role("link", name="LilAI Data Oracle").click()
    page.wait_for_load_state()
    assert "lilai_data_oracle.php" in page.url

#Bluebird
def test_bluebird(page: Page):
    page.goto("/")
    page.wait_for_load_state()
    page.get_by_role("button", name="Products").click()
    page.get_by_role("link", name="lilAI Bluebird").click()
    page.wait_for_load_state()
    assert "lilAI_bluebird.php" in page.url

