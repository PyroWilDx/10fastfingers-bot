import time
from keyboard import wait
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random

mail = "wipak35813@poetred.com"
password = "12345678909912002AZERTYHGFDSQWXCVBN"
login_url = "https://10fastfingers.com/login"
type_url = "https://10fastfingers.com/typing-test/french"

driver = webdriver.Chrome()

driver.get(login_url)

while True:
    try:
        cookie_button = driver.find_element_by_xpath("//*[@id=\"CybotCookiebotDialogBodyLevelButton"
                                                     "LevelOptinAllowAll\"]")
        driver.implicitly_wait(2.5)
        time.sleep(1)
        cookie_button.click()
        break
    except NoSuchElementException:
        pass

while True:
    try:
        mail_input = driver.find_element_by_xpath("//*[@id=\"UserEmail\"]")
        password_input = driver.find_element_by_xpath("//*[@id=\"UserPassword\"]")
        mail_input.send_keys(mail)
        password_input.send_keys(password)
        driver.find_element_by_xpath("//*[@id=\"login-form-submit\"]").click()
        break
    except NoSuchElementException:
        pass

while True:
    try:
        temp = driver.find_element_by_xpath("//*[@id=\"row1\"]/span[1]").text
        break
    except NoSuchElementException:
        pass

driver.get(type_url)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"
           "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "à", "î", "é", "è"]

wait_duration = random.uniform(0.0475, 0.055)
wrong_word_probability = random.uniform(0.035, 0.055)
word_correction_probability = random.uniform(0.0125, 0.025)

print(f"Wait Duration = {str(wait_duration*1000)[:4]} ms")
print(f"P(Wrong Word) = {str(wrong_word_probability*100)[:4]}%")
print(f"P(Word Correction) = {str(word_correction_probability*100)[:4]}%")

time.sleep(5)

i = 1

while True:
    try:
        word = driver.find_element_by_xpath(f"//*[@id=\"row1\"]/span[{i}]").text + " "
        input_entry = driver.find_element_by_xpath("//*[@id=\"inputfield\"]")
        if random.random() <= wrong_word_probability:
            input_entry.send_keys(word[:-2] + random.choice(letters) + " ")
        else:
            for c in word:
                input_entry.send_keys(c)
                time.sleep(wait_duration)
                if random.random() <= word_correction_probability:
                    input_entry.send_keys(random.choice(letters))
                    time.sleep(wait_duration)
                    input_entry.send_keys(Keys.BACKSPACE)
        i += 1
        if driver.find_element_by_xpath("//*[@id=\"timer\"]").text == "0:00":
            break
    except NoSuchElementException:
        while driver.find_element_by_xpath("//*[@id=\"timer\"]").text != "0:00":
            time.sleep(1)
            try:
                input_entry = driver.find_element_by_xpath("//*[@id=\"inputfield\"]")
                input_entry.send_keys("a")
            except NameError:
                pass
        break

time.sleep(10)

print("EZ")
