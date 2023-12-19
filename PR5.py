import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions

count = 1
def get_url(url):


    optinons = ChromeOptions()
    optinons.add_argument('--headless=new')
    driver = webdriver.Chrome(options=optinons)
    #driver.get(url)
    driver.get(url=url)

    global count
    

    try:
        with open(f'page_source/page_source-{count}.html', 'w', encoding='UTF-8') as file:
            file.write(driver.page_source)
            count += 1
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def get_info(name, count_temp):
        global count
    # count_local = 1
    # while count_local <= 1:
        temp_day = []
        temp_night_1 = []
        time_day = []
        with open(f'page_source/page_source-{count_temp}.html', encoding='UTF-8') as file:
            src = file.read()
            #count_local += 1
        soup = BeautifulSoup(src, 'lxml')
        segodnya = soup.find(id = 'forecastTable_1_3')
        temp_all_day = segodnya.find_all('div', class_ = 't_0', limit= 78)
        time_all_day = segodnya.find('tr', class_ = 'forecastTime').find_all('td', 'underlineRow')
        count_time = 1
        for i in time_all_day:
            time_day.append(i.text)
            count_time += 1
        # for i in temp_all_day:
        #     temp_day.append(i.text)
        #     #print(i.text)

        #for i in temp_day:

        print(name, ' : ', time_day)
        print('Count = ', count_time)
        #print('Temperature: ', temp_n_1)

        





def main():
    global count
    list_city_rp5 = [
        {'Name' : 'Южно-Сахалинск', 'Url' : 'https://rp5.ru/Погода_в_Южно-Сахалинске'},
        {'Name' : 'Холмск', 'Url' : 'https://rp5.ru/Погода_в_Холмске'},
        {'Name' : 'Корсаков', 'Url' : 'https://rp5.ru/Погода_в_Корсакове'},
        {'Name' : 'Александровск-Сахалинский', 'Url' : 'https://rp5.ru/Погода_в_Александровске-Сахалинском'},
        {'Name' : 'Тымовск', 'Url' : 'https://rp5.ru/Погода_в_Тымовском'},
        {'Name' : 'Поронайск', 'Url' : 'https://rp5.ru/Погода_в_Поронайске'},
        {'Name' : 'Северо-Курильск', 'Url' : 'https://rp5.ru/Погода_в_Северо-Курильске'},
        {'Name' : 'Курильск', 'Url' : 'https://rp5.ru/Погода_в_Курильске'},
        {'Name' : 'Оха', 'Url' : 'https://rp5.ru/Погода_в_Охе'},
        {'Name' : 'Ноглики', 'Url' : 'https://rp5.ru/Погода_в_Ногликах'},
        {'Name' : 'Южно-Курильск', 'Url' : 'https://rp5.ru/Погода_в_Южно-Курильске'},
        {'Name' : 'Углегорск', 'Url' : 'https://rp5.ru/Погода_в_Углегорске,_Сахалинская_область'},
        {'Name' : 'Ильинск', 'Url' : 'https://rp5.ru/Погода_в_Ильинском,_Сахалинская_область'},
        {'Name' : 'Макаровск', 'Url' : "https://rp5.ru/Погода_в_Макарове,_Россия"}
    ]

    # for c in list_city_rp5:
    #     get_url(c['Url'])
    #     print(f'--Page-{c['Name']} done --')
    count_temp = 1
    #get_info()
    for c in list_city_rp5:
        get_info(name = c['Name'], count_temp = count_temp)
        count_temp += 1


if __name__ == '__main__':
    main()
