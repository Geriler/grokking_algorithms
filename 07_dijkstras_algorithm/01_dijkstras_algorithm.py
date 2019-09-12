graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "a": {
        "fin": 1
    },
    "b": {
        "a": 3,
        "fin": 5
    },
    "fin": {}
}

infinity = float("inf")

costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

processed = []
path = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


def find_next_node(name):
    path.append(name)
    for node in parents:
        if parents[node] == name and node not in path:
            return find_next_node(node)


find_next_node("start")
print(path)
print(costs["fin"])
