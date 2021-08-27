from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.color import Color
import random
import string
import  time
import re
import  rand_log_pas
driver = webdriver.Chrome(
    executable_path='./chromedriver'
)

"""Открыть главную страницу сайта Netpeak"""
driver.get("https://netpeak.ua/")

""" Нажать на кнопку 'О нас' и в выпавшем списке нажать кнопку 'Команда'"""
about_as_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]")
about_as_button.click()
command_button = driver.find_element_by_link_text("Команда")
command_button.click()

"""Нажать кнопку 'Стать частью команды' и убедится что в новой вкладке открылась страница Работа в Нетпик"""
add_to_command_button = driver.find_element_by_link_text("Стать частью команды")
add_to_command_button.click()
driver.switch_to.window(driver.window_handles[1])
print(f"Текущий адрес: {driver.current_url}")
pagge_name = driver.title
print("Имя страницы: '", pagge_name, "'")

"""Убедится что на странице есть кнопка "Я хочу работать в Netpeak" и на нее можно кликнуть."""
button = driver.find_element_by_link_text('Я хочу работать в Netpeak')
if button is None:
    is_here = False
    print("Кнопка 'Я хочу работать в Netpeak' нет!")
else:
    print("Кнопка 'Я хочу работать в Netpeak' существует")
href_data = button.get_attribute('href')
if href_data is None:
    is_clickable = False
    print("Кнопка 'Я хочу работать в Netpeak' не прожимается!")
else:
    print("Кнопка 'Я хочу работать в Netpeak' прожимается")

"""Вернутся на предыдущую вкладку и нажать кнопку "Личный кабинет"."""
driver.switch_to.window(driver.window_handles[0])
kabinet_button = driver.find_element_by_link_text("Личный кабинет")
kabinet_button.click()

"""На странице личного кабинета заполнить Логин и Пароль случайными данными. """
driver.switch_to.window(driver.window_handles[2])
login_button = driver.find_element_by_name("login")
login_button.send_keys(rand_log_pas.loginus)
pas_button = driver.find_element_by_name("password")
pas_button.send_keys(rand_log_pas.pas)

"""Проверить что кнопка "Войти" не доступна."""
enter_buton = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[5]/button")
if enter_buton.is_enabled():
    print("Баг - Кнопка 'Вход' может быть нажата!")
else:
    print("Кнопка 'Вход' не может быть нажата")

"""Отметить чекбокс 'Авторизируясь, вы соглашаетесь с Политикой конфиденциальности'"""
flag = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div/md-checkbox/div[1]")
flag.click()
enter_buton.click()

""""Проверка на наличие нотификации о неправильном логине или пароле."""
def check_exists_by_xpath(xpath):
    if len(driver.find_elements_by_xpath(xpath))>0:
        print("Наличие нотификацииустоновлено")
    else:
        print("Баг - элемент нотификации не найден!")

check_exists_by_xpath("/html/body/md-toast/div")

"""Проверить что Логин и Пароль подсветились красным цветом.  """
def LogColorCheck():
    rgb = driver.find_element_by_name("login").value_of_css_property('border-color')
    hex = Color.from_string(rgb).hex
    if hex != "#dd2c00":
        print("Баг! Цвет Логина - Не красный ", hex, "!")
    elif hex == "#dd2c00":
        print("Цвет Логина - Красный ", hex)
    else:
        print("Баг! Ошибка определения цвета!")
LogColorCheck()

def PasColorCheck():
    rgb1 = driver.find_element_by_name("password").value_of_css_property('border-color')
    hex1 = Color.from_string(rgb1).hex
    if hex1 != "#dd2c00":
        print("Цвет пароля - Не красный ", hex1, "!")
    elif hex1 == "#dd2c00":
        print("Цвет пароля - Красный ", hex1)
    else:
        print("Ошибка ", hex1)

PasColorCheck()
"""Завершение"""
print("Finish")
driver.quit()