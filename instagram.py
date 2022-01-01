from selenium import webdriver
# web driver location
driver = webdriver.Chrome('C:/Users/AHAD RAZA/Desktop/chromedriver.exe')
# instagram url(location)
driver.get('https://www.instagram.com/')
# wait for 5 seconds
driver.implicitly_wait(5)
#---> ENTER THE USERNAME ON LOGIN PAGE OF INSTAGRAM
driver.find_element_by_name('username').send_keys('a_ahadraza')
#---> ENTER THE PASSWORD ON LOGIN PAGE OF INSTAGRAM
driver.find_element_by_name('password').send_keys('hellodear')
#--> THIS IS LOCATION OF SIGN IN BUTTON OF LOGIN PAGE(INSTAGRAM
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()

driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()

# WAIT FOR 1 SECOND
driver.implicitly_wait(1)
# QUIT CHROME
driver.quit()
