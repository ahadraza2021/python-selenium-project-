from selenium import webdriver
driver = webdriver.Chrome('C:/Users/AHAD RAZA/Desktop/chromedriver.exe')
driver.get('https://www.jotform.com/build/212422741648454#preview')
driver.find_element_by_xpath('//*[@id="first_11"]').send_keys('ABDUL')
driver.find_element_by_xpath('//*[@id="middle_11"]').send_keys('AHAD')
driver.find_element_by_xpath('//*[@id="last_11"]').send_keys('RAZA')
driver.find_element_by_xpath('//*[@id="input_18_month"]').send_keys('December')
driver.find_element_by_xpath('//*[@id="input_18_day"]').send_keys('10')
driver.find_element_by_xpath('//*[@id="input_18_year"]').send_keys('2002')
driver.find_element_by_xpath('//*[@id="input_16_addr_line1"]').send_keys('HOUSE NO-102/H NAI ABADHI TALI MORI RAWALPINDI')
driver.find_element_by_xpath('')