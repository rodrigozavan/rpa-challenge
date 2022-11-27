from abc import ABC
from locators.Locators import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class PageElement(ABC):
    def __init__(self, driver, url:str=''):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.url = url

    def find_element(self, locator:tuple, timeout:int=15):
        """
        Find element present in the page
        
        Args:
            locator: tuple of locator the element
            timeout: maximum element wait time
        Return: 
            element
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.visibility_of_element_located(locator))
        return element

    def find_elements(self, locator:tuple, timeout:int=10) -> list:
        """
        Find all elements present in the page
        
        Args:
            locator: tuple of locator the element
            timeout: maximum element wait time
        Return: 
            list of elements
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.presence_of_all_elements_located(locator))
        return element

    def do_click(self, locator:tuple, timeout:int=15) -> None:
        """
        Click on the element from the past locator
        
        Args:
            locator: tuple of locator the element
            timeout: maximum element wait time
        Return: 
            None
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.element_to_be_clickable(locator))
        return element.click()
    
    def do_double_click(self, locator:tuple, timeout:int=15) -> None:
        """
        Double Click on the element from the past locator

        Args:
            locator: tuple of locator the element
            timeout: maximum element wait time
        Return: 
            None
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.element_to_be_clickable(locator))
        return self.actions.double_click(element).perform()

    def do_send_keys(self, locator:tuple, text_to_send:str, timeout:int=15) -> None:
        """
        Send text to element
        
        Args:
            locator: tuple of locator the element
            text_to_send: string to send
            timeout: maximum element wait time
        Return: 
            None
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(ec.visibility_of_element_located(locator), message="Element not found").send_keys(text_to_send)

    def get_text_to_element(self, locator:tuple, timeout:int=15):
        """
        Get text to element
        
        Args:
            locator: tuple of locator the element
            timeout: maximum element wait time
        Return: 
            element
        """
        wait = WebDriverWait(self.driver, timeout)
        element = str(wait.until(ec.visibility_of_element_located(locator)).text)
        return element

    def open(self) -> None:
        """
        Open the page.

        Return: 
            None
        """
        self.driver.get(self.url)
        return None