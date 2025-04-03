from collections import deque

def find_nearest_equipment(n, edges, availability, start_provider, target_equipment):
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    if target_equipment in availability.get(start_provider, []):
        return [start_provider]

    queue = deque([(start_provider, [start_provider])])
    visited = set([start_provider])

    while queue:
        provider, path = queue.popleft()
        for neighbor in graph[provider]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                if target_equipment in availability.get(neighbor, []):
                    return new_path
                queue.append((neighbor, new_path))
                visited.add(neighbor)

    return -1

# Case 1

n = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
availability = {1: ["excavator"], 2: [], 3: ["bulldozer"], 4: ["excavator"], 5: ["crane"]}
start_provider = 2
target_equipment = "excavator"

# Ouput : [2,1]

# Case 2

# n = 6
# edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# availability = {1: ["crane"], 2: ["excavator"], 3: ["bulldozer"], 4: ["crane"], 5: [], 6: ["excavator"]}
# start_provider = 2
# target_equipment = "excavator"


# Output: [2]


output = find_nearest_equipment(n, edges, availability, start_provider, target_equipment)

print(output)  
