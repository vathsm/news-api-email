import requests

api_key = "2e5eb05f27204009a2b333f316ebcf05"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2024-01-29&sortBy=publishedAt&apiKey=" \
    "2e5eb05f27204009a2b333f316ebcf05"

requests = requests.get(url)

content = requests.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])