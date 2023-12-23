#IMPORT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
import os

#Define starting url
url = 'https://www.zoopla.co.uk/for-sale/houses/edinburgh/?beds_min=3&property_sub_type=detached&property_sub_type=terraced&property_sub_type=semi_detached&q=Edinburgh&results_sort=newest_listings&search_source=for-sale'

#Gets HTML data from web page and turns it into soup
def get_soup(url):
    #put reqired website url in quotes
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url);
    html_text = driver.page_source
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup

#Gets url for next page
def get_next_page(soup):
    page = soup.find('div', {'class': '_12n5fe22'})
    if not page.find('a', {'aria-disabled': 'true'}):
        url = 'https://www.zoopla.co.uk' + str(page.find('a', {'aria-disabled': 'false'})['href'])
        return url
    else:
        return
        
#Takes in soup and returns all info wanted from it
def find_houses(soup):
    #inspect reqired web page and put html tags and classes wanted inside quotes
    houses = soup.find_all('div', class_ = 'dkr2t82')

    #loop for each house in the list of houses
    for index, house in enumerate(houses):      
        #list of requirements can be made here and "a" is a varibale can be changed to go deeper into specific tags if needed
        requirement1 = house.find('li', class_ = '_1wickv1').svg.next_sibling.text

        if '3' in requirement1:
            
            #this is where you put things that you want to print
            address = house.find('address', class_ = 'm6hnz62 _1cvp8fm9').text.replace('  ','')

            #now to find links to those websites
            link = house.find('div', class_ = '_1lw0o5c0').a['href']

            path = 'c:/Users/godfreyantomarlin/Downloads/Python_projects/Web_Scraper'
            file_name = "houses.txt"
            
            #this is where you print outputs using f.write instead if the usual print
            f = open(file_name, 'a')
            f.write(f"{address}: zoopla.co.uk{link} \n \n")
            f.close()

            print(f"file saved: {index}")

#Brings together other functions to check all pages of website
def find_all_houses(url):
    while url:
        soup = get_soup(url)
        find_houses(soup)
        url = get_next_page(soup)

#MAIN PROGRAM
if __name__ == '__main__':
    counter = 1
    
    #Loop Indefinitely
    while True:
        #Edit File of info
        f = open("houses.txt", 'a')
        f.write(f"\n \n Search Number {counter} \n")
        f.close()
        
        #Run Scraping Program
        find_all_houses(url)
        
        #Extra Stuff to loop forever and sleep in between
        time_wait_min = 10
        print(f"waiting {time_wait_min} minutes...")
        time.sleep(time_wait_min * 60)
        counter += 1
