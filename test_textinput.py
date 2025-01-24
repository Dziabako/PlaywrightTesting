from playwright.sync_api import Page, expect


def test_correct_input(page: Page) -> None:
    page.goto("https://demoqa.com/text-box")
    
    page.get_by_placeholder("Full Name").fill("Test Test")
    page.get_by_placeholder("name@example.com").fill("test@test.com")
    page.get_by_placeholder("Current Address").fill("Test 12\n12-345 Test")
    page.locator("#permanentAddress").fill("Test 12\n12-345 Test")
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#output").inner_text()).to_equal("Name:Test Test\nEmail:test@test.com\nCurrent Address :Test 12 12-345 Test\nPermananet Address :Test 12 12-345 Test")
    

def test_incorrect_input(page: Page) -> None:
    page.goto("https://demoqa.com/text-box")
    
    page.get_by_placeholder("Full Name").fill("Test Test")
    page.get_by_placeholder("name@example.com").fill("test")
    page.get_by_placeholder("Current Address").fill("Test 12\n12-345 Test")
    page.locator("#permanentAddress").fill("Test 12\n12-345 Test")
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#output").is_visible()).to_be_false()
    expect(page.get_by_placeholder("name@example.com")).to_have_css("border", "rgb(255, 0, 0)")


def test_empty_submit(page: Page) -> None:
    page.goto("https://demoqa.com/text-box")
    
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#output").inner_text).to_equal("")
    
