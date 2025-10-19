import json

from playwright.sync_api import Page, expect, Route


def test_exercise_one(page: Page):
    exp_res = 'Яблокофон 17 про'

    def handle_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = exp_res
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route('https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat', handle_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone_17_tab = page.locator('//*[@aria-label="All models."]/child::div[1]')
    iphone_17_tab.click()
    popup_header = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')

    expect(popup_header).to_have_text(exp_res)
