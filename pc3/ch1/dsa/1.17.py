"""
Extracting a Subset of a Dictionary
"""
prices = {
    'acme': 45.23,
    'aapl': 612.78,
    'ibm': 205.55,
    'hpq': 37.20,
    'fb': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}
tech_names = {'aapl', 'ibm', 'hpq', 'msft'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p1)
print(p2)
print()
p1 = dict((key, value) for key, value in prices.items() if value > 200)
p2 = {key: prices[key] for key in prices.keys() & tech_names}
print(p1)
print(p2)
print()
