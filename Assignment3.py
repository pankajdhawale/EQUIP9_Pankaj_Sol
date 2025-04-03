import heapq
from bisect import bisect_left, bisect_right

def find_best_deals(requests, sellers):
    equipment_prices = {}
    for equipment, price in sellers:
        if equipment not in equipment_prices:
            equipment_prices[equipment] = []
        heapq.heappush(equipment_prices[equipment], price)
    
    results = []
    for equipment, max_price in requests:
        if equipment in equipment_prices and equipment_prices[equipment][0] <= max_price:
            results.append(heapq.heappop(equipment_prices[equipment]))
        else:
            results.append(None)
    
    return results

def maintenance_costs(maintenance_logs, queries):
    date_to_cost = {}
    prefix_sums = []
    dates = []
    total = 0
    
    for _, date, cost in maintenance_logs:
        if date not in date_to_cost:
            date_to_cost[date] = 0
        date_to_cost[date] += cost
    
    for date in sorted(date_to_cost.keys()):
        total += date_to_cost[date]
        dates.append(date)
        prefix_sums.append(total)
    
    results = []
    for start_date, end_date in queries:
        left = bisect_left(dates, start_date)
        right = bisect_right(dates, end_date) - 1
        if left <= right:
            results.append(prefix_sums[right] - (prefix_sums[left - 1] if left > 0 else 0))
        else:
            results.append(0)
    
    return results

# Example test case for Maintenance Log Analysis
maintenance_logs = [(101, "2024-01-01", 500), (102, "2024-01-10", 300), (101, "2024-01-15", 700)]
queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]
print(maintenance_costs(maintenance_logs, queries))
