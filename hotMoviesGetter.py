from urllib import request
#import urllib2
from bs4 import BeautifulSoup

with request.urlopen('http://movie.douban.com') as f:
#with urllib2.urlopen('http://movie.douban.com') as f:
    soup = BeautifulSoup(f.read())
    #print(soup.decode('utf-8'))
    
    div_hot = soup.find('div', {"id":"screening"})
    for i in div_hot.find_all('li', class_='title'):
        movie_title = i.a.get_text()
        #movie_title = movie_title.strip()
        print(movie_title)
'''
    print("\n豆瓣近期热门： ")
    div_new = soup.find('div', {"id":"new-movies"})
    for i in div_new.find_all('li', class_='title'):
        movie_new = i.a.get_text()
        print(movie_new)
'''

