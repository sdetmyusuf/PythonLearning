from selenium import webdriver
from selenium.webdriver.chrome.service import Service
servObj = Service("C:\\Users\\Mohd Yusuf\\.cache\\selenium\\chromedriver\\win64\\115.0.5790.170\chromedriver.exe")
driver = webdriver.Chrome(servObj)
driver.get("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
