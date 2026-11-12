import requests

def get_rates(code, n):
    list_rates = []
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{code.lower()}/last/{n}/"
    response = requests.get(url, params={"format": "json"}, timeout=10)
    if response.status_code == 200:
        data = response.json()
        for rate in data["rates"]:
            list_rates.append({
                "date": rate["effectiveDate"],
                "code": data["code"],
                "rate": rate["mid"]
            })
    else:
        print(f"Failed to get {code}: status {response.status_code}") 
    return list_rates

print(get_rates("usd", 1))
print(get_rates("eur", 3))
print(get_rates("xyz", 5))