from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER = './chromedriver'
BOOKOFF_URL = 'https://www.bookoffonline.co.jp//book/CSfTop.jsp?bg=12'

AUTHER_NAME = ''
WORK_NAME = 'ドストエフスキーとの旅'
PUBLISHER_NAME = ''

def bookoff_search(workname:str,authername:str='',publishername:str='',item_num:int=1):
    output_dict = {}
    SEARCH_WORD = workname + '　' + authername + '　' + publishername
    service = Service(executable_path=CHROMEDRIVER)
    
    
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=service,options=options)
    driver.implicitly_wait(10)
    driver.get(BOOKOFF_URL)
    
    driver.find_element(By.ID,'zsSearchFormInput').send_keys(SEARCH_WORD)
    driver.find_element(By.ID,'zsSearchFormButton').click()
    
    crnt_url = driver.current_url
    usedOrNew = driver.find_element(By.XPATH,f'//*[@id="anchor_link_{item_num}"]/img').get_attribute('alt')
    bookname_elements = driver.find_elements(By.XPATH,f'//*[@id="resList"]/form/div["{item_num + 3}"]/div[1]/p/a')
    price_elements = driver.find_elements(By.CLASS_NAME,'mainprice')
    price_word = price_elements[item_num - 1].text
    
    
    for i,word in enumerate(price_word) :
        if word == '（' :
            price_word = price_word[:i]
            break
    
    price_word = price_word.strip('￥') # price_word.strip('￥')はそのままではダメで、price_word = price_word.strip('￥')
    price_word = price_word.strip(',') #と代入する必要がある。

    

    # find_elements ではないので一番上の本だけが取得される。
    if workname == '' :
        print('Name is nessesary.')
    if WORK_NAME in bookname_elements[item_num - 1].text :
          
        output_dict = {
            'usedOrNew' : usedOrNew,
            'workname' : bookname_elements[item_num - 1].text,
            'price' : price_word,
            'url' : crnt_url
        }
    else :
        output_dict = {
            'usedOrNew' : 'No book',
            'workname' : 'No book',
            'price' : 'No book',
            'url' : crnt_url
        }
    return output_dict

if __name__ == '__main__':
    print(bookoff_search(WORK_NAME,AUTHER_NAME))
    

    # if WORK_NAME in work_name :    
    #     try :
    #         price_element = driver.find_element(By.XPATH,f'//*[@id="item-{item_num}"]/div/div[3]/span/span/div/div[1]')
    #     except :
    #         print('No')
    # //*[@id="item-2"]/div/div[3]/span/span/div/div[1]
    # //*[@id="item-3"]/div/div[3]/span/span/div/div[1]


    


    


    # AMAZON
    # driver.find_element(By.ID,"twotabsearchtextbox").send_keys(SEARCH_WORD)
    # driver.find_element(By.ID,'nav-search-submit-button').click()
    # element = driver.find_elements(By.CLASS_NAME,'a-declarative')
    
    
    

    
"""
btn = driver.find_element(By.ID,'nav-search-submit-button')
btn.click()

はダメで

btn = driver.find_element(By.ID,'nav-search-submit-button').click()

にする必要がある。
"""

