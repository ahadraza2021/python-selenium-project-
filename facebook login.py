from selenium import webdriver
driver=webdriver.Chrome('C:/Users/AHAD RAZA/Desktop/chromedriver.exe')
driver1 = driver.get('https://www.facebook.com/')
english = driver.find_element_by_xpath('//*[@id="pageFooter"]/ul/li[2]/a')
english.click()
username = driver.find_element_by_id('email').send_keys('abdulahadraza02@gmail.com')
password = driver.find_element_by_id('pass').send_keys('a_ahadrazaofficial')
login = driver.find_element_by_name('login').click()