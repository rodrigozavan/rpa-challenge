from locators.Locators import *
from .BasePage import PageElement


class FormPage(PageElement):

    def send_first_name(self, first_name:str) -> None:
        """
        Send the first name
        
        Args:
            first_name: str containing the first name
        Return: 
            None
        """
        self.do_send_keys(FormPageLocators.input_first_name, first_name)

    def send_last_name(self, last_name:str) -> None:
        """
        Send the last name
        
        Args:
            last_name: str containing the last name
        Return: 
            None
        """
        self.do_send_keys(FormPageLocators.input_last_name, last_name)

    def send_email(self, email:str) -> None:
        """
        Send the email
        
        Args:
            email: str containing the email
        Return: 
            None
        """
        self.do_send_keys(FormPageLocators.input_email, email)

    def send_role(self, role:str) -> None:
        """
        Send the role in the company
        
        Args:
            role: str containing the role in the company
        Return: 
            None
        """
        self.do_send_keys(FormPageLocators.input_role_in_company, role)

    def send_address(self, address:str) -> None:
        """
        Send the address
        
        Args:
            address: str containing the address
        Return: 
            None
        """
        self.do_send_keys(FormPageLocators.input_address, address)

    def send_phone(self, phone:str) -> None:
        """
        Send the phone number
        
        Args:
            phone: str containing the phone number
        Return: 
            None
        """
        self.do_send_keys(FormPageLocators.input_phone_number, phone)

    def send_company_name(self, company_name:str) -> None:
        """
        Send the company name
        
        Args:
            company_name: str containing the company name
        Return: 
            None
        """
        self.do_send_keys(FormPageLocators.input_company_name, company_name)
    
    def submit_form(self) -> None:
        """
        Click on submit form button
        
        Args:
        
        Return: 
            None
        """
        self.do_click(FormPageLocators.btn_submit)

    def start_challenge(self) -> None:
        """
        Click on start challenge button
        
        Args:

        Return: 
            None
        """
        self.do_click(FormPageLocators.btn_start)
    
    def print_result(self) -> None:
        """
        Print the result
        
        Args:

        Return: 
            None
        """
        result = self.get_text_to_element(FormPageLocators.div_result)
        print(result)
