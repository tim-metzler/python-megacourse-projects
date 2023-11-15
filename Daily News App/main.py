import requests

api_key = "7a704fec9e2f4cd097570f8d16204386"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-15&sort" \
      "By=publishedAt&apiKey=7a704fec9e2f4cd097570f8d16204386"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
