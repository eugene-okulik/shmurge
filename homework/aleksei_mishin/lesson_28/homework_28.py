from playwright.sync_api import Page, expect


def test_exercise_one(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()

    login = page.get_by_role('textbox', name='username')
    password = page.get_by_role('textbox', name='password')

    login.fill('AlexTest')
    password.fill('12345')
    page.get_by_role('button', name='Login').click()


def test_exercise_two(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.locator('[id="firstName"]').fill('Alex')
    page.locator('[id="lastName"]').fill('Mishin')
    page.locator('[id="userEmail"]').fill('test@example.si')
    page.locator('[for="gender-radio-1"]').click()
    page.locator('[id="userNumber"]').fill('88888888888')
    birthday_input = page.locator('[id="dateOfBirthInput"]')
    birthday_input.fill('06.06.2000')
    birthday_input.press('Enter')
    subj_input = page.locator('[id="subjectsInput"]')
    subj_input.fill('Maths')
    subj_input.click()
    subj_input.press('Enter')
    page.locator('[for="hobbies-checkbox-1"]').check()
    page.locator('[for="hobbies-checkbox-2"]').check()
    page.locator('[for="hobbies-checkbox-3"]').check()
    page.locator('[id="currentAddress"]').fill('Широкая, 1')
    page.locator('[id="state"]').click()
    page.locator('//*[text()="Rajasthan"]').click()
    page.locator('[id="city"]').click()
    page.locator('//*[text()="Jaiselmer"]').click()
    page.locator('[id="submit"]').click()
