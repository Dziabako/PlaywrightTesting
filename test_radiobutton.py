from playwright.sync_api import Page, expect


def test_yes_button(page: Page) -> None:
    page.goto("https://demoqa.com/radio-button")
    page.get_by_text("Yes").click()

    expect(page.locator("text=You have selected Yes").is_visible()).to_be_truthy()
    

def test_impresive_button(page: Page) -> None:
    page.goto("https://demoqa.com/radio-button")
    page.get_by_text("Impressive").click()

    expect(page.locator("text=You have selected Impressive").is_visible()).to_be_truthy()


def test_no_button(page: Page) -> None:
    page.goto("https://demoqa.com/radio-button")
    page.get_by_text("No").click()

    expect(page.locator("input#noRadio").is_disabled()).to_be_truthy()