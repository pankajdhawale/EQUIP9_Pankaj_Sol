import heapq

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

# Example test case for Optimal Equipment Deal Matching
requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]
print("Optimal Equipment Deal Matching Output:", find_best_deals(requests, sellers))
