#IMPORT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
import os

#Define starting url
url = 'Your_URL'

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
    page = soup.find('tag', {'class': 'class name'})
    if not page.find('tag', {'something to find it': 'value'}):
        url = 'website starting url' + str(page.find('tag', {'identifier': 'value'})['href'])
        return url
    else:
        return
        
#Takes in soup and returns all info wanted from it
def find_things(soup):
    #inspect reqired web page and put html tags and classes wanted inside quotes
    things = soup.find_all('div', class_ = 'dkr2t82')

    #loop for each thing in the list of thing
    for index, thing in enumerate(things):      
        #list of requirements can be made here and "a" is a varibale can be changed to go deeper into specific tags if needed
        requirement1 = thing.find('tag', class_ = 'value').a.a.text

        if 'condition1' in requirement1:
            
            #this is where you put things that you want to print
            address = thing.find('tag', class_ = 'value').text.replace('  ','')

            #now to find links to those websites
            link = thing.find('tag', class_ = 'value').a['href']

            path = 'c:/Users/godfreyantomarlin/Downloads/Python_projects/Web_Scraper'
            file_name = "things.txt"
            
            #this is where you print outputs using f.write instead if the usual print
            f = open(file_name, 'a')
            f.write(f"{address}: website.co.uk{link} \n \n")
            f.close()

            print(f"file saved: {index}")

#Brings together other functions to check all pages of website
def find_all_things(url):
    while url:
        soup = get_soup(url)
        find_things(soup)
        url = get_next_page(soup)

#MAIN PROGRAM
if __name__ == '__main__':
    counter = 1
    
    #Loop Indefinitely
    while True:
        #Edit File of info
        f = open("file name.txt", 'a')
        f.write(f"\n \n Search Number {counter} \n")
        f.close()
        
        #Run Scraping Program
        find_all_things(url)
        
        #Extra Stuff to loop forever and sleep in between
        time_wait_min = 10
        print(f"waiting {time_wait_min} minutes...")
        time.sleep(time_wait_min * 60)
        counter += 1







