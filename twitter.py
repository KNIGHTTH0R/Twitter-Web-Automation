from selenium import webdriver

Uname=input('Twitter Username: ')
Pass=input('Twitter Password: ')

browser= webdriver.Chrome()
browser.get('https://twitter.com/login')
    
username= browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
username.send_keys(Uname)
password= browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys(Pass)
login= browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
login.click()


