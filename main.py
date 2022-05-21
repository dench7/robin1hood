import re
from multiprocessing import Pool
from random import choice

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument("--mute-audio")
options.add_argument("--disable-blink-features")
options.add_argument('--profile-directory=Default')
options.add_argument("--mute-audio")
options.add_extension("anticaptcha.crx")

acc = 100 
o = ("1")
mail42 = o * acc
api = ("") #ApiKey 




def work(mail43):
    try:
        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
        wait = WebDriverWait(driver, 30)
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.get("chrome-extension://lncaoejhfdpcafpkkcddpjnhnodcajfg/options.html")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="account_key"]'))).send_keys(
            "7231b6668f311c5a4eb28ef1a1ea6903")
        wait.until(EC.element_to_be_clickable((By.ID, 'auto_submit_form'))).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'delay_onready_callback'))).click()
        wait.until(EC.element_to_be_clickable(
            (By.ID, 'run_explicit_invisible_hcaptcha_callback_when_challenge_shown'))).click()
        save = driver.find_elements_by_class_name("save_button")
        wait.until(EC.element_to_be_clickable((save[0]))).click()
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[0])
        driver.get("https://robinhood.com/web3-wallet/e3d6e103")
        time.sleep(1)# Реф.ссылка
        mail = "".join([choice("abcdefghijklmnopqrstuvwxyz013456789") for _ in range(15)]) + ("@gmail.com")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-nw7ehx'))).send_keys(mail)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-1vswmk6-UnstyledButton'))).click()
        u = 0
        j = 0
        while u == 0:
            if j != 40:
                try:
                    driver.find_element_by_class_name("css-p7hvk2")
                    u = u + 1
                    j = 30
                except:
                    print(j)
                    time.sleep(1)
                    j = j + 1
            elif j == 40:
                driver.close()
                work(j)
        print("Акк зареган")
        time.sleep(2)











    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=1) 
    p.map(work, mail42)
