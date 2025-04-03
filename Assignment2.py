import heapq

def match_requests_with_sellers(requests, sellers):
    seller_map = {}
    for equipment, price in sellers:
        if equipment not in seller_map:
            seller_map[equipment] = []
        heapq.heappush(seller_map[equipment], price)

    result = []
    for equipment, max_price in requests:
        if equipment in seller_map:
            while seller_map[equipment] and seller_map[equipment][0] > max_price:
                heapq.heappop(seller_map[equipment])
            result.append(seller_map[equipment][0] if seller_map[equipment] else None)
        else:
            result.append(None)

    return result

# case I input : 

requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

# Ouput : [45000, 68000]

# Case II Input: 

# requests = [("crane", 60000), ("excavator", 40000), ("bulldozer", 75000)]
# sellers = [("excavator", 42000), ("bulldozer", 73000), ("crane", 62000)]
# Output: [None, None, 73000]  


print(match_requests_with_sellers(requests, sellers))
