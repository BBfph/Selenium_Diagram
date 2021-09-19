import time
import json
import datetime
import xpath_store 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def Open_firefox():
    driver = webdriver.Firefox()
    url = "https://koronavirus.gov.hu/"
    driver.get(url) 
    return driver

# current request date
def get_time():
    x = datetime.datetime.now()
    x = x.strftime("%Y/%m/%d")
    return x

def write_json(data, filename="Info.json"):
        with open (filename, "w") as f:
            json.dump(data, f, indent=4)

def get_info_json(json_data):

    with open ("Info.json") as json_file:
        data = json.load(json_file)
        temp = data["Data"]
        temp.append(json_data)
    write_json(data)


def Getting_items(Browser):
    # coolect json informations (get)
    _json_data = {
        "Time": get_time(), 
        "Beoltottak": Browser.find_element_by_xpath(xpath_store.Beoltottak_xpath).text.replace(" ", ""),
        "Aktivfertozottek videk": Browser.find_element_by_xpath(xpath_store.Aktívfertőzöttek_videk_xpath).text.replace(" ", ""),
        "Aktivfertozottek budapest": Browser.find_element_by_xpath(xpath_store.Aktívfertőzöttek_budapest_xpath).text.replace(" ", ""),
        "Gyogyultak videk": Browser.find_element_by_xpath(xpath_store.Gyógyultak_vidék_xpath).text.replace(" ", ""),
        "Gyogyultak budapest": Browser.find_element_by_xpath(xpath_store.Gyógyultak_budapest_xpath).text.replace(" ", ""),
        "Elhunytak videk": Browser.find_element_by_xpath(xpath_store.Elhunytak_vidék_xpath).text.replace(" ", ""),
        "Elhunytak budapest": Browser.find_element_by_xpath(xpath_store.Elhunytak_budapest_xpath).text.replace(" ", ""),
        "Hatosagi hazikaranten": Browser.find_element_by_xpath(xpath_store.Hatósági_házikarantén_xpath).text.replace(" ", ""),
        "Mintavetel": Browser.find_element_by_xpath(xpath_store.Mintavétel_xpath).text.replace(" ", "")
    }
    # upload to Info.json file
    get_info_json(_json_data)

    

def main():
    Browser = Open_firefox()    #open browser
    time.sleep(1)
    Browser.execute_script("window.scrollTo(0, 2200)") # scroll where data is becouse website don't load at the top 
    time.sleep(1)
    
    Getting_items(Browser) # info handeling
    #close browser
    Browser.close()



if __name__ == '__main__':
    main()
    