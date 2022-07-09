from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from newspaper import Article
from newspaper import Article
import nltk

nltk.download('punkt')
site = 'https://news.google.com/rss/search?q=politics'
op = urlopen(site)
rd = op.read()
op.close()

sp_page = soup(rd,'xml')
news_list = sp_page.find_all('item')
print(news_list)

for news in news_list:
    print('Title: ',news.title.text)
    print('News Link: ',news.link.text)
    news_data = Article(news.link.text)
    news_data.download()
    news_data.parse()
    news_data.nlp()
    print("News Summary: ", news_data.summary)
    print("News Poster Link: ", news_data.top_image)
    print("Pub date: ", news.pubDate.text)
    print('-' * 60)
