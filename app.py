import requests


class APIComunication():

    def __init__(self, apikey):

        self.base_url = "https://www.alphavantage.co/query?"
        self.function = "TIME_SERIES_DAILY"
        self.outputsize = "full"

        self.apikey = apikey
        self.base_url += f"apikey={self.apikey}"

        self.base_url += f"&function={self.function}"
        self.base_url += f"&outputsize={self.outputsize}"
        self.base_url += "&symbol=%s"

    def get_stock_prices(self, symbol):
        response = requests.get(self.base_url % symbol)
        data = response.json()
        data = data["Time Series (Daily)"]

        prices = { date: values["4. close"] for date, values in data.items() }
        return prices



# NYSE: New York Stock Exchange
NYSE = {
    "Microsoft": "MSFT",
    "Apple": "AAPL",
    "Amazon": "AMZN",
    "Google": "GOGL",
    "Facebook": "FBNK",
    "Alibaba": "BABA",
    "Netflix": "NFLX",
    "Disney": "DIS",
    "Spotify": "SPOT",
    "Uber": "UBER",
    "Tesla": "TSLA",
    "Under Armour": "UA"
}

APICon = APIComunication(apikey="GWT5VNWYEKMM0NLS")
prices = APICon.get_stock_prices(NYSE["Google"])

print(prices)
