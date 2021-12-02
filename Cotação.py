def cotacao():
    
    import requests
    import locale

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    url = "https://api.bitvalor.com/v1/ticker.json"
    page = requests.get(url)
    data = page.json()
    price = data['ticker_1h']['exchanges']['MBT']['last']
    price = locale.currency(price, grouping=True)
    return price

print(cotacao())