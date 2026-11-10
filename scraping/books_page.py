import requests

url = "https://books.toscrape.com/"

response = requests.get(url, timeout = 10)
response.encoding = "utf-8"

print(response.status_code)

print(response.text[:500])

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")


books = soup.find_all("article", class_= "product_pod")

print(len(books))

first = books[0]

print(first.h3.a["title"])
print(first.find("p", class_= "price_color").text)

# for book in books:
#     print(book.h3.a["title"])

def all_books(books):
    total_arr = []
    for book in books:
        total_dict = {}
        total_dict["title"] = book.h3.a["title"]
        new_price = book.find("p", class_= "price_color").text.replace("£", "")
        total_dict["price"] = float(new_price)
        total_arr.append(total_dict)
    return total_arr

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

print(parse_books(books))
