import requests
import smtplib, ssl, os

def send_email(message, receiver="s8timetz@gmail.com"):
    host = "smtp.gmail.com"
    port = 465
    username = "s8timetz@gmail.com"
    password = os.getenv("GMAIL_PW")
    # password = "" for test purposes only
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

api_key = "7a704fec9e2f4cd097570f8d16204386"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-15&sort" \
      "By=publishedAt&apiKey=7a704fec9e2f4cd097570f8d16204386"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
email_txt = f"""\
Subject: Tesla News Bot
"""

for article in content["articles"]:
    if article["title"] is not None:
        email_txt = email_txt + "\n" + "\n" + article["title"] + "\n" + article["description"]
        # print(article["title"])
        # print(article["description"])
    print(email_txt)

email_txt = email_txt.encode('utf-8')

send_email(email_txt, "s8timetz@gmail.com")


