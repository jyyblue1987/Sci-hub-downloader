from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager

def load_driver():    
    chrome_options = ChromiumOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(chrome_options=chrome_options, service=service)

    return driver