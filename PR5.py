import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions

def get_url(url):


    optinons = ChromeOptions()
    #optinons.add_argument('--headless')
    driver = webdriver.Chrome(options=optinons)
    #driver.get(url)
    driver.get(url=url)

    try:
        with open('page_source/page_source.html', 'w', encoding='UTF-8') as file:
            file.write(driver.page_source)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def get_info():

    with open('page_source/page_source.html', 'r') as file:
        src = file.read()


def main():
    get_url('https://rp5.ru/Погода_в_Южно-Сахалинске')


if __name__ == '__main__':
    main()
