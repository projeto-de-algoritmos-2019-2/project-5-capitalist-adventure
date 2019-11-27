import requests

def get_data(symbol):

    function = "TIME_SERIES_DAILY"
    apikey = "GWT5VNWYEKMM0NLS"
    outputsize = "full"

    base_url = "https://www.alphavantage.co/query?function=%s&apikey=%s&symbol=%s&outputsize=%s"
    base_url = base_url % (function, apikey, symbol, outputsize)
    response = requests.get(base_url)

    data = response.json()
    data = data["Time Series (Daily)"]
    data = { date: values["4. close"] for date, values in data.items() }

    return data


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

data = get_data(NYSE["Google"])

