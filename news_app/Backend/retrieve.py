import requests

def getNews():
    api_key = "5a2ec5b716fb43b88bc51065b6fb1a81"

    wall_st_url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey="+api_key
    tech_crunch_head_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="+api_key
    us_business_head_url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey="+api_key
    tesla_articles_url = "https://newsapi.org/v2/everything?q=tesla&from=2025-07-31&sortBy=publishedAt&apiKey="+api_key
    apple_articles_url = "https://newsapi.org/v2/everything?q=apple&from=2025-08-30&to=2025-08-30&sortBy=popularity&apiKey="+api_key

    wall_st_journal = requests.get(wall_st_url).json()
    tech_crunch_head = requests.get(tech_crunch_head_url).json()
    us_business_head = requests.get(us_business_head_url).json()
    tesla_articles = requests.get(tesla_articles_url).json()
    apple_articles = requests.get(apple_articles_url).json()
    
    journals = wall_st_journal['articles']

    my_journals = []
    my_news = " "

    for journal in journals:
        my_journals.append(journal['title'])

    for i in range(10):
        my_news = my_news + my_journals[i] + "\n"
    

getNews()