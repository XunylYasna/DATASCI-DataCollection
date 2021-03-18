import json
from newsapi import NewsApiClient

apiKey = 'secret'
domains='bbc.co.uk'
fromDate = '2021-03-11'
toDate = '2021-03-12'
pageSize = 100


# Get JSON file
newsapi = NewsApiClient(api_key=apiKey)
all_articles = newsapi.get_everything(domains=domains,
                                      from_param=fromDate,
                                      to=toDate,
                                      language='en',
                                      page_size=pageSize)

# Get news Articles
newsArticles = all_articles['articles']

result = []
# Create new JSON
for article in newsArticles:
    source = article['source']
    date = article['publishedAt']
    title = article['title']
    content = article['content']
    author = article['author']
    result.append({
        'source': source,
        'date': date,
        'title': title,
        'content': content,
        'author': author
    })

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)