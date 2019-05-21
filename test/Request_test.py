import  requests
from bs4 import BeautifulSoup
#获取电影名（包括中文英文港台名)
def get_movie_name():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': "movie.douban.com"
    }
    movies_list = []
    for i in range(0,10):
        WebPage = "https://movie.douban.com/top250?start="+str(i*25)+"&filter="
        r = requests.get(WebPage,headers=headers,timeout = 20)
        soup = BeautifulSoup(r.text,'lxml')
        div_list = soup.find_all('div',class_ = 'hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movies_list.append(movie)
    return movies_list
def get_movie_Ename():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': "movie.douban.com"
    }
    movies_list = []
    for i in range(0, 10):
        WebPage = "https://movie.douban.com/top250?start=" + str(i * 25) + "&filter="
        r = requests.get(WebPage, headers=headers, timeout=20)
        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.contents[3].text.strip()
            movie = movie[2:]
            movies_list.append(movie)
    return movies_list
movies = get_movie_Ename()
print(movies)