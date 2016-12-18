"""
Finding the Largest or Smallest N Items
"""
import heapq

nums = [1, 8, 2, 24, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print()

portfolio = [
    {'name': 'ibm', 'shares': 100, 'price': 91.1},
    {'name': 'aapl', 'shares': 50, 'price': 543.22},
    {'name': 'fb', 'shares': 200, 'price': 21.09},
    {'name': 'hpq', 'shares': 35, 'price': 31.75},
    {'name': 'yhoo', 'shares': 45, 'price': 16.35},
    {'name': 'acme', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)
print()

heap = list(nums)
heapq.heapify(heap)
print(heap)
print()

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
