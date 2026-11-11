import requests
import time
from bs4 import BeautifulSoup


RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
def parse_books(books):
    result = []
    for book in books:
        title = book.h3.a["title"]
        price = float(book.find("p", class_= "price_color").text.replace("£", ""))
        availability = book.find("p", class_="availability").text.strip()
        rating = book.find("p", class_ = "star-rating")["class"][1]
        result.append({
            "title" : title,
            "price" : price,
            "availability": availability,
            "rating": RATINGS[rating]
        })
    return result

def scrape_page(url):
    response = requests.get(url, timeout = 10)
    response.encoding = "utf8"
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_= "product_pod")
        result = parse_books(books)
    else:
        print(f"Failed to scrape {url}: status {response.status_code}")
        return []
    return result

all_books = []
for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    result = scrape_page(url)
    all_books.extend(result)
    time.sleep(1)
    print(f"Page{page}:{len(all_books)}")

titles = []
for book in all_books:
    titles.append(book["title"])
print(len(set(titles)))