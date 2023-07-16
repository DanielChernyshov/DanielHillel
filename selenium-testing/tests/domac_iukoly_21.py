import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
import string


def random_char(char_num):
   return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


def test_number_1():
   browser = webdriver.Chrome()
   browser.get("https://guest:welcome2qauto@qauto.forstudy.space")
   sign_in = browser.find_element(By.XPATH, "//button[@class='btn btn-outline-white header_signin']")
   sign_in.click()
   registration = browser.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[1]")
   registration.click()
   first_name = browser.find_element(By.ID, "signupName")
   first_name.send_keys("Vasyl")
   last_name = browser.find_element(By.ID, "signupLastName")
   last_name.send_keys("Holoborodko")
   email = browser.find_element(By.ID, "signupEmail")
   email.send_keys(random_char(7)+"@gmail.com")
   password = browser.find_element(By.ID, "signupPassword")
   password.send_keys("Iamgod2009")
   re_password = browser.find_element(By.ID, "signupRepeatPassword")
   re_password.send_keys("Iamgod2009")
   register = browser.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")
   register.click()
   time.sleep(3)
   add_car = browser.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button")
   add_car.click()
   add_mileage = browser.find_element(By.ID, "addCarMileage")
   add_mileage.send_keys(1)
   add_button = browser.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]")
   add_button.click()
   time.sleep(3)
   browser.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/div/a[1]").click()
   first_element = browser.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-profile/div/div[2]/div/p")
   assert first_element.text() == "Vasyl Holoborodko"
   add_expense_button = browser.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div[1]/div[2]/button[2]")
   add_expense_button.click()
   new_mileage = browser.find_element(By.ID, "addExpenseMileage")
   new_mileage.send_keys(Keys.ARROW_UP)
   time.sleep(10)
   new_mileage.send_keys(5)
   time.sleep(5)
   # number_of_liters = browser.find_element(By.ID, "addExpenseLiters")
   # number_of_liters.send_keys(random.randrange(2,20))
   # add_cost = browser.find_element(By.ID,"addExpenseTotalCost")
   # add_cost.send_keys(random.randrange(2,20))
   # add_expense = browser.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
   # add_expense.click()
   # time.sleep(3)
   #
   # time.sleep(5)

