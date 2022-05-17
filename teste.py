from playwright.sync_api import sync_playwright
import os

user_dir = '/tmp/playwright'

if not os.path.exists(user_dir):
  os.makedirs(user_dir)

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(user_dir, channel="msedge", headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("edge://settings/defaultbrowser")
    page.locator("[aria-label='Adicionar página às páginas do modo Internet Explorer']").click() 
    page.fill('#userListAddUrl', 'https://google.com')   
    page.locator('[aria-invalid="false"]').click()

    browser.close()
