from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

#configurações de abertura do browser
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')

service = Service('C:/Desenvolvimento/Drives/chromedriver.exe')
browser = webdriver.Chrome(options=options, service=service)
browser.get("https://apollo.portal.nttltd.global.ntt/admin/app/login")

#clica no botão "corporate login"
bt_login = browser.find_element(By.XPATH, '/html/body/bn-root/ng-component/div/main/div/div/div/div/div[2]/div/div/div/div/button')
bt_login.click()
sleep(3)

#associando uma variável à nova url do login
url = browser.current_url
print(url)

#login pessoal
name = 'usuário NTT'
password = 'Senha'

#Digita o e-mail
user_login = browser.find_element(By.CSS_SELECTOR, '#i0116')
user_login.click()
user_login.send_keys(name)

bt_next = browser.find_element(By.XPATH, '//*[@id="idSIButton9"]')
bt_next.click()
sleep(2)

#Digita a senha
password_login = browser.find_element(By.CSS_SELECTOR, '#i0118')
password_login.click()
password_login.send_keys(password)

password_login = browser.find_element(By.XPATH, '//*[@id="idSIButton9"]')
password_login.click()
sleep(1)

#browser.close()