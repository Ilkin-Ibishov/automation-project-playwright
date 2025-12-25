import logging  
from utils.config import Config
class BasePage:
    def __init__(self, page):
        self.page = page
        self.config = Config()

    def click(self, locator:str) -> None:
        logging.info(f"Clicked on {locator}")
        self.page.click(locator)
    
    def type(self, locator:str, text:str) -> None:
        logging.info(f"Typed {text} in {locator}")
        self.page.fill(locator, text)
    
    def get_text(self, locator:str) -> str:
        logging.info(f"Getting text from {locator}")
        return int(self.page.inner_text(locator))
    
    def get_url(self) -> str:
        logging.info("Getting current URL")
        return self.page.url

    def go_to(self, url:str) -> None:
        logging.info(f"Navigating to {url}")
        self.page.goto(url)
    
    def wait_for(self, locator:str) -> None:
        logging.info(f"Waiting for {locator}")
        self.page.wait_for_selector(locator)

    def is_visible(self, locator:str) -> bool:
        logging.info(f"Checking visibility of {locator}")
        return self.page.is_visible(locator)
    
