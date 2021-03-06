from pyquery import PyQuery
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WYMusicCrawler:
    home_url = 'https://music.163.com/'

    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def searchMusic(self, keyword):
        self.driver.get(self.home_url)
        input_form = self.driver.find_element_by_id('srch')
        input_form.send_keys(keyword + '\n')
        self.driver.switch_to.frame('contentFrame')

        music_eles = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item.f-cb')))
        musics = []
        for music_ele in music_eles:
            name = music_ele.find_element_by_css_selector('.w0').text
            url = music_ele.find_element_by_css_selector('.w0 a').get_attribute('href')
            author = music_ele.find_element_by_css_selector('.w1').text
            music = WYMusic(name, url, author)
            musics.append(music)

        return musics

    def getLyric(self, html):
        doc = PyQuery(html)
        lyric_ele = doc('#lyric-content')
        lyric_ele.remove('a')
        lyric = lyric_ele.text()
        return lyric

    def getComment(self, html):
        doc = BeautifulSoup(html, features="lxml")
        comments = []
        comment_eles = doc.find_all(class_='itm')

        for comment_ele in comment_eles:
            comment = comment_ele.find(class_='cnt').text
            comments.append(comment.split())
        return comments

    def turunPage(self, url, max_page=20):
        comments = []
        self.driver.get(url)
        self.driver.switch_to.frame('contentFrame')
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.m-cmmt')))
        switch = True
        cur_page = 1
        while switch:
            html = self.driver.page_source
            comments.append(self.getComment(html))
            nxt_btn = self.driver.find_element_by_class_name('znxt')
            if 'js-disabled' in nxt_btn.get_attribute('class'):
                switch = False
            elif cur_page > max_page:
                switch = False
            else:
                self.driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")
                nxt_btn.click()
                cur_page += 1
                self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.m-cmmt .cnt')))
        return comments


class WYMusic:

    def __init__(self, name, url, author, album='', time='') -> None:
        self.name = name
        self.url = url
        self.author = author
        self.time = time
        self.album = album
