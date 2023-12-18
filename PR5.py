import requests
from selenium import webdriver

def get_url(url):
    driver = webdriver.Chrome()
    #driver.get(url)
    driver.get(url=url)

    with open('page_source\page_source.html', 'w', encoding='UTF-8') as file:
        
        file.write(driver.page_source)


def main():
    get_url('https://rp5.ru/Погода_в_Южно-Сахалинске')


if __name__ == '__main__':
    main()
