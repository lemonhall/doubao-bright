import time
from playwright.sync_api import Playwright, sync_playwright, expect



def send_input(page,input):
    #第二步：say hi
    page.get_by_role("textbox", name="发消息").click()
    page.get_by_role("textbox", name="发消息").fill(input)
    page.get_by_role("button", name="发送").click()

    #第三步：等待
    # 暂停 5 秒钟
    time.sleep(5)

    #第四步：取剪贴板
    page.locator(".action-button-f4a696 > .semi-button").first.click()
    response_text = page.evaluate("navigator.clipboard.readText()")
    
    return response_text

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")

    #第一步：取得剪切板的授权
    context.grant_permissions(['clipboard-read','clipboard-write'])
    page = context.new_page()
    page.goto("https://www.doubao.com/chat/")

    while True:
        user_input = input("请输入一些内容：")
        res_text= send_input(page,user_input)
        print("豆包：",res_text)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
