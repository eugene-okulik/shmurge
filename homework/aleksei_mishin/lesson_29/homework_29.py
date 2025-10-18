import re
from playwright.sync_api import Page, expect, Dialog, BrowserContext


def test_exercise_one(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role(role='link', name='Click').click()
    message = page.locator('[id="result"]')

    expect(message).to_have_text('You selected Ok')


def test_exercise_two(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_button = page.get_by_role(role='link', name='Click')
    with context.expect_page() as new_tab_event:
        click_button.click()

    new_page = new_tab_event.value
    message = new_page.locator('[id="result-text"]')

    expect(message).to_have_text('I am a new page in a new tab')
    expect(click_button).to_be_enabled()


def test_exercise_three(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    change_color_button = page.locator('[id="colorChange"]')

    expect(change_color_button).to_have_attribute(name='class',
                                                  value=re.compile('text-danger'))
    change_color_button.click()
