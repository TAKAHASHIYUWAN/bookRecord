import requests
import json

AUTHOR = 'ドストエフスキー'
TITLE = 'カラマーゾフの兄弟'
API_AUTHOR = 'inauthor:' + AUTHOR
API_TITLE = 'intitle:' + TITLE

GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes?q={}+{}'.format(API_AUTHOR,API_TITLE)

OPENBD_AIP_URL = 'https://api.openbd.jp/v1/get?isbn='

def isbnSearch(TITLE):
    API_TITLE = 'intitle:' + TITLE

    GOOGLE_BOOK_API_URL = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(API_TITLE)
    
    resp = requests.get(GOOGLE_BOOK_API_URL).json()
    items_list = resp['items']
    resp_dict = []
    for num,item in enumerate(items_list) :
        for identify in item['volumeInfo']['industryIdentifiers']:
            if identify['type'] == 'ISBN_13':
                resp_dict.append(identify['identifier'])

    return resp_dict        
    """
    resp_dict = []
    for content in items_list :
        n = 0
        while n != 2:
            if content['volumeInfo']['industryIdentifiers'][n]['type'] == 'ISBN_13':
                resp_dict.append(content['volumeInfo']['industryIdentifiers'][n]['identifier'])
            n += 1
    
    return resp_dict
    """

def imageSearch(isbns:dict) -> dict :
    out_dict = []
    for isbn in isbns:
        res = requests.get(OPENBD_AIP_URL + isbn).json()
        
        if res[0] != None  and res[0]['summary']['cover'] != '':
            res = res[0]['summary']['cover']
            out_dict.append(res)
    return out_dict

    """
        if res[0] != None:
            out_dict.append(res[0]['onix']['CollateralDetail']['SupportingResource'][0]['ResourceVersion'][0]['ResourceLink'])
    
    return out_dict
    """
    
    """
    res = requests.get(OPENBD_AIP_URL + isbn).json()
    if res[0] != None:
        out = res[0]['onix']['CollateralDetail']['SupportingResource'][0]['ResourceVersion'][0]['ResourceLink']
    # out = res[0]['CollateralDetail']['SupportingResource']['ResourceLink']
        return out
    return None
    """
if __name__ == '__main__':
    print(imageSearch(isbnSearch(TITLE)))
    

"""
jpegで保存する場合は次のようにする。

-----1-----
response = requests.get(image_url)
image = response.content

-----2-----
file_name = '0124820198490509093.jpg'

with open(file_name, 'wb') as f :
    f.write(image)
"""

