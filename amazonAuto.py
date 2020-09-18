from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\antri\\AppData\\Local\\Programs\\Python\\Python38-32\\chromedriver.exe")
driver.get("https://www.facebook.com/?stype=lo&jlou=AffnhJdYXNqyQ3zbBI7VoDj3MWmFPfxPH8qdbOcHkjF6fFe-5sIbm7Y6EFtBRVRw2-Y1fT3vWaQOnIuScSCmaKay59cvvjF-1SmnecL9p2iaWw&smuh=19647&lh=Ac9jJMaQLxrL7zdf")
driver.find_element_by_id("email").send_keys("misriantriksh@gmail.com")
driver.find_element_by_id("pass").send_keys("Infraknight@1234")
driver.find_element_by_name("login").click()
