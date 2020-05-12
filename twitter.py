from selenium import webdriver
import pandas as pd
print('Welcome to Tweakter - A Twitter Automation')

auto=input('Use auto-login(For Old users)(Y/N):')
if(auto == 'Y' ):
    f= open('Data.txt','r')
    Uname= f.readline()
    Pass= f.readline()
    f.close()
elif(auto=='N'):    
    Uname=input('Twitter Username: ')
    Pass=input('Twitter Password: ')
    choice=input('Save details for auto-login?(Y/N):')
    if (choice=='Y'):
        f= open('Data.txt','w')
        f.write(Uname)
        f.write('\n')
        f.write(Pass)
        f.close()
        
browser= webdriver.Chrome()
browser.get('https://twitter.com/login')
    
username= browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
username.send_keys(Uname)
password= browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys(Pass)
login= browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
login.click()


