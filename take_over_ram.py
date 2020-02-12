from selenium import webdriver

import downloader
import time

#The lenght needs to be at least than 1
#Script will wait for the first tab to load before trying to load the others idk why 
#if you close the terminal , alll the chrome tabs will die too
to_open_per_window = ['https://google.com',"https://lttstore.com","https://reddit.com"]
number_of_windows = 5
time_between_tabs = 0 #in seconds
time_between_windows = 0 
wait_after_each_window = False #change this to "True" if you wanna press enter after each window

def main():
    downloader.check_for_driver()
    drivers = []
    for i in range(number_of_windows):
        new_driver = webdriver.Chrome('chromedriver')
        drivers.append(new_driver)
        per_page(new_driver)
        print("Window Opened: " + str(i+1))
        print("Number of tabs " + str((i+1)*len(to_open_per_window)))
        time.sleep(time_between_windows)
        if(wait_after_each_window):
            input()
    
def per_page(driver):
    driver.get(to_open_per_window[0])
    for url in to_open_per_window[1:]:
        driver.execute_script("window.open('" + url + "');")
        time.sleep(time_between_tabs)

if  __name__ == "__main__":
    main()
    input()