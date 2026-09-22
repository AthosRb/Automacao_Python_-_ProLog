from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://adm.prologapp.com/login")

sleep(6)

campo_user = browser.find_element(By.XPATH,"//input[@name='user']")
sleep(1)
campo_user.send_keys("----")
sleep(3)

campo_password = browser.find_element(By.XPATH,"//input[@name='pass']")
sleep(1)
campo_password.send_keys("----")
sleep(3)

botao_enter = browser.find_element(By.XPATH,"//button[@data-testid='login-submit']").click()
sleep(3)

browser.find_element(By.XPATH,"//span[@data-i18n='menu.frota.checklist.titulo']").click()
sleep(3)

browser.find_element(By.XPATH,"//a[@data-i18n='menu.frota.checklist.checklists_realizados']").click()
sleep(5)

browser.find_element(By.XPATH,"(//button[@class='banner-button-cockpit'])[1]").click()
sleep(3)


input("[ENTER] Selecione a data desejada no campo!\n Click em FILTRAR!")
sleep(3)

wait = WebDriverWait(browser, 10)

while True:
    try:
        botao_carregar = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='carregar']"))
        )

        botao_carregar.click()

        sleep(1)  # pequeno delay para os dados carregarem

    except TimeoutException:
        print("✅ Não há mais dados para carregar.")
        break

    except StaleElementReferenceException:
        # Caso o botão seja recriado pelo JS
        print("♻️ Botão recarregado pelo sistema, tentando novamente...")
        continue

input("[ENTER]...")
print("❌ Automação finalizada!")
