from playwright.sync_api import Page
import pytest


def test_title(page: Page):
    page.goto("https://lilai.co/")
    assert page.title() == "lilAI - Smart Automated Community Management"
