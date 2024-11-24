import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"  
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the page!")
    html_content = response.text  
    soup = BeautifulSoup(html_content, 'html.parser')

    titles = soup.find_all(['h2', 'h3'])

    print("Article Titles:")
    for title in titles:
        print(title.text.strip())  

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
