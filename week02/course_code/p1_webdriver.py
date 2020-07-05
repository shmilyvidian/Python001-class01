from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.get('https://shimo.im/welcome')
    time.sleep(1)

    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    print(btm1)
    btm1.click()

    browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('shmilyvidian@163.com')
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('lsf19941026@!')
    time.sleep(1)
    browser.find_element_by_xpath('//button[@type="black"]').click()
    
except Exception as e:
    print(e)
finally:
    browser.close()