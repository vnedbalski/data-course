# Day 1: Python basics — functions, loops, dictionaries, sorting


def sum_even(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total


def count_long(words, n):
    total = 0
    for word in words:
        if len(word) > n:
            total += 1
    return total


def my_max(nums):
    if not nums:
        return None
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value


def letter_counts(text):
    counts = {}
    for letter in text:
        if letter in counts:
            counts[letter] = counts[letter] + 1
        else:
            counts[letter] = 1
    return counts


def word_counts(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts


def top_words(text, n):
    counts = word_counts(text)
    pairs = list(counts.items())
    sorted_pairs = sorted(pairs, key=lambda p: p[1], reverse=True)
    return sorted_pairs[:n]


orders = [
    {"city": "Warsaw", "price": 120},
    {"city": "Gdansk", "price": 80},
    {"city": "Warsaw", "price": 200},
    {"city": "Lodz", "price": 50},
    {"city": "Gdansk", "price": 100},
]


def city_totals(orders):
    totals = {}
    for order in orders:
        city = order["city"]
        price = order["price"]
        if city in totals:
            totals[city] += price
        else:
            totals[city] = price
    return totals


def average_price(orders):
    totals = {}
    counts = {}
    for order in orders:
        city = order["city"]
        price = order["price"]
        if city in totals:
            totals[city] += price
            counts[city] += 1
        else:
            totals[city] = price
            counts[city] = 1

    averages = {}
    for city, total in totals.items():
        averages[city] = total / counts[city]
    return averages


print(sum_even([1, 2, 3, 4, 10]))                    # 16
print(count_long(["kot", "pies", "samochód"], 3))    # 2
print(my_max([-5, -2, -9]))                          # -2
print(my_max([]))                                    # None
print(letter_counts("banana"))                       # {'b': 1, 'a': 3, 'n': 2}
print(word_counts("Kot pies kot"))                   # {'kot': 2, 'pies': 1}
print(top_words("a b A c b a", 2))                   # [('a', 3), ('b', 2)]
print(city_totals(orders))                           # {'Warsaw': 320, 'Gdansk': 180, 'Lodz': 50}
print(average_price(orders))                         # {'Warsaw': 160.0, 'Gdansk': 90.0, 'Lodz': 50.0}