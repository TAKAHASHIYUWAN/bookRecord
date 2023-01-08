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


def imageSearch(isbns:dict) -> dict :
    out_dict = []
    for isbn in isbns:
        res = requests.get(OPENBD_AIP_URL + isbn).json()
        
        if res[0] != None  and res[0]['summary']['cover'] != '':
            res = res[0]['summary']['cover']
            out_dict.append(res)
    return out_dict


if __name__ == '__main__':
    print(imageSearch(isbnSearch(TITLE)))
    



