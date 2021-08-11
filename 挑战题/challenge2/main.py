"""
    挑战题2
"""
from selenium import webdriver
import re


def get_info(broswer, i):
    title = broswer.find_elements_by_css_selector(
        '#__01 > tbody > tr:nth-child(4) > td > div > div > ul > li:nth-child({}) > '
        'span.title >a'.format(i)).text
    date = broswer.find_elements_by_css_selector(
        '#__01 > tbody > tr:nth-child(4) > td > div > div > ul > li:nth-child({}) > '
        'span.hits >a'.format(i)).text
    publish_date = re.compile(r"\d{4}-\d{2}-\d{2}").findall(date)[0]
    url = broswer.find_elements_by_css_selector(
        '#__01 > tbody > tr:nth-child(4) > td > div > div > ul > li:nth-child({}) > '
        'span.title >a'.format(i)).get_attribute('href')
    with open('nfu_news.csv', 'w') as f:
        f.write('{:80},{:20},{}'.format(title, publish_date, url + '\n'))


def main():
    with open('njfu_news.csv', 'w') as f:
        f.write('{:80},{:20},{}'.format("文章名称", '发布时间', '对应链接\n'))
        browser = webdriver.Chrome(executable_path='chromedriver.exe')
        browser.get('https://news.njfu.edu.cn/ybdt/')
        for page in range(1, 68):
            for i in range(1, 20):
                get_info(browser, i)
            next_page = browser.find_elements_by_css_selector('#pages > a.next')
            next_page.click()


if __name__ == '__main__':
    main()
