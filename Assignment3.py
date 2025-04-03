class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, idx, value):
        while idx < len(self.tree):
            self.tree[idx] += value
            idx += idx & -idx  # Move to next index

    def prefix_sum(self, idx):
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx  # Move to parent index
        return total

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

def maintenance_costs(maintenance_logs, queries):
    date_map = {}
    sorted_dates = sorted(set(date for _, date, _ in maintenance_logs))
    
    for i, date in enumerate(sorted_dates):
        date_map[date] = i + 1  # 1-based indexing for BIT

    fenwick = FenwickTree(len(sorted_dates))

    for _, date, cost in maintenance_logs:
        fenwick.update(date_map[date], cost)

    results = []
    for start_date, end_date in queries:
        if start_date in date_map and end_date in date_map:
            results.append(fenwick.range_sum(date_map[start_date], date_map[end_date]))
        else:
            results.append(0)

    return results

# Input Case 1 :
maintenance_logs = [(101, "2024-01-01", 500), (102, "2024-01-10", 300), (101, "2024-01-15", 700)]
queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]

# Ouput : [800, 1500]

# Input Case 2
# maintenance_logs = [(201, "2024-02-02", 800), (202, "2024-02-08", 1200), (203, "2024-02-12", 600), (201, "2024-02-18", 1500), (204, "2024-02-22", 900), (205, "2024-02-28", 1100)]  
# queries = [("2024-02-02", "2024-02-12"), ("2024-02-08", "2024-02-22"), ("2024-02-12", "2024-02-28"), ("2024-02-01", "2024-02-28"), ("2024-02-15", "2024-02-20")]  

# Ouput : [2600, 4200, 4100, 0, 0]

print(maintenance_costs(maintenance_logs, queries))  # Output: [800, 1500]
