## News Automator Python Project

---

**Project description**

The News Automator is a Python project designed to streamline the process of gathering, processing, and presenting news articles from various sources using the News API. This project aims to provide the user with a convenient way to access up-to-date news content tailored to their preferences, all within a single application.

---

Import the necessary libraries

```python
import requests
from sys import argv
```
---

Provide the url to the API and the API key.

```python
url = 'https://newsapi.org/v2/top-headlines?'
api_key = 'api_key_code' # I don't write the actual API key here because it's connected to my accounts on newsapi.org
```
---

Create the function _get_articles, that prints titles and urls of the articles based on given parameters

```python
def _get_articles(params):
    response = requests.get(url, params=params)
    articles = response.json()['articles']
    
    results = []
    
    for article in articles:
        results.append({'title':article['title'], 'url':article['url']})
        
    for result in results:
        print(result['title'])
        print(result['url'])
```
---

Create the function get_articles_by_category, that calls the function _get_articles with parameters based on a category

```python
def get_articles_by_category(category):
    query_parameters = {'category' : category,
                       'sortBy' : 'top',
                       'country' : 'it',
                       'apiKey' : api_key,
                       'pageSize' : 10}
    return _get_articles(query_parameters)
```
---

Create function get_articles_by_query, that calls the function _get_articles with parameters based on a query

```python
def get_articles_by_query(query):
    query_parameters = {'q' : query,
                       'sortBy' : 'top',
                       'country' : 'it',
                       'apiKey' : api_key,
                       'pageSize' : 10}
    return _get_articles(query_parameters)
```
---

Create function get_sources_by_category, that prints titles and urls of the sources where News API gets its information from
```python
def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    
    query_parameters = {'category': category,
                        'apiKey': api_key,
                       'pageSize' : 10}

    response = requests.get(url, params=query_parameters)
    sources = response.json()['sources']

    for source in sources:
        print(source['name'])
        print(source['url'])
```
---

In this cell the program is run:
1. Ask the user what action he wants to execute
2. Run the function that corresponds to the user's input

```python
print("Digit the number of the operation you want to execute:")
print("1) Get articles by category")
print("2) Get articles by query")
print("3) Get sources by category")

operation = int(input())

if operation == 1:
    category = input('What argument do you want to search? ')
    get_articles_by_category(category)
elif operation == 2:
    query = input('What argument do you want to search? ')
    get_articles_by_query(query)
elif operation == 3:
    category = input('What category do you want to search? ')
    get_sources_by_category(category)
else:
    print('Invalid input')
```

---

**Final considerations**

* This project has not only been useful for aggregating news but has also provided a practical learning experience in API integration.
* Moreover, the project has significant potential for future expansion, allowing for the incorporation of additional features and functionalities to further enhance its utility and educational value, for example incorporating a machine learning reccomendation system which finds out news the user might be interested in.
