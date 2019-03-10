import requests
from bs4 import BeautifulSoup


class Loader:
    def getContent(self):
        return content


class FileLoader(Loader):

    def __init__(self, file_path='file.txt') -> None:
        global content
        with open(file_path, encoding='utf-8') as file:
            content = file.read()


class UrlLoader(Loader):

    def __init__(self, url) -> None:
        global content
        response = requests.get(url)
        text = response.text
        doc = BeautifulSoup(text, features='html.parser')
        for d in doc('head'):
            d.extract()
        for d in doc('meta'):
            d.extract()
        for d in doc('script'):
            d.extract()
        content = doc.text
