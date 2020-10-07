from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import datetime



def search_price_exsist(code):
    browser.get('https://exist.ua')
    time.sleep(2)
    browser.find_element_by_class_name('new-search-toggler-body').click()
    search = browser.find_element_by_class_name('multi-search-input')
    # find_elements will give us the list of all elements with id as subjectInput
    search.send_keys(code)
    time.sleep(2)
    try:
        data = browser.find_element_by_class_name('price').text.split()[0]
        return data
    except:
        data = None
        return data

def search_price_ukrparts(code):
    browser.get('https://ukrparts.com.ua')
    time.sleep(2)
    search = browser.find_element_by_id('artnum')
    # find_elements will give us the list of all elements with id as subjectInput
    search.send_keys(code)
    time.sleep(2)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    try:
        data = browser.find_element_by_class_name('price_min').text.split(': ')[1]
        return data
    except:
        data = None
        return data

def search_price_dok(code):
    browser.get('https://dok.ua')
    time.sleep(2)
    search = browser.find_element_by_id('search_with-hints')
    # find_elements will give us the list of all elements with id as subjectInput
    search.send_keys(code)
    time.sleep(2)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element_by_class_name('search-result-shortlist-item__title').click()
    time.sleep(2)
    data = browser.find_element_by_class_name('search-result__price').text.split()[0]
    # browser.quit()
    return data



if __name__ == "__main__":
    df = pd.read_excel('C:/Users/Admin/Desktop/iparts/listcode.xlsx', dtype=str)
    code = [x for x in df['art']]
    fullcode = [x + ' ' + y for x, y in zip(df['brand'], df['art'])]

    browser = webdriver.Chrome('D:\Downloads\chromedriver_win32\chromedriver.exe')
    df['dok'] = '0'
    df['ukrparts'] = '0'
    df['exsist'] = '0'
    ind = 0
    for i in fullcode:
        df['dok'][ind] = search_price_dok(i)
        ind += 1
    ind = 0
    for i in code:
        df['ukrparts'][ind] = search_price_ukrparts(i)
        ind += 1
    ind = 0
    for i in code:
        df['exsist'][ind] = search_price_exsist(i)
        ind += 1
    browser.quit()
    print(df.head())
    df.to_excel('analise.xlsx', index=False)