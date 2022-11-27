from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager
from pages.FormPage import FormPage
from selenium import webdriver
from utils.utils import read_excel
from time import sleep


rows = read_excel("challenge.xlsx")

service_chrome = ServiceChrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_chrome)
driver.maximize_window()

form_page = FormPage(driver, url="https://rpachallenge.com/")
form_page.open()
form_page.start_challenge()

for row in rows:
    form_page.send_first_name(row["first_name"])
    form_page.send_last_name(row["last_name"])
    form_page.send_company_name(row["company_name"])
    form_page.send_role(row["role_in_company"])
    form_page.send_address(row["address"])
    form_page.send_email(row["email"])
    form_page.send_phone(row["phone_number"])
    form_page.submit_form()

form_page.print_result()
sleep(5)