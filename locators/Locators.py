from selenium.webdriver.common.by import By


class FormPageLocators(object):
    input_first_name = (By.CSS_SELECTOR, 'input[ng-reflect-name="labelFirstName"]')
    input_last_name = (By.CSS_SELECTOR, 'input[ng-reflect-name="labelLastName"]')
    input_email = (By.CSS_SELECTOR, 'input[ng-reflect-name="labelEmail"]')
    input_role_in_company = (By.CSS_SELECTOR, 'input[ng-reflect-name="labelRole"]')
    input_address = (By.CSS_SELECTOR, 'input[ng-reflect-name="labelAddress"]')
    input_phone_number = (By.CSS_SELECTOR, 'input[ng-reflect-name="labelPhone"]')
    input_company_name = (By.CSS_SELECTOR, 'input[ng-reflect-name="labelCompanyName"]')
    btn_submit = (By.CSS_SELECTOR, 'input[value="Submit"]')
    btn_start = (By.CSS_SELECTOR, 'button.uiColorButton')
    div_result = (By.CSS_SELECTOR, "div.message2")