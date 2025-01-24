from playwright.sync_api import Page, expect


def test_checkbox(page: Page) -> None:
    page.goto("https://demoqa.com/checkbox")
    page.locator("#tree-node").get_by_role("img").nth(3).click()

    expect(page.locator("#result").inner_text()).to_equal("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")


def test_expanded_single_check(page: Page) -> None:
    page.goto("https://demoqa.com/checkbox")
    page.get_by_label("Expand all").click()
    page.locator("label").filter(has_text="General").get_by_role("img").first.click()

    elements = page.locator("#tree-node .rct-node")
    for element in elements.all():
        expect(element).to_be_visible()

    expect(page.locator("#result").inner_text()).to_equal("You have selected :General")

