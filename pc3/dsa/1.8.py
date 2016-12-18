"""
Calculating with Dictionaries
"""
prices = {
    'acme': 45.23,
    'aapl': 612.78,
    'ibm': 205.55,
    'hpq': 37.20,
    'fb': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
print()

print(min(prices))
print(max(prices))
print()

min_p = min(prices, key=lambda k: prices[k])
print(min(prices, key=lambda k: prices[k]))
print(prices[min_p])
max_p = max(prices, key=lambda k: prices[k])
print(max(prices, key=lambda k: prices[k]))
print(prices[max_p])
print()

another_price = {'aaa': 45.23, 'zzz': 45.23}
print(min(zip(another_price.values(), another_price.keys())))
print(max(zip(another_price.values(), another_price.keys())))
