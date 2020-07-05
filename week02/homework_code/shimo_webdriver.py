from selenium import webdriver
import time


def run():
    try:
        global browser
        browser = webdriver.Chrome()

        browser.get('https://shimo.im/welcome')
        time.sleep(1)

        # 找到登录按钮
        btm1 = browser.find_element_by_xpath(
            '//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
        btm1.click()
        # 填充账户和密码
        browser.find_element_by_xpath(
            '//*[@name="mobileOrEmail"]').send_keys('xxxx')
        browser.find_element_by_xpath(
            '//*[@name="password"]').send_keys('xxxx')
        time.sleep(1)

        # 登录
        browser.find_element_by_xpath('//button[@type="black"]').click()

    except Exception as e:
        print(e)
    finally:
        browser.close()


if __name__ == '__main__':
    run()
