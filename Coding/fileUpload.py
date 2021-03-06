'''
Created on Jan 21, 2019

@author: siddardha.teegela
'''

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
import autoit

def rescale_upload():
    user = "sidhumeher@yahoo.co.in"
    pwd = "1055088S!dhu"
    
    # For Chrome
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome("C:/Users/siddardha.teegela/Downloads/Softwares/chromedriver.exe",options=opts)
    driver.get("https://platform.rescale.com/")
    
    #Find login
    element = driver.find_element_by_id("id_username")
    element.send_keys(user)
    
    element = driver.find_element_by_id("id_password")
    element.send_keys(pwd)
    
    element.send_keys(Keys.RETURN)
    
    time.sleep(3)
    #file_click = driver.find_element_by_id("menuFiles")
    file_click = driver.find_element_by_xpath("//*[@id='menuFiles']/a")
    file_click.click()
    
    time.sleep(10)
    
    try:
        upload_file = driver.find_element_by_xpath("//*[@id='filesPageDropZone']")
        upload_file.click()
        time.sleep(5)
        autoit.win_active("Open")
        autoit.control_send("Open", "Edit1",r"C:\Users\siddardha.teegela\Downloads\testdoc1.txt")
        autoit.control_send("Open","Edit1","{ENTER}")
    except Exception as e:
        print(e,'Could not upload file')
    
    time.sleep(50)
    
    #driver.close()

if __name__ == '__main__':
    #pass
    rescale_upload()