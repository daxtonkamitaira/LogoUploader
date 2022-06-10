import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

login = {
    'email': '',
    'password': '',
}

logos = []
logo_dir = 'logos'
for (dirpath, dirnames, filenames) in os.walk(logo_dir, topdown=True):
    for f in filenames:
        logos.append(os.path.abspath(os.path.join(dirpath, f)))

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://worldvectorlogo.com/account/sign-in')

email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'password')

email.send_keys(login['email'])
password.send_keys(login['password'])
password.submit()

for logo in logos:
    driver.get('https://worldvectorlogo.com/account/add-logo')

    logo_input = driver.find_element(By.XPATH, '//input[@type="file"]')
    tag_input = driver.find_element(By.CLASS_NAME, 'taggle_input')
    next = driver.find_element(By.XPATH, '//button[@class="button button--green button--full-width"]')

    logo_input.send_keys(logo)

    sleep(3)

    tag_input.send_keys(os.path.basename(logo).split('.')[0])
    tag_input.send_keys(Keys.ENTER)
    next.click()

    submit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="button button--wide button--green"]')))
    submit.click()

    sleep(3)

driver.quit()
