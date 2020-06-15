from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time


#클립보드에 input을 복사한 뒤
#해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
def copy_input(xpath, input,driver):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)


def naver_blog(id,pw):

    driver = webdriver.Chrome(r'C:\Users\adf\Downloads\chromedriver_win32\chromedriver.exe')
    driver.implicitly_wait(3)

    driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

    copy_input('//*[@id="id"]', id,driver)
    time.sleep(1)
    copy_input('//*[@id="pw"]', pw,driver)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(3)

    driver.implicitly_wait(3)
    driver.get('https://blog.naver.com/MyBlog.nhn')
    driver.get(driver.current_url + "/postwrite")
    title = "제목"
    main = "내용"
    driver.implicitly_wait(5)

    # selector = "se-toolbar-button-code"
    # query = 'document.getElementsByClassName("%s")[1].click()'%(selector)
    # driver.execute_script(query)

    time.sleep(5)

    actions1 = ActionChains(driver)
    actions2 = ActionChains(driver)
    actions3 = ActionChains(driver)
    actions4 = ActionChains(driver)

    actions1.send_keys(Keys.UP).perform();
    time.sleep(1)
    actions2.send_keys(title).perform();
    time.sleep(1)
    actions3.send_keys(Keys.DOWN).perform();
    time.sleep(1)
    actions4.send_keys(main).perform();
    time.sleep(1)
    driver.find_element_by_xpath('//*[@class="se-help-panel-close-button"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="header"]/div[@class="header_menu"]/div[@class="area_btn_publish"]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@class="btn_confirm"]').click()
    # copy_input('//*[@id="SE-87a3377b-0f88-4526-a915-9f118c0d8ed2"]',title)
    # copy_input('//*[@id="SE-0d8ad3fc-1dbb-47d3-8864-b233a13c3063"]',main)

